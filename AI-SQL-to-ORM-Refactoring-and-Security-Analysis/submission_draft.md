# Vanessa_AI: SQL to ORM Refactoring and Security Analysis

## Prompt Formulation

Act as a Python developer and database security reviewer. Refactor the supplied
procedural Python/MySQL user-management code into a SQLAlchemy ORM example.
Define a declarative `User` model with `id`, `username`, `email`, and
`created_at` fields. Show how to configure an engine and ORM `Session`, create
the table, add a new user, and query that user. Also implement the original
Create, Read, Update, Delete, and list operations using the ORM. Use
configuration or environment variables for database credentials rather than
hard-coding a real password. After the code, explain in detail the security and
professional benefits and limitations of the ORM version compared with raw SQL
built by string formatting. Explain parameter binding accurately: parameterized
SQL is already safe for values, and ORM expressions bind values by default, but
unsafe raw SQL can still be vulnerable. Finally, explain how mapping Python
objects to tables can reduce repeated query mistakes and improve
maintainability. Keep the example beginner-friendly and compatible with
SQLAlchemy 2.x.

Starting code: use the contents of `initial_code.py` in this task folder.

## Execution Screenshot

**Add one genuine screenshot here after running the prompt in ChatGPT.** Make
sure it shows the complete ORM code and the complete security/professional
explanation. The screenshots previously supplied show parts of an answer, but
do not capture the complete response in one image, so they are not represented
here as a complete screenshot.

## Verification and Reflection

Reflection draft — revise this in your own words before submitting: With raw
SQL, the programmer has to keep table and column names, placeholders, query
text, and returned-row handling consistent in every function. When similar SQL
is repeated, a change to the data model can leave one query behind or introduce
a typo. An ORM gives the table a Python model and lets CRUD functions work with
instances of that model, so related structure and operations are easier to
locate and update together.

The ORM does not remove the need to understand SQL or review database code, but
it reduces some manual work and makes common changes more consistent. For
example, changing an object's email and committing the session is easier to
read than separately composing an UPDATE statement and interpreting affected
rows. In a larger application, shared models and query patterns can make code
easier for teammates to review. Schema migrations, transactions, constraints,
and security still need deliberate attention.

## GitHub Repository Update

**Add the link to the task folder in your AI coursework repository after the
folder is pushed.** The repository URL was not included with the task, so this
link remains to be filled in.

