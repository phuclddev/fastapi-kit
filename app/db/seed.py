from sqlalchemy.orm import Session

from . import models
from .database import engine
from .. import utils
from datetime import datetime, timedelta
import random

# def seed_data():
#     session = Session(bind=engine)
    
#     # Create some users
#     user1 = models.User(email="user1@gmail.com", password=utils.hash("pass"))
#     user2 = models.User(email="user2@gmail.com", password=utils.hash("pass"))
#     user3 = models.User(email="user3@gmail.com", password=utils.hash("pass"))
#     user4 = models.User(email="user4@gmail.com", password=utils.hash("pass"))
#     user5 = models.User(email="user5@gmail.com", password=utils.hash("pass"))
#     user6 = models.User(email="user6@gmail.com", password=utils.hash("pass"))
    
#     session.add(user1)
#     session.add(user2)
#     session.add(user3)
#     session.add(user4)
#     session.add(user5)
#     session.add(user6)
#     session.commit()

#     # Create some posts
#     post1 = models.Post(
#         title="Post 1",
#         content="Content for post 1",
#         owner_id=user1.id
#     )

#     post2 = models.Post(
#         title="Post 2",
#         content="Content for post 2",
#         owner_id=user1.id
#     )

#     post3 = models.Post(
#         title="Post 3",
#         content="Content for post 3",
#         owner_id=user2.id
#     )

#     post4 = models.Post(
#         title="Post 4",
#         content="Content for post 4",
#         owner_id=user2.id
#     )

#     post5 = models.Post(
#         title="Post 5",
#         content="Content for post 5",
#         owner_id=user3.id
#     )

#     post6 = models.Post(
#         title="Post 6",
#         content="Content for post 6",
#         owner_id=user3.id
#     )

#     post7 = models.Post(
#         title="Post 5",
#         content="Content for post 5",
#         owner_id=user4.id
#     )

#     post8 = models.Post(
#         title="Post 4",
#         content="Content for post 4",
#         owner_id=user4.id
#     )
    
#     session.add_all([post1, post2, post3, post4])
#     session.commit()

#     session.close()

def random_date(start, end):
    """Generate a random datetime between `start` and `end`."""
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

def seed_data():
    session = Session(bind=engine)
    
    # Create some users
    user1 = models.User(email="user1@gmail.com", password=utils.hash("pass"))
    user2 = models.User(email="user2@gmail.com", password=utils.hash("pass"))
    user3 = models.User(email="user3@gmail.com", password=utils.hash("pass"))
    user4 = models.User(email="user4@gmail.com", password=utils.hash("pass"))
    user5 = models.User(email="user5@gmail.com", password=utils.hash("pass"))
    user6 = models.User(email="user6@gmail.com", password=utils.hash("pass"))
    
    session.add(user1)
    session.add(user2)
    session.add(user3)
    session.add(user4)
    session.add(user5)
    session.add(user6)
    session.commit()

    # Define the time range for the random dates
    now = datetime.utcnow()
    two_weeks_ago = now - timedelta(weeks=2)

    # Create some posts with random created_at timestamps
    posts = [
        models.Post(title="Post 1", content="Content for post 1", owner_id=user1.id, created_at=random_date(two_weeks_ago, now)),
        models.Post(title="Post 2", content="Content for post 2", owner_id=user1.id, created_at=random_date(two_weeks_ago, now)),
        models.Post(title="Post 3", content="Content for post 3", owner_id=user2.id, created_at=random_date(two_weeks_ago, now)),
        models.Post(title="Post 4", content="Content for post 4", owner_id=user2.id, created_at=random_date(two_weeks_ago, now)),
        models.Post(title="Post 5", content="Content for post 5", owner_id=user3.id, created_at=random_date(two_weeks_ago, now)),
        models.Post(title="Post 6", content="Content for post 6", owner_id=user3.id, created_at=random_date(two_weeks_ago, now)),
        models.Post(title="Post 7", content="Content for post 7", owner_id=user4.id, created_at=random_date(two_weeks_ago, now)),
        models.Post(title="Post 8", content="Content for post 8", owner_id=user4.id, created_at=random_date(two_weeks_ago, now)),
        models.Post(title="Post 7", content="Content for post 9", owner_id=user5.id, created_at=random_date(two_weeks_ago, now)),
        models.Post(title="Post 8", content="Content for post 10", owner_id=user5.id, created_at=random_date(two_weeks_ago, now)),
        models.Post(title="Post 7", content="Content for post 11", owner_id=user6.id, created_at=random_date(two_weeks_ago, now)),
        models.Post(title="Post 8", content="Content for post 12", owner_id=user6.id, created_at=random_date(two_weeks_ago, now)),
    ]

    session.add_all(posts)
    session.commit()

    session.close()