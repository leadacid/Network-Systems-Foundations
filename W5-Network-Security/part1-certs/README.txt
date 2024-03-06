####
# One example workflow for creating signed digital certificates.  

# DONE BY CA
#  1) Certificate Authority creates a root certificate. This includes 
#  1a) creating a private/public key,
#  1b) creating the x.509 certificate that can be shared (e.g., installed in browsers)

# DONE BY WEBSERVER ADMIN
# 2) Each webserver will then create a certificate to be signed by the CA 
# 2a) create a private key 
# 2b) Create a certificate request.  
# 2c) Share the certificate request with a CA.

# DONE BY CA
# 3) CA validated the identity by some means, and then creates certificate.  Sends that back to WEBSERVER ADMIN

# DONE BY WEBSERVER ADMIN
# 4)  Then that can be installed on your webserver to be provided as part of the webserver configuration
# e.g., for nginx http://nginx.org/en/docs/http/configuring_https_servers.html
# e.g., for python code directly, see server.py 
# in both cases, you configure it with the webserver's private key, and the web server's signed certificate.


####
# LAB TASKS

# Provided are:
#  The folder CA - contains their private key, and root certificate. The private key is provided since we don't actually have a CA, and we'll pretend to be it.
#  webserver-req.ext - used in creating a certificate request 
#  server.py - example using the certificates (and a curl example is at the bottom of this README)

# You just need to run through Steps 2 and 3, and test it with step 4.

# What will be submitted is submission.tar containing:
#  webserver-private.pem 
#  webserver-cert.pem
# From the directory containing those files, you can run:
#   tar cf submission.tar webserver-cert.pem webserver-private.pem
# Note: those must be the exact file names in submission.tar, otherwise an error will occur. 

####


#### STEP 1
# Create CA certificate

openssl genrsa -out CA-private-key.key 2048
# No passphrase needed


# Create CA root certificate
openssl req -x509 -new -nodes -key CA-private-key.key -sha256 -days 1825 -out CA-root-certificate.pem

# It prompted for the follow (after the : is my answer)
Country Name (2 letter code) [AU]:US
State or Province Name (full name) [Some-State]:Colorado
Locality Name (eg, city) []:Boulder
Organization Name (eg, company) [Internet Widgits Pty Ltd]:Fake-CA
Organizational Unit Name (eg, section) []:Fake-Org
Common Name (e.g. server FQDN or YOUR name) []:Fake-Name
Email Address []:eric.keller@colorado.edu



### STEP 2

####  WEB Server - request a certificate to be signed by CA ###

# Generate private key for web server 
openssl genrsa -out webserver-private.key 2048

# create .pem format
openssl rsa -in webserver-private.key -text > webserver-private.pem

# Create a certificate request

openssl req -new -key webserver-private.key -out webserver-cert-request.csr

# Here's how I answered
Country Name (2 letter code) [AU]:US
State or Province Name (full name) [Some-State]:Colorado
Locality Name (eg, city) []:Louisville
Organization Name (eg, company) [Internet Widgits Pty Ltd]:FakeWS-Org
Organizational Unit Name (eg, section) []:FakeWS-Unit
Common Name (e.g. server FQDN or YOUR name) []:FakeWS-Name
Email Address []:fake@email.com

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:password
An optional company name []:FakeWS-CompanyName

# The webserver-req.ext file is an X509 V3 certificate extension config file, 
# which is used to define the Subject Alternative Name (SAN) 
# in our case - localhost 


### STEP 3

### CA creates certificate ###
# Web server admin will send the request (.csr and .ext) to the CA 
# The CA will run this on it's private servers.

openssl x509 -req -in ../server/webserver-cert-request.csr -CA CA-root-certificate.pem -CAkey CA-private-key.key -CAcreateserial -out ../server/webserver-cert.crt -days 1000 -sha256 -extfile ../webserver-req.ext

# convert the crt format to pem 
openssl x509 -in webserver-cert.crt -out webserver-cert.pem


### STEP 4

#### Server can now create a webserver, using webserver-cert.pem
See server.py

# Any clients need to have the root certificate installed locally
# one option is to use curl 
curl --cacert /home/coder/project/learn/part1-certs/CA/CA-root-certificate.pem https://localhost:4443






