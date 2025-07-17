from pydantic import BaseModel

class ContactCreate(BaseModel):
    name: str
    phone: str
    email: str
    message: str

class NewsletterCreate(BaseModel):
    email: str

class BlogCreate(BaseModel):
    title: str
    content: str

class CommentCreate(BaseModel):
    blog_id: int
    name: str
    content: str

class UserCreate(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
