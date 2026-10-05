"""Starting procedural version for the SQL-to-ORM refactoring activity."""

import mysql.connector
from mysql.connector import Error


def get_connection():
    """Open a connection to the example database."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword",  # Replace locally; never commit a real secret.
        database="example_db",
    )


def create_user(db_cursor, username, email):
    """Create a user using a parameterized SQL statement."""
    if not username or not email:
        print("Username and email are required.")
        return
    sql = "INSERT INTO users (username, email) VALUES (%s, %s)"
    try:
        db_cursor.execute(sql, (username, email))
        print(f"User '{username}' created successfully.")
    except Error as error:
        print(f"Error creating user: {error}")


def get_user_by_username(db_cursor, username):
    sql = "SELECT id, username, email, created_at FROM users WHERE username = %s"
    db_cursor.execute(sql, (username,))
    return db_cursor.fetchone()


def update_user_email(db_cursor, username, new_email):
    sql = "UPDATE users SET email = %s WHERE username = %s"
    db_cursor.execute(sql, (new_email, username))
    return db_cursor.rowcount > 0


def delete_user(db_cursor, username):
    sql = "DELETE FROM users WHERE username = %s"
    db_cursor.execute(sql, (username,))
    return db_cursor.rowcount > 0


def list_users(db_cursor, limit=5):
    sql = (
        "SELECT id, username, email, created_at FROM users "
        "ORDER BY created_at DESC LIMIT %s"
    )
    db_cursor.execute(sql, (limit,))
    return db_cursor.fetchall()

