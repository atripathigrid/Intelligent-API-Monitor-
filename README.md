# Intelligent API Monitor

Intelligent API Monitor is a scalable backend monitoring system built with Python and FastAPI that collects, stores, processes, and analyzes data from multiple external APIs such as weather, finance, and earthquake services.

The system is designed to help monitor incoming API data in real time, identify unusual patterns, detect anomalies, and generate alerts whenever abnormal conditions are found.

This project demonstrates strong backend engineering concepts including API integration, clean architecture, database management, anomaly detection, pagination, streaming responses, exporting large datasets, and REST API development.

---
## Clean Backend Architecture
The project follows a modular structure with separate layers for:

- Models
- Schemas
- CRUD operations
- Services
- Routes
- Database configuration

---

# Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Core programming language |
| FastAPI | Backend framework |
| SQLAlchemy | ORM for database operations |
| Pydantic | Data validation |
| SQLite / PostgreSQL | Database |
| Uvicorn | ASGI server |
| REST APIs | Communication layer |

---
# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/intelligent-api-monitor.git
cd intelligent-api-monitor
```

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

## 3. Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the root directory:

```env
DATABASE_URL=sqlite:///./monitor.db
SECRET_KEY=your_secret_key
DEBUG=True
```

For PostgreSQL:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/monitor_db
```

---

# Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The application will run on:

```bash
http://127.0.0.1:8000
```

Swagger documentation:

```bash
http://127.0.0.1:8000/docs
```

ReDoc documentation:

```bash
http://127.0.0.1:8000/redoc
```

---
# Learning Outcomes

This project helped in understanding:

- FastAPI application structure
- SQLAlchemy ORM
- Pydantic validation
- CRUD operations
- REST API development
- Streaming responses
- Exporting data
- Database relationships
- Clean architecture
- Error handling
- Backend scalability concepts

---

# Author

## Achintya Tripathi

Fullstack Developer | Python Enthusiast | FastAPI Learner

- Focused on backend development and API design
- Interested in scalable systems and data monitoring
- Passionate about learning clean architecture and modern backend technologies
