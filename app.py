from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session
from datetime import datetime, date
import os

# Database setup
DATABASE_URL = "sqlite:///./finance_dashboard.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Models
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    transactions = relationship("Transaction", back_populates="user")
    goals = relationship("Goal", back_populates="user")
    insights = relationship("Insight", back_populates="user")

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Float)
    category = Column(String)
    date = Column(Date)
    description = Column(String)
    user = relationship("User", back_populates="transactions")

class Goal(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String)
    target_amount = Column(Float)
    current_amount = Column(Float)
    due_date = Column(Date)
    user = relationship("User", back_populates="goals")

class Insight(Base):
    __tablename__ = "insights"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    content = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship("User", back_populates="insights")

# Create tables
Base.metadata.create_all(bind=engine)

# Seed data
def seed_data(db: Session):
    if not db.query(User).first():
        user = User(name="John Doe", email="john@example.com", password_hash="hashed_password")
        db.add(user)
        db.commit()
        db.refresh(user)

        transaction = Transaction(user_id=user.id, amount=100.0, category="Groceries", date=date.today(), description="Weekly groceries")
        db.add(transaction)

        goal = Goal(user_id=user.id, title="Save for Vacation", target_amount=2000.0, current_amount=150.0, due_date=date(2024, 12, 31))
        db.add(goal)

        insight = Insight(user_id=user.id, content="Consider reducing dining out expenses to save more.")
        db.add(insight)

        db.commit()

# FastAPI app setup
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# Dependency
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
async def startup_event():
    db = SessionLocal()
    seed_data(db)
    db.close()

@app.get("/", response_class=HTMLResponse)
async def read_dashboard():
    with open("templates/dashboard.html") as f:
        return f.read()

@app.get("/transactions", response_class=HTMLResponse)
async def read_transactions():
    with open("templates/transactions.html") as f:
        return f.read()

@app.get("/goals", response_class=HTMLResponse)
async def read_goals():
    with open("templates/goals.html") as f:
        return f.read()

@app.get("/profile", response_class=HTMLResponse)
async def read_profile():
    with open("templates/profile.html") as f:
        return f.read()

@app.get("/insights", response_class=HTMLResponse)
async def read_insights():
    with open("templates/insights.html") as f:
        return f.read()

@app.get("/api/users/{user_id}")
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/api/transactions")
async def get_transactions(db: Session = Depends(get_db)):
    transactions = db.query(Transaction).all()
    return transactions

@app.post("/api/transactions")
async def create_transaction(transaction: Transaction, db: Session = Depends(get_db)):
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction

@app.get("/api/goals")
async def get_goals(db: Session = Depends(get_db)):
    goals = db.query(Goal).all()
    return goals

@app.post("/api/goals")
async def create_goal(goal: Goal, db: Session = Depends(get_db)):
    db.add(goal)
    db.commit()
    db.refresh(goal)
    return goal
