# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import service_pb2 as service__pb2


class TestServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.tell_me_a_fact = channel.unary_unary(
                '/TestService/tell_me_a_fact',
                request_serializer=service__pb2.FactBasis.SerializeToString,
                response_deserializer=service__pb2.Fact.FromString,
                )
        self.get_advice = channel.unary_unary(
                '/TestService/get_advice',
                request_serializer=service__pb2.AnimeRequest.SerializeToString,
                response_deserializer=service__pb2.AnimeAdvice.FromString,
                )


class TestServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def tell_me_a_fact(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_advice(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TestServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'tell_me_a_fact': grpc.unary_unary_rpc_method_handler(
                    servicer.tell_me_a_fact,
                    request_deserializer=service__pb2.FactBasis.FromString,
                    response_serializer=service__pb2.Fact.SerializeToString,
            ),
            'get_advice': grpc.unary_unary_rpc_method_handler(
                    servicer.get_advice,
                    request_deserializer=service__pb2.AnimeRequest.FromString,
                    response_serializer=service__pb2.AnimeAdvice.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TestService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TestService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def tell_me_a_fact(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TestService/tell_me_a_fact',
            service__pb2.FactBasis.SerializeToString,
            service__pb2.Fact.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_advice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TestService/get_advice',
            service__pb2.AnimeRequest.SerializeToString,
            service__pb2.AnimeAdvice.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
