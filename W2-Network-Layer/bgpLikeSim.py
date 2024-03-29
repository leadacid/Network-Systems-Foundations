# Task: Create some functions for a simplified BGP router
#   Specifically, the withdraw, update, and next_hop functions of the Router
#   The class Route will be used.
# 
#   withdraw(rt) - rt is type Route. If a simplified BGP router gets this message, it will   
#

import ipaddress

class Route:
    # A prefix is in form 
    neighbor = ""  # The router that send this router - will be a.b.c.d
    prefix = ""    # The IP address portion of a prefix - will be a.b.c.d
    prefix_len = 0 # The length portion of a prefix - will be an integer
    path = []      # the AS path - list of integers

    def __init__(self, neigh, p, plen, path):
        self.neighbor = neigh
        self.prefix = p
        self.prefix_len = plen
        self.path = path 

    # convert Route to a String    
    def __str__(self):
        return self.prefix+"/"+str(self.prefix_len)+"- ASPATH: " + str(self.path)+", neigh: "+self.neighbor

    # Get the prefix in the a.b.c.d/x format
    def pfx_str(self):
        return self.prefix+"/"+str(self.prefix_len)


# Implement the following functions:
#  update - the router received a route advertisement (which can be a new one, or an update
#         - the function needs to store the route in the RIB
#  withdraw - the router received a route withdraw message
#          - the function needs to delete the route in the RIB
#  nexthop - given ipaddr in a.b.c.d format as a string (e.g., "10.1.2.3"), perform a longest prefix match in the RIB
#          - Select the best route among multiple routes for that prefix by path length.  
#          - if same length, return either

class Router:
    # You can use a different data structure
    # dictionary with key of the prefix, value a list of Route
    # example: rib["10.0.0.0/24"] = [Route("1.1.1.1", "10.0.0.0", 24, [1,2,3]), 
    #                                Route("2.2.2.2", "10.0.0.0", 24, [10,20])]
    #          rib["10.0.0.0/22"] = [Route("3.3.3.3", "10.0.0.0", 22, [33,44,55,66]]
    rib = {} 

    # If you use the same data structure for the rib, this will print it
    def printRIB(self):
        for pfx in self.rib.keys():
            for route in self.rib[pfx]:
                print(route) 


    # TASK
    def update(self, rt):
        # YOUR CODE HERE
        rtp = rt.pfx_str()
        if rtp not in self.rib: #check if the prefix doesn't exist
            self.rib[rtp] = [rt]
        else:
            for c, r in enumerate(self.rib[rtp]): #check if the neighbor is already in the prefix
                if r.neighbor == rt.neighbor:
                    self.rib[rtp][c] = rt
                    break
                else: # neighbord not in prefix, we append route
                    if c == len(self.rib[rtp]) - 1:
                        self.rib[rtp].append(rt)

                
        return



    # TASK    
    def withdraw(self, rt):
        # YOUR CODE HERE
        rtp = rt.pfx_str()
        if rtp in self.rib:  # check to see if the prefix is in the RIB
            for r in self.rib[rtp]: # go through each route in the prefix
                if str(r) == str(rt):  #comparing strings, as to not have to implement an eq method in the class
                    self.rib[rtp].remove(r)
                else:
                    continue
            if self.rib[rtp] == []: # if the prefix is empty, we should remove
                del self.rib[rtp]

        else:
            pass
        return 


    # ipaddr in a.b.c.d format
    # find longest prefix that matches
    # then find shortest path of routes for that prefix
    def next_hop(self, ipaddr):
        retval = None
        best_prefix = None
        best_l = 0

        for pref in self.rib.keys():   # Loop through each prefix in the rib
            if ipaddress.ip_address(ipaddr) in ipaddress.ip_network(pref):  # Check to see if ipadress fits in prefix net
                if int(pref[-2:]) > best_l:     # There maybe multiple candidates so we choose the highest prefix
                    best_l = int(pref[-2:])
                    best_prefix = pref
        print("Best_prefix:")
        print(best_prefix)

        if(best_prefix != None):         # There maybe a case where there is no route possible    
            v = 100
            for r in self.rib[best_prefix]:
                cost = len(r.path)          # Weights are 0, so no need to implement OSPF, number of hops is enough for this sim
                if cost < v:
                    v = cost
                    print(cost)
                    retval = r.neighbor
        print("Returning")
        print(retval)
        return retval


def test_cases():
    rtr = Router()

    #Test that withdrawing a non-existant route works
    rtr.withdraw (Route("1.1.1.1", "10.0.0.0", 24, [3,4,5]))

    #Test updates work - same prefix, two neighbors
    rtr.update (Route("1.1.1.1", "10.0.0.0", 24, [3,4,5]))
    rtr.update (Route("2.2.2.2", "10.0.0.0", 24, [1,2]))

    #print("RIB")
    #rtr.printRIB()

    #Test updates work - overwriting an existing route from a neighbor
    rtr.update (Route("2.2.2.2", "10.0.0.0", 24, [1, 22, 33, 44]))

    #print("RIB")
    #rtr.printRIB()

    #Test updates work - an overlapping prefix (this case, a shorter prefix)
    rtr.update (Route("2.2.2.2", "10.0.0.0", 22, [4,5,7,8]))

    #Test updates work - completely different prefix
    rtr.update (Route("2.2.2.2", "12.0.0.0", 16, [4,5]))
    rtr.update (Route("1.1.1.1", "12.0.0.0", 16, [1, 2, 30]))

    print("RIB")
    rtr.printRIB()
    print("-------------------")

    # Should Fail
    print("One")
    nh = rtr.next_hop("10.2.0.13")
    assert nh == None

    print("Two")
    nh = rtr.next_hop("10.0.0.13")
    assert nh == "1.1.1.1"

    # Test withdraw - withdraw the route from 1.1.1.1 that we just matched
    rtr.withdraw (Route("1.1.1.1", "10.0.0.0", 24, [3,4,5]))

    # Should match something different

    print("Three")
    nh = rtr.next_hop("10.0.0.13")
    assert nh == "2.2.2.2"

    # Re-announce - so, 1.1.1.1 would now be best route
    rtr.withdraw (Route("1.1.1.1", "10.0.0.0", 24, [3,4,5]))

    
    print("Four")
    rtr.update (Route("2.2.2.2", "10.0.0.0", 22, [4,5,7,8]))
    # Should match 10.0.0.0/22 (next hop 2.2.2.2) but not 10.0.0.0/24 (next hop 1.1.1.1)
    nh = rtr.next_hop("10.0.1.77")
    assert nh == "2.2.2.2"

    print("Five")
    # Test a different prefix
    nh = rtr.next_hop("12.0.12.0")
    assert nh == "2.2.2.2"

    print("Six")
    rtr.update (Route("1.1.1.1", "20.0.0.0", 16, [4,5,7,8]))
    rtr.update (Route("2.2.2.2", "20.0.0.0", 16, [44,55]))
    nh = rtr.next_hop("20.0.12.0")
    assert nh == "2.2.2.2"

    print("Seven")
    rtr.update (Route("1.1.1.1", "20.0.12.0", 24, [44,55,66,77,88]))
    nh = rtr.next_hop("20.0.12.0")
    assert nh == "1.1.1.1"


    # Remember to delete the entry from the RIB, not just removing the specific route
    # That is, when you withdraw, remove the route for the prefix, and if there are 0 routes, remove the prefix from the RIB
    rtr.withdraw(Route("1.1.1.1", "20.0.12.0", 24, [44,55,66,77,88]))
    nh = rtr.next_hop("20.0.12.0")
    assert nh == "2.2.2.2"

if __name__ == "__main__":
    test_cases()
    

