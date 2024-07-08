from sqlalchemy.orm import Session

from . import models
from .database import engine
from .. import utils
from datetime import datetime, timedelta
import random


def random_date(start, end):
    """Generate a random datetime between `start` and `end`."""
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

def seed_data():
    session = Session(bind=engine)

    # Create permissions
    create_post = models.Permission(name="create_post")
    edit_post = models.Permission(name="edit_post")
    delete_post = models.Permission(name="delete_post")
    view_post = models.Permission(name="view_post")

    session.add_all([create_post, edit_post, delete_post, view_post])
    session.commit()

    # Create roles and assign permissions
    admin_role = models.Role(name="admin", permissions=[create_post, edit_post, delete_post, view_post])
    editor_role = models.Role(name="editor", permissions=[create_post, edit_post, view_post])
    viewer_role = models.Role(name="viewer", permissions=[view_post])

    session.add_all([admin_role, editor_role, viewer_role])
    session.commit()
    
    # Create some users
    user1 = models.User(email="admin@gmail.com", password=utils.hash("pass"), roles=[admin_role])
    user2 = models.User(email="editor@gmail.com", password=utils.hash("pass"), roles=[editor_role])
    user3 = models.User(email="viewer@gmail.com", password=utils.hash("pass"), roles=[viewer_role])
    user4 = models.User(email="user4@gmail.com", password=utils.hash("pass"), roles=[viewer_role])
    user5 = models.User(email="user5@gmail.com", password=utils.hash("pass"), roles=[viewer_role])
    user6 = models.User(email="user6@gmail.com", password=utils.hash("pass"), roles=[viewer_role])
    
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