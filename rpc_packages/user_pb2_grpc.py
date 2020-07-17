# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from rpc_packages import user_pb2 as user__pb2


class UserRpcServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.registerUser = channel.unary_unary(
                '/user_service.UserRpcService/registerUser',
                request_serializer=user__pb2.registerUserRequest.SerializeToString,
                response_deserializer=user__pb2.registerUserResponse.FromString,
                )
        self.userLogin = channel.unary_unary(
                '/user_service.UserRpcService/userLogin',
                request_serializer=user__pb2.userLoginRequest.SerializeToString,
                response_deserializer=user__pb2.userLoginResponse.FromString,
                )
        self.userProfile = channel.unary_unary(
                '/user_service.UserRpcService/userProfile',
                request_serializer=user__pb2.userProfileRequest.SerializeToString,
                response_deserializer=user__pb2.userProfileResponse.FromString,
                )


class UserRpcServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def registerUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def userLogin(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def userProfile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserRpcServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'registerUser': grpc.unary_unary_rpc_method_handler(
                    servicer.registerUser,
                    request_deserializer=user__pb2.registerUserRequest.FromString,
                    response_serializer=user__pb2.registerUserResponse.SerializeToString,
            ),
            'userLogin': grpc.unary_unary_rpc_method_handler(
                    servicer.userLogin,
                    request_deserializer=user__pb2.userLoginRequest.FromString,
                    response_serializer=user__pb2.userLoginResponse.SerializeToString,
            ),
            'userProfile': grpc.unary_unary_rpc_method_handler(
                    servicer.userProfile,
                    request_deserializer=user__pb2.userProfileRequest.FromString,
                    response_serializer=user__pb2.userProfileResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'user_service.UserRpcService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserRpcService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def registerUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user_service.UserRpcService/registerUser',
            user__pb2.registerUserRequest.SerializeToString,
            user__pb2.registerUserResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def userLogin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user_service.UserRpcService/userLogin',
            user__pb2.userLoginRequest.SerializeToString,
            user__pb2.userLoginResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def userProfile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user_service.UserRpcService/userProfile',
            user__pb2.userProfileRequest.SerializeToString,
            user__pb2.userProfileResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
