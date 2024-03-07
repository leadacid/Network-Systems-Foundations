# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import moderate_pb2 as moderate__pb2


class EricStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ericFunction = channel.unary_unary(
                '/Eric/ericFunction',
                request_serializer=moderate__pb2.FunctionParameter.SerializeToString,
                response_deserializer=moderate__pb2.FunctionReturnVal.FromString,
                )


class EricServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ericFunction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EricServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ericFunction': grpc.unary_unary_rpc_method_handler(
                    servicer.ericFunction,
                    request_deserializer=moderate__pb2.FunctionParameter.FromString,
                    response_serializer=moderate__pb2.FunctionReturnVal.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Eric', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Eric(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ericFunction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Eric/ericFunction',
            moderate__pb2.FunctionParameter.SerializeToString,
            moderate__pb2.FunctionReturnVal.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class MyFunctionsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.myfunction1 = channel.unary_unary(
                '/MyFunctions/myfunction1',
                request_serializer=moderate__pb2.FunctionParameter.SerializeToString,
                response_deserializer=moderate__pb2.FunctionReturnVal.FromString,
                )
        self.myfunction2 = channel.unary_unary(
                '/MyFunctions/myfunction2',
                request_serializer=moderate__pb2.FunctionParameter.SerializeToString,
                response_deserializer=moderate__pb2.FunctionReturnVal.FromString,
                )


class MyFunctionsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def myfunction1(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def myfunction2(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MyFunctionsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'myfunction1': grpc.unary_unary_rpc_method_handler(
                    servicer.myfunction1,
                    request_deserializer=moderate__pb2.FunctionParameter.FromString,
                    response_serializer=moderate__pb2.FunctionReturnVal.SerializeToString,
            ),
            'myfunction2': grpc.unary_unary_rpc_method_handler(
                    servicer.myfunction2,
                    request_deserializer=moderate__pb2.FunctionParameter.FromString,
                    response_serializer=moderate__pb2.FunctionReturnVal.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'MyFunctions', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MyFunctions(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def myfunction1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MyFunctions/myfunction1',
            moderate__pb2.FunctionParameter.SerializeToString,
            moderate__pb2.FunctionReturnVal.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def myfunction2(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MyFunctions/myfunction2',
            moderate__pb2.FunctionParameter.SerializeToString,
            moderate__pb2.FunctionReturnVal.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)