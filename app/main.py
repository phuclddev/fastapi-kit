from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .db import models
from .db.database import engine
from .routers import post, user, auth, vote, admin_post
from .config import settings
from .db.seed import seed_data
import aiofiles
import os
from fastapi.staticfiles import StaticFiles

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include user routers
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

# Include admin routers
app.include_router(admin_post.router)

@app.get("/seed")
def root():
    seed_data()
    return {"message": "Hello World pushing out to ubuntu"}

UPLOAD_DIR = "uploads"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)
ALLOWED_IMAGE_TYPES = ["image/jpeg", "image/png", "image/gif"]

@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_IMAGE_TYPES:
        raise HTTPException(status_code=400, detail="Invalid file type. Only JPEG, PNG, and GIF files are allowed.")

    file_location = os.path.join(UPLOAD_DIR, file.filename)
    async with aiofiles.open(file_location, 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)
    return {"filename": file.filename, "location": file_location}

# Add static files route
app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")