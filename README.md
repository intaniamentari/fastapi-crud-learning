# FastAPI CRUD Project

This project is a simple CRUD implementation using **FastAPI**, **SQLAlchemy**, and **MySQL**.

## 📌 1. Create Virtual Environment

### Linux / Mac

```bash
python -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

## 📌 2. Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy pymysql python-dotenv
```

## 📌 3. Save Dependency List to `requirements.txt`

```bash
pip freeze > requirements.txt
```

## 📌 4. Run the Server

```bash
uvicorn app.main:app --reload
```

Access the application at:

```
http://127.0.0.1:8000
```

Swagger Documentation is available at:

```
http://127.0.0.1:8000/docs
```

## 📌 5. Project Structure (Example)

```
app/
 ├── main.py
 ├── config/
 │    └── database.py
 ├── models/
 ├── schemas/
 ├── services/
 ├── routes/
```

## 📌 6. Environment Variables

Create a `.env` file to store your environment settings:

```
DATABASE_URL=mysql+pymysql://root:password@localhost:3306/dbname
```

## 📌 7. Running Without a Virtual Environment

If you prefer to run directly without creating a venv:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```