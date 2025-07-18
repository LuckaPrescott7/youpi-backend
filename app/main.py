from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from .database import Base, engine, SessionLocal
from .models import AdminUser
from .auth import hash_password, authenticate_user, create_token
from .routes import contact, newsletter, blog, comment
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Youpi. Backend")

Base.metadata.create_all(bind=engine)

app.include_router(contact.router)
app.include_router(newsletter.router)
app.include_router(blog.router)
app.include_router(comment.router)

@app.post("/register")
def register(email: str, password: str, db=Depends(SessionLocal)):
    if db.query(AdminUser).filter(AdminUser.email == email).first():
        raise HTTPException(status_code=400, detail="Email exists")
    hashed = hash_password(password)
    user = AdminUser(email=email, hashed_password=hashed)
    db.add(user)
    db.commit()
    return {"msg": "Admin créé"}

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db=Depends(SessionLocal)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401)
    token = create_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/")
def home():
    return {"msg": "Welcome to Youpi. API!"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # À restreindre à ton domaine frontend en production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)