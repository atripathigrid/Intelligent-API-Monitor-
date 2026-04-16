# 🤖 Intelligent API Monitor

A scalable backend system built using **FastAPI** to collect, process, and analyze data from multiple external APIs such as weather, finance, and earthquake services.  

The application focuses on **real-time monitoring, anomaly detection, and alert generation**, helping identify unusual patterns in incoming API data.

---

# 🚀 Features

### 🌐 Multi-API Integration
- Collects data from multiple external APIs (Weather, Finance, Earthquake)
- Unified data handling and storage

### 📡 Real-time Data Processing
- Continuously processes incoming API responses
- Efficient handling of large datasets

### 🚨 Anomaly Detection System
- Identifies abnormal patterns in incoming data
- Generates alerts for unusual conditions

### 📊 Data Streaming & Export
- Streaming API responses for large datasets
- Export functionality for bulk data analysis

### 📄 Pagination Support
- Efficient handling of large database queries
- Optimized API responses with pagination

### 🏗️ Clean Backend Architecture
- Modular structure with:
  - Models
  - Schemas
  - CRUD
  - Services
  - Routes
  - Database layer

---

# 🛠️ Tech Stack

| Component            | Technology            |
|---------------------|----------------------|
| Backend             | Python, FastAPI      |
| Database            | SQLite / PostgreSQL  |
| ORM                 | SQLAlchemy           |
| Validation          | Pydantic             |
| Server              | Uvicorn              |
| API Style           | REST APIs            |

---
# 📁 Project Structure

- **app/main.py** → Entry point of the FastAPI application  
- **models/** → Defines database tables and structure  
- **schemas/** → Handles request/response validation using Pydantic  
- **crud/** → Performs database operations (CRUD)  
- **services/** → Contains business logic and API integrations  
- **routes/** → Defines API endpoints  
- **database/** → Manages database connection and sessions  
- **dashboard/** → Interactive dashboard built with Streamlit  
- **tests/** → Includes 12 test cases for validation and reliability  
---
# ⚙️ Installation & Usage

## 1. 📥 Clone the Repository

```bash
git clone https://github.com/your-username/intelligent-api-monitor.git
cd intelligent-api-monitor
```

## 2. 🧪 Create Virtual Environment

```bash
python -m venv venv
```

## 3. ▶️ Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

## 4. 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Configuration

📝 Create .env file in the root directory:

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

# ▶️ Running the Application

🚀 Start FastAPI Server

```bash
uvicorn app.main:app --reload
```

The application will run on:

```bash
http://127.0.0.1:8000
```

📄 Swagger Documentation

```bash
http://127.0.0.1:8000/docs
```

📘 ReDoc Documentation

```bash
http://127.0.0.1:8000/redoc
```

---
# 📊 System Design & Logic

- **🔄 Data Flow** → External APIs → Services → Database → Routes → Dashboard  
- **🧠 Data Validation** → Handled using Pydantic schemas  
- **🗄️ Data Storage** → Managed using SQLAlchemy ORM  
- **🚨 Anomaly Detection** → Identifies unusual patterns in API data  
- **📡 API Layer** → Exposes processed data via REST endpoints  
- **📊 Dashboard** → Visualizes data using Streamlit  
- **📦 Data Handling** → Supports streaming, pagination, and export  

---

# 👨‍💻 Internship Project Details

- **📌 Project Number** → 02  
- **💼 Role** → Backend Development & Dashboard Integration  
- **🎯 Focus** → API integration, scalable architecture, real-time monitoring  

---

