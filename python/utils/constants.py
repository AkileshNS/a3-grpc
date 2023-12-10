from google.protobuf.timestamp_pb2 import Timestamp
import reddit_pb2 as r_pb2

DUPLICATE_POST_ID_RESPONSE = "Post with Post ID already exists"
POST_RESPONSE = "Post created successfully"
VOTE_POST_RESPONSE = "Vote on post stored"
VOTE_COMMENT_RESPONSE = "Vote on comment stored"
POST_NOT_FOUND = "Post not found"
COMMENT_RESPONSE = "Comment created successfully"

HOST = "localhost"
PORT = 50051

post1 = r_pb2.Post(title = "You won't believe this!", content = "Dog drives car", video_url="r.com/123", author = r_pb2.User(user_id="A"), score = 20, state = r_pb2.POST_NORMAL, sub_reddit = r_pb2.SubReddit(name="r/Dogs", state=r_pb2.SUBREDDIT_PUBLIC), post_id = 'P1')
post2 = r_pb2.Post(title = "FUNNY", content = "2010 Memes", image_url="r.com/235", author = r_pb2.User(user_id="B"), score = 25, state = r_pb2.POST_NORMAL, sub_reddit = r_pb2.SubReddit(name="r/memes", state=r_pb2.SUBREDDIT_PUBLIC), post_id = 'P2')
post3 = r_pb2.Post(title = "Architectural Wonders", content = "The Burj Khalifa", image_url="r.com/236", author = r_pb2.User(user_id="C"), score = 30, state = r_pb2.POST_NORMAL, sub_reddit = r_pb2.SubReddit(name="r/Architecture", state=r_pb2.SUBREDDIT_PUBLIC), post_id = 'P3')
post4 = r_pb2.Post(title = "Friends Fan Theory", content = "Ross dies in episode 1", video_url="r.com/237", author = r_pb2.User(user_id="D"), score = 35, state = r_pb2.POST_NORMAL, sub_reddit = r_pb2.SubReddit(name="r/Friends", state=r_pb2.SUBREDDIT_PUBLIC), post_id = 'P4')

comment1 = r_pb2.Comment(author=r_pb2.User(user_id="A"), score=0, state = r_pb2.COMMENT_NORMAL, comment_on=r_pb2.Content(content_type=r_pb2.POST, post_id='P1'), comment_id='C1', replies_present=True)

comment2 = r_pb2.Comment(author=r_pb2.User(user_id="B"), score=5, state = r_pb2.COMMENT_NORMAL, comment_on=r_pb2.Content(content_type=r_pb2.COMMENT, comment_id='C1'), comment_id='C2', replies_present=True)
comment3 = r_pb2.Comment(author=r_pb2.User(user_id="C"), score=10, state = r_pb2.COMMENT_NORMAL, comment_on=r_pb2.Content(content_type=r_pb2.COMMENT, comment_id='C1'), comment_id='C3', replies_present=True)
comment4 = r_pb2.Comment(author=r_pb2.User(user_id="D"), score=15, state = r_pb2.COMMENT_NORMAL, comment_on=r_pb2.Content(content_type=r_pb2.COMMENT, comment_id='C1'), comment_id='C4', replies_present=True)
comment5 = r_pb2.Comment(author=r_pb2.User(user_id="E"), score=20, state = r_pb2.COMMENT_NORMAL, comment_on=r_pb2.Content(content_type=r_pb2.COMMENT, comment_id='C1'), comment_id='C5', replies_present=True)

comment6 = r_pb2.Comment(author=r_pb2.User(user_id="F"), score=5, state = r_pb2.COMMENT_NORMAL, comment_on=r_pb2.Content(content_type=r_pb2.COMMENT, comment_id='C2'), comment_id='C6', replies_present=True)
comment7 = r_pb2.Comment(author=r_pb2.User(user_id="G"), score=10, state = r_pb2.COMMENT_NORMAL, comment_on=r_pb2.Content(content_type=r_pb2.COMMENT, comment_id='C2'), comment_id='C7', replies_present=True)
comment8 = r_pb2.Comment(author=r_pb2.User(user_id="H"), score=15, state = r_pb2.COMMENT_NORMAL, comment_on=r_pb2.Content(content_type=r_pb2.COMMENT, comment_id='C2'), comment_id='C8', replies_present=True)
comment9 = r_pb2.Comment(author=r_pb2.User(user_id="I"), score=20, state = r_pb2.COMMENT_NORMAL, comment_on=r_pb2.Content(content_type=r_pb2.COMMENT, comment_id='C2'), comment_id='C9', replies_present=True)

comment10 = r_pb2.Comment(author=r_pb2.User(user_id="J"), score=5, state = r_pb2.COMMENT_NORMAL, comment_on=r_pb2.Content(content_type=r_pb2.COMMENT, comment_id='C3'), comment_id='C10', replies_present=True)
comment11 = r_pb2.Comment(author=r_pb2.User(user_id="K"), score=10, state = r_pb2.COMMENT_NORMAL, comment_on=r_pb2.Content(content_type=r_pb2.COMMENT, comment_id='C3'), comment_id='C11', replies_present=True)
comment12 = r_pb2.Comment(author=r_pb2.User(user_id="L"), score=15, state = r_pb2.COMMENT_NORMAL, comment_on=r_pb2.Content(content_type=r_pb2.COMMENT, comment_id='C3'), comment_id='C12', replies_present=True)
comment13 = r_pb2.Comment(author=r_pb2.User(user_id="M"), score=20, state = r_pb2.COMMENT_NORMAL, comment_on=r_pb2.Content(content_type=r_pb2.COMMENT, comment_id='C3'), comment_id='C13', replies_present=True)

comment14 = r_pb2.Comment(author=r_pb2.User(user_id="N"), score=5, state = r_pb2.COMMENT_NORMAL, comment_on=r_pb2.Content(content_type=r_pb2.COMMENT, comment_id='C4'), comment_id='C14', replies_present=True)
comment15 = r_pb2.Comment(author=r_pb2.User(user_id="O"), score=10, state = r_pb2.COMMENT_NORMAL, comment_on=r_pb2.Content(content_type=r_pb2.COMMENT, comment_id='C4'), comment_id='C15', replies_present=True)
comment16 = r_pb2.Comment(author=r_pb2.User(user_id="P"), score=15, state = r_pb2.COMMENT_NORMAL, comment_on=r_pb2.Content(content_type=r_pb2.COMMENT, comment_id='C4'), comment_id='C16', replies_present=True)
comment17 = r_pb2.Comment(author=r_pb2.User(user_id="Q"), score=20, state = r_pb2.COMMENT_NORMAL, comment_on=r_pb2.Content(content_type=r_pb2.COMMENT, comment_id='C4'), comment_id='C17', replies_present=True)

comment18 = r_pb2.Comment(author=r_pb2.User(user_id="R"), score=5, state = r_pb2.COMMENT_NORMAL, comment_on=r_pb2.Content(content_type=r_pb2.COMMENT, comment_id='C5'), comment_id='C14', replies_present=True)
comment19 = r_pb2.Comment(author=r_pb2.User(user_id="S"), score=10, state = r_pb2.COMMENT_NORMAL, comment_on=r_pb2.Content(content_type=r_pb2.COMMENT, comment_id='C5'), comment_id='C15', replies_present=True)
comment20 = r_pb2.Comment(author=r_pb2.User(user_id="T"), score=15, state = r_pb2.COMMENT_NORMAL, comment_on=r_pb2.Content(content_type=r_pb2.COMMENT, comment_id='C5'), comment_id='C16', replies_present=True)
comment21 = r_pb2.Comment(author=r_pb2.User(user_id="U"), score=20, state = r_pb2.COMMENT_NORMAL, comment_on=r_pb2.Content(content_type=r_pb2.COMMENT, comment_id='C5'), comment_id='C17', replies_present=True)


COMMENTS = [comment1, comment2, comment3, comment4, comment5, comment6, comment7, comment8, comment9, comment10, comment11, comment12,
            comment13, comment14, comment15, comment16, comment17, comment18, comment19, comment20, comment21]

POSTS = [post1, post2, post3, post4]