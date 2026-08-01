from sqlalchemy.orm import Session
from app.core.security import get_password_hash
from app.models.user import User
from app.schemas.user import UserCreate

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserCreate) -> User:
    db_user = User(
    email=user.email,
    phone=user.phone,
    password=get_password_hash(user.password),
    name=user.name,
    age=user.age,
    gender=user.gender,
    language_preference=user.language_preference,
    consent_agreed=user.consent_agreed,
)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user