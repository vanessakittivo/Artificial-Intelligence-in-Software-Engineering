"""A small SQLAlchemy ORM example for the database learning lesson.

By default this uses SQLite so it can be tried without a MySQL server. Set
DATABASE_URL to use MySQL, for example:
mysql+mysqlconnector://root:password@localhost/example_db
"""

import os

from sqlalchemy import Column, DateTime, Integer, String, create_engine, func
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///example_db.sqlite3")

# SQLite needs this option when a connection is used from a different thread.
engine_options = {"echo": False}
if DATABASE_URL.startswith("sqlite"):
    engine_options["connect_args"] = {"check_same_thread": False}

engine = create_engine(DATABASE_URL, **engine_options)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class User(Base):
    """Python representation of one row in the users table."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    created_at = Column(DateTime, server_default=func.current_timestamp())

    def __repr__(self):
        return (
            f"User(id={self.id!r}, username={self.username!r}, "
            f"email={self.email!r}, created_at={self.created_at!r})"
        )


def create_user(session, username, email):
    """Add a user and return it after the transaction is saved."""
    if not username or not email:
        raise ValueError("Username and email are required.")

    user = User(username=username, email=email)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def get_user_by_username(session, username):
    """Return the first user with this username, or None."""
    return session.query(User).filter_by(username=username).first()


def update_user_email(session, username, new_email):
    """Update the first matching user's email; return that user or None."""
    user = get_user_by_username(session, username)
    if user is None:
        return None
    user.email = new_email
    session.commit()
    return user


def delete_user(session, username):
    """Delete the first matching user; return True if one was found."""
    user = get_user_by_username(session, username)
    if user is None:
        return False
    session.delete(user)
    session.commit()
    return True


def list_users(session, limit=5):
    """Return the newest users first."""
    return (
        session.query(User)
        .order_by(User.created_at.desc(), User.id.desc())
        .limit(limit)
        .all()
    )


def main():
    # Creates missing tables; it does not change an existing table's schema.
    Base.metadata.create_all(engine)

    # A context manager closes the session even if an error occurs.
    with SessionLocal() as session:
        try:
            username = input("Username to add: ").strip()
            email = input("Email to add: ").strip()
            created = create_user(session, username, email)
            print("Created:", created)

            found = get_user_by_username(session, username)
            print("Looked up:", found)

            print("\nLatest users:")
            for user in list_users(session):
                print(user)
        except Exception:
            session.rollback()
            raise


if __name__ == "__main__":
    main()

