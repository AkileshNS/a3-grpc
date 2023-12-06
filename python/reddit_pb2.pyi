from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PostState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    POST_NORMAL: _ClassVar[PostState]
    POST_LOCKED: _ClassVar[PostState]
    POST_HIDDEN: _ClassVar[PostState]

class CommentState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    COMMENT_NORMAL: _ClassVar[CommentState]
    COMMENT_HIDDEN: _ClassVar[CommentState]

class SubRedditState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SUBREDDIT_PUBLIC: _ClassVar[SubRedditState]
    SUBREDDIT_PRIVATE: _ClassVar[SubRedditState]
    SUBREDDIT_HIDDEN: _ClassVar[SubRedditState]

class PostVoteType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    POST_UPVOTE: _ClassVar[PostVoteType]
    POST_DOWNVOTE: _ClassVar[PostVoteType]

class CommentVoteType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    COMMENT_UPVOTE: _ClassVar[CommentVoteType]
    COMMENT_DOWNVOTE: _ClassVar[CommentVoteType]
POST_NORMAL: PostState
POST_LOCKED: PostState
POST_HIDDEN: PostState
COMMENT_NORMAL: CommentState
COMMENT_HIDDEN: CommentState
SUBREDDIT_PUBLIC: SubRedditState
SUBREDDIT_PRIVATE: SubRedditState
SUBREDDIT_HIDDEN: SubRedditState
POST_UPVOTE: PostVoteType
POST_DOWNVOTE: PostVoteType
COMMENT_UPVOTE: CommentVoteType
COMMENT_DOWNVOTE: CommentVoteType

class User(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class Post(_message.Message):
    __slots__ = ["author", "score", "state", "date", "sub_reddit", "post_id"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    SUB_REDDIT_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    author: User
    score: int
    state: PostState
    date: _timestamp_pb2.Timestamp
    sub_reddit: SubReddit
    post_id: str
    def __init__(self, author: _Optional[_Union[User, _Mapping]] = ..., score: _Optional[int] = ..., state: _Optional[_Union[PostState, str]] = ..., date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., sub_reddit: _Optional[_Union[SubReddit, _Mapping]] = ..., post_id: _Optional[str] = ...) -> None: ...

class Content(_message.Message):
    __slots__ = ["post", "comment"]
    POST_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    post: Post
    comment: Comment
    def __init__(self, post: _Optional[_Union[Post, _Mapping]] = ..., comment: _Optional[_Union[Comment, _Mapping]] = ...) -> None: ...

class Comment(_message.Message):
    __slots__ = ["author", "score", "state", "date", "comment_on", "comment_id"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    COMMENT_ON_FIELD_NUMBER: _ClassVar[int]
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    author: User
    score: int
    state: CommentState
    date: _timestamp_pb2.Timestamp
    comment_on: Content
    comment_id: str
    def __init__(self, author: _Optional[_Union[User, _Mapping]] = ..., score: _Optional[int] = ..., state: _Optional[_Union[CommentState, str]] = ..., date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., comment_on: _Optional[_Union[Content, _Mapping]] = ..., comment_id: _Optional[str] = ...) -> None: ...

class SubReddit(_message.Message):
    __slots__ = ["name", "state", "tags"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: SubRedditState
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., state: _Optional[_Union[SubRedditState, str]] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...

class CreatePostRequest(_message.Message):
    __slots__ = ["post"]
    POST_FIELD_NUMBER: _ClassVar[int]
    post: Post
    def __init__(self, post: _Optional[_Union[Post, _Mapping]] = ...) -> None: ...

class CreatePostResponse(_message.Message):
    __slots__ = ["response"]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: str
    def __init__(self, response: _Optional[str] = ...) -> None: ...

class VotePostRequest(_message.Message):
    __slots__ = ["post_id", "vote"]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    VOTE_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    vote: PostVoteType
    def __init__(self, post_id: _Optional[str] = ..., vote: _Optional[_Union[PostVoteType, str]] = ...) -> None: ...

class VotePostResponse(_message.Message):
    __slots__ = ["response"]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: str
    def __init__(self, response: _Optional[str] = ...) -> None: ...

class GetPostRequest(_message.Message):
    __slots__ = ["post_id"]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    def __init__(self, post_id: _Optional[str] = ...) -> None: ...

class GetPostResponse(_message.Message):
    __slots__ = ["post"]
    POST_FIELD_NUMBER: _ClassVar[int]
    post: Post
    def __init__(self, post: _Optional[_Union[Post, _Mapping]] = ...) -> None: ...

class CreateCommentRequest(_message.Message):
    __slots__ = ["comment"]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    comment: Comment
    def __init__(self, comment: _Optional[_Union[Comment, _Mapping]] = ...) -> None: ...

class CreateCommentResponse(_message.Message):
    __slots__ = ["response"]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: str
    def __init__(self, response: _Optional[str] = ...) -> None: ...

class VoteCommentRequest(_message.Message):
    __slots__ = ["comment_id", "vote"]
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    VOTE_FIELD_NUMBER: _ClassVar[int]
    comment_id: str
    vote: PostVoteType
    def __init__(self, comment_id: _Optional[str] = ..., vote: _Optional[_Union[PostVoteType, str]] = ...) -> None: ...

class VoteCommentResponse(_message.Message):
    __slots__ = ["response"]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: str
    def __init__(self, response: _Optional[str] = ...) -> None: ...

class GetPostTopCommentsRequest(_message.Message):
    __slots__ = ["post_id", "n"]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    N_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    n: int
    def __init__(self, post_id: _Optional[str] = ..., n: _Optional[int] = ...) -> None: ...

class GetPostTopCommentsResponse(_message.Message):
    __slots__ = ["comments"]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    comments: _containers.RepeatedCompositeFieldContainer[Comment]
    def __init__(self, comments: _Optional[_Iterable[_Union[Comment, _Mapping]]] = ...) -> None: ...

class GetCommentTopCommentsRequest(_message.Message):
    __slots__ = ["comment_id", "n"]
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    N_FIELD_NUMBER: _ClassVar[int]
    comment_id: str
    n: int
    def __init__(self, comment_id: _Optional[str] = ..., n: _Optional[int] = ...) -> None: ...

class GetCommentTopCommentsResponse(_message.Message):
    __slots__ = ["top_n_comments", "top_n_comments_comments"]
    TOP_N_COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TOP_N_COMMENTS_COMMENTS_FIELD_NUMBER: _ClassVar[int]
    top_n_comments: _containers.RepeatedCompositeFieldContainer[Comment]
    top_n_comments_comments: _containers.RepeatedCompositeFieldContainer[Comment]
    def __init__(self, top_n_comments: _Optional[_Iterable[_Union[Comment, _Mapping]]] = ..., top_n_comments_comments: _Optional[_Iterable[_Union[Comment, _Mapping]]] = ...) -> None: ...

class GetContentScoreUpdatesRequest(_message.Message):
    __slots__ = ["post_id", "comment_id"]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    comment_id: str
    def __init__(self, post_id: _Optional[str] = ..., comment_id: _Optional[str] = ...) -> None: ...

class GetContentScoreUpdatesResponse(_message.Message):
    __slots__ = ["score"]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: int
    def __init__(self, score: _Optional[int] = ...) -> None: ...
