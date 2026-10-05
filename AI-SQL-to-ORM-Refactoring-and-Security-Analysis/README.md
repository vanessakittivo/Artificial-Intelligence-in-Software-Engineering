# AI: SQL to ORM Refactoring and Security Analysis

This folder contains the starting procedural MySQL code and its SQLAlchemy ORM
refactor for the coursework task.

## Files

- `initial_code.py` — parameterized `mysql.connector` starting example.
- `refactored_code.py` — SQLAlchemy declarative `User` model and Create, Read,
  Update, and Delete functions, plus a simple runnable demonstration.
- `submission_draft.md` — prompt and reflection draft to transfer into the
  requested Google Doc.

## Run the ORM example

Create and activate a virtual environment in this folder, then install
`requirements.txt`. For example, in Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe refactored_code.py
```

The default database is SQLite; `DATABASE_URL` can be set to a MySQL connection
URL if MySQL is configured.

## Security notes

The starting code already uses parameterized queries for user-supplied values;
it does not build SQL by formatting those values into SQL strings. SQLAlchemy
ORM expressions also bind values safely by default. Neither approach makes all
database code automatically safe: review any raw SQL, avoid string-building
queries from untrusted input, keep credentials out of source control, and use
least-privilege database accounts.

The ORM model keeps table structure and common CRUD operations together in
Python. This can reduce repeated hand-written query mistakes and makes future
changes easier to find, while database-specific constraints and migrations
still need deliberate handling.

