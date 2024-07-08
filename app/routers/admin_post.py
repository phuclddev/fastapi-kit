from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional

from sqlalchemy import func

from ..services import oauth2

from ..db import models, crud
from .. import schemas
from ..db.database import get_db
from datetime import datetime, timedelta

router = APIRouter(
    prefix="/admin/api/posts",
    tags=['Admin Posts']
)

Post = models.Post
post = crud.CRUDBase[Post, schemas.PostCreate, schemas.PostUpdate](Post)

@router.post("/", response_model=schemas.Post)
def create_Post(
    *,
    db: Session = Depends(get_db),
    Post_in: schemas.PostCreate,
    current_user: models.User = Depends(oauth2.require_permission("create_post"))
):
    return post.create(db=db, obj_in=Post_in)

@router.get("/", response_model=List[schemas.Post])
def read_Posts(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 10,
    current_user: models.User = Depends(oauth2.require_permission("read_post"))
):
    Posts = post.get_multi(db=db, skip=skip, limit=limit)
    return Posts

@router.get("/{id}", response_model=schemas.Post)
def read_Post(
    *,
    db: Session = Depends(get_db),
    id: int,
    current_user: models.User = Depends(oauth2.require_permission("read_post"))
):
    Post = post.get(db=db, id=id)
    if not Post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return Post

@router.put("/{id}", response_model=schemas.Post)
def update_Post(
    *,
    db: Session = Depends(get_db),
    id: int,
    Post_in: schemas.PostUpdate,
    current_user: models.User = Depends(oauth2.require_permission("update_post"))
):
    Post = post.get(db=db, id=id)
    if not Post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    Post = Post.update(db=db, db_obj=Post, obj_in=Post_in)
    return Post

@router.delete("/{id}", response_model=schemas.Post)
def delete_Post(
    *,
    db: Session = Depends(get_db),
    id: int,
    current_user: models.User = Depends(oauth2.require_permission("delete_post"))
):
    Post = post.remove(db=db, id=id)
    return Post