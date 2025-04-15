from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from passlib.hash import bcrypt

app = FastAPI()
engine = create_engine("sqlite:///shop.db", connect_args={"check_same_thread": False})
Session = sessionmaker(bind=engine)
Base = declarative_base()

class U(Base):
    __tablename__ = "u"
    id = Column(Integer, primary_key=True)
    phone = Column(String)
    passw = Column(String)

class P(Base):
    __tablename__ = "p"
    id = Column(Integer, primary_key=True)
    n = Column(String)
    d = Column(String)
    c = Column(Float)

class O(Base):
    __tablename__ = "o"
    id = Column(Integer, primary_key=True)
    uid = Column(Integer, ForeignKey("u.id"))
    pid = Column(Integer, ForeignKey("p.id"))
    qty = Column(Integer)

Base.metadata.create_all(bind=engine)

@app.post("/signup")
def signup(phone: str, password: str):
    db = Session()
    user = db.query(U).filter(U.phone == phone).first()
    if user:
        raise HTTPException(status_code=400, detail="already")
    u = U(phone=phone, passw=bcrypt.hash(password))
    db.add(u)
    db.commit()
    return {"msg": "ok"}

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db = Session()
    u = db.query(U).filter(U.phone == form_data.username).first()
    if not u or not bcrypt.verify(form_data.password, u.passw):
        raise HTTPException(status_code=401, detail="bad")
    return {"msg": "welcome", "user_id": u.id}

@app.get("/prods")
def g(lim: int, off: int):
    db = Session()
    return db.query(P).offset(off).limit(lim).all()

@app.post("/add")
def a(n: str, d: str, c: float):
    db = Session()
    p = P(n=n, d=d, c=c)
    db.add(p)
    db.commit()
    return {"msg": "added"}

@app.post("/buy")
def b(u: int, p: int, q: int):
    db = Session()
    o = O(uid=u, pid=p, qty=q)
    db.add(o)
    db.commit()
    return {"msg": "bought"}

@app.get("/orders")
def o(uid: int, lim: int, off: int):
    db = Session()
    return db.query(O).filter(O.uid == uid).offset(off).limit(lim).all()
