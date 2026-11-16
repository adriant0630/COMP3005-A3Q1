# COMP3005-A3Q1

## Description
A Python application that connects to PostgreSQL and performs CRUD operations.

## Setup

```bash
### 1. Clone Repository
git clone https://github.com/adriant0630/COMP3005-A3Q1.git
cd COMP3005-A3Q1

### 2. Install Dependencies
pip install -r requirements.txt
```

## Creating the PostgreSQL Database
Using pgAdmin create a database using the command:
```sql
CREATE DATABASE "<Database Name>";
```

## Run

### 3. Edit Database Connection Parameters
In src/main.py edit dbname, user, password, host, and port to connect your PostgreSQL database

### 4. Run in Terminal
Open a terminal in the project directory and run:
```bash
python src\main.py
```