from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from forum.models import Post, Comment
import json

"""
 generate a CSV file for them with a line for each post that includes 
 1)the number of comments the post has, 
 2)the number of comments with positive sentiment,
 3)the number of comments with negative sentiment
"""


db_url='postgres://admin:password@3.220.167.6:80/forum'
engine = create_engine(db_url)
sm = sessionmaker(bind=engine)
session = sm()

comments = (
    session.query(Comment.post_id, func.count("*").label("comments"))
    .group_by(Comment.post_id)
    .subquery()
)

positive_comments = (
    session.query(Comment.post_id,func.count("*").label("positive_comments"))
    .filter(Comment.sentiment == 'positive')
    .group_by(Comment.post_id)
    .subquery()
)

negative_comments = (
    session.query(Comment.post_id,func.count("*").label("negative_comments"))
    .filter(Comment.sentiment == 'negative')
    .group_by(Comment.post_id)
    .subquery()
)

final_query = (
    session.query(
        Post,
        comments.c.comments,
        positive_comments.c.positive_comments,
        negative_comments.c.negative_comments,
    )
    .outerjoin(comments, Post.id == comments.c.post_id)
    .outerjoin(positive_comments, Post.id == positive_comments.c.post_id)
    .outerjoin(negative_comments, Post.id == negative_comments.c.post_id)
)





comms = []
for post, comments, positive_comments, negative_comments in  final_query:
    comms.append(
        {
            "id": post.id,
            "body": post.body,
            "author_name": post.author_name,
            "created_on": str(post.created_on.date()),
            "comments": comments or 0,
            "positive_comments": positive_comments or 0,
            "negative_comments": negative_comments or 0,        
        }
    )

with open('forum.json','w') as f:
    json.dump(comms,f)
"""
items = []
for post, comments, negative_comments, positive_comments in final_query:
   items.append({
           "id": post.id,
           "body": post.body,
           "author_name": post.author_name,
           "created_on": str(post.created_on.date()),
           "comments": comments or 0,
           "positive_comments": positive_comments or 0,
           "negative_comments": negative_comments or 0,
       })

with open("forum_export.json", mode="w") as f:
   json.dump(items, f)
   """