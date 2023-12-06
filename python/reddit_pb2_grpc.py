# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import reddit_pb2 as reddit__pb2


class RedditStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreatePost = channel.unary_unary(
                '/Reddit/CreatePost',
                request_serializer=reddit__pb2.CreatePostRequest.SerializeToString,
                response_deserializer=reddit__pb2.CreatePostResponse.FromString,
                )
        self.VoteOnPost = channel.unary_unary(
                '/Reddit/VoteOnPost',
                request_serializer=reddit__pb2.VotePostRequest.SerializeToString,
                response_deserializer=reddit__pb2.VotePostResponse.FromString,
                )
        self.GetPost = channel.unary_unary(
                '/Reddit/GetPost',
                request_serializer=reddit__pb2.GetPostRequest.SerializeToString,
                response_deserializer=reddit__pb2.GetPostResponse.FromString,
                )
        self.CreateComment = channel.unary_unary(
                '/Reddit/CreateComment',
                request_serializer=reddit__pb2.CreateCommentRequest.SerializeToString,
                response_deserializer=reddit__pb2.CreateCommentResponse.FromString,
                )
        self.VoteOnComment = channel.unary_unary(
                '/Reddit/VoteOnComment',
                request_serializer=reddit__pb2.VoteCommentRequest.SerializeToString,
                response_deserializer=reddit__pb2.VoteCommentResponse.FromString,
                )
        self.GetPostTopComments = channel.unary_unary(
                '/Reddit/GetPostTopComments',
                request_serializer=reddit__pb2.GetPostTopCommentsRequest.SerializeToString,
                response_deserializer=reddit__pb2.GetPostTopCommentsResponse.FromString,
                )
        self.GetCommentTopComments = channel.unary_unary(
                '/Reddit/GetCommentTopComments',
                request_serializer=reddit__pb2.GetCommentTopCommentsRequest.SerializeToString,
                response_deserializer=reddit__pb2.GetCommentTopCommentsResponse.FromString,
                )
        self.GetContentScoreUpdates = channel.stream_stream(
                '/Reddit/GetContentScoreUpdates',
                request_serializer=reddit__pb2.GetContentScoreUpdatesRequest.SerializeToString,
                response_deserializer=reddit__pb2.GetContentScoreUpdatesResponse.FromString,
                )


class RedditServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreatePost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VoteOnPost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateComment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VoteOnComment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPostTopComments(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCommentTopComments(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetContentScoreUpdates(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RedditServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreatePost': grpc.unary_unary_rpc_method_handler(
                    servicer.CreatePost,
                    request_deserializer=reddit__pb2.CreatePostRequest.FromString,
                    response_serializer=reddit__pb2.CreatePostResponse.SerializeToString,
            ),
            'VoteOnPost': grpc.unary_unary_rpc_method_handler(
                    servicer.VoteOnPost,
                    request_deserializer=reddit__pb2.VotePostRequest.FromString,
                    response_serializer=reddit__pb2.VotePostResponse.SerializeToString,
            ),
            'GetPost': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPost,
                    request_deserializer=reddit__pb2.GetPostRequest.FromString,
                    response_serializer=reddit__pb2.GetPostResponse.SerializeToString,
            ),
            'CreateComment': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateComment,
                    request_deserializer=reddit__pb2.CreateCommentRequest.FromString,
                    response_serializer=reddit__pb2.CreateCommentResponse.SerializeToString,
            ),
            'VoteOnComment': grpc.unary_unary_rpc_method_handler(
                    servicer.VoteOnComment,
                    request_deserializer=reddit__pb2.VoteCommentRequest.FromString,
                    response_serializer=reddit__pb2.VoteCommentResponse.SerializeToString,
            ),
            'GetPostTopComments': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPostTopComments,
                    request_deserializer=reddit__pb2.GetPostTopCommentsRequest.FromString,
                    response_serializer=reddit__pb2.GetPostTopCommentsResponse.SerializeToString,
            ),
            'GetCommentTopComments': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCommentTopComments,
                    request_deserializer=reddit__pb2.GetCommentTopCommentsRequest.FromString,
                    response_serializer=reddit__pb2.GetCommentTopCommentsResponse.SerializeToString,
            ),
            'GetContentScoreUpdates': grpc.stream_stream_rpc_method_handler(
                    servicer.GetContentScoreUpdates,
                    request_deserializer=reddit__pb2.GetContentScoreUpdatesRequest.FromString,
                    response_serializer=reddit__pb2.GetContentScoreUpdatesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Reddit', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Reddit(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreatePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Reddit/CreatePost',
            reddit__pb2.CreatePostRequest.SerializeToString,
            reddit__pb2.CreatePostResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VoteOnPost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Reddit/VoteOnPost',
            reddit__pb2.VotePostRequest.SerializeToString,
            reddit__pb2.VotePostResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Reddit/GetPost',
            reddit__pb2.GetPostRequest.SerializeToString,
            reddit__pb2.GetPostResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateComment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Reddit/CreateComment',
            reddit__pb2.CreateCommentRequest.SerializeToString,
            reddit__pb2.CreateCommentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VoteOnComment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Reddit/VoteOnComment',
            reddit__pb2.VoteCommentRequest.SerializeToString,
            reddit__pb2.VoteCommentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPostTopComments(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Reddit/GetPostTopComments',
            reddit__pb2.GetPostTopCommentsRequest.SerializeToString,
            reddit__pb2.GetPostTopCommentsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCommentTopComments(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Reddit/GetCommentTopComments',
            reddit__pb2.GetCommentTopCommentsRequest.SerializeToString,
            reddit__pb2.GetCommentTopCommentsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetContentScoreUpdates(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/Reddit/GetContentScoreUpdates',
            reddit__pb2.GetContentScoreUpdatesRequest.SerializeToString,
            reddit__pb2.GetContentScoreUpdatesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
