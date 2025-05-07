# SQL-Python
PostgreSQL 
# dept-crud-console

A simple Python console application for performing operations on a PostgreSQL `dept` table using the `psycopg` library.

## Features

- **Select**: View all departments or a specific department by ID
- **Insert**: Add a new department with a name and last updated date
- **Update**: Change the name or last updated date of an existing department
- **Delete**: Remove a department by its ID

## Prerequisites

- Python 3.8+
- PostgreSQL database with a table named `dept` in the `public` schema
- `psycopg` library installed

Install dependencies:
```bash
pip install psycopg[binary]
