# DevOps Logs Explorer with MongoDB

> A real-time logging simulation and exploration system that demonstrates how DevOps teams can centralize and analyze application logs using MongoDB.

## Table of Contents

- [What This App Does](#-what-this-app-does)
- [Architecture](#-architecture)
- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Installation & Setup](#-installation--setup)
- [Running the Application](#-running-the-application)
- [Viewing Logs in MongoDB Compass](#-viewing-logs-in-mongodb-compass)
- [Example Queries](#-example-queries)
- [Project Structure](#-project-structure)
- [Technologies Used](#-technologies-used)
- [Use Cases](#-use-cases)
- [Troubleshooting](#-troubleshooting)

---

## What This App Does

This application simulates a real-world microservices environment where multiple services generate logs continuously. It demonstrates:

- **Simulates a running service** with multiple microservices
- **Generates random logs every few seconds** with different severity levels
- **Pushes logs into MongoDB** for centralized storage
- **Enables real-time log monitoring and analysis** using MongoDB Compass
- **Feels like real-time application logging** in production environments

Perfect for learning DevOps monitoring, centralized logging, and NoSQL database operations!

---

## Architecture

The system follows a simple yet effective pipeline for log collection and analysis:

![Architecture Diagram](assets/architecture-diagram.png)

### Data Flow:
1. **Microservices** (`auth-service`, `payment-service`, `order-service`) generate logs
2. **Python Log Producer** (`demo.py`) simulates log generation every 2 seconds
3. **PyMongo Driver** handles communication with MongoDB
4. **MongoDB Database** stores all logs in the `devops_logs` database
5. **MongoDB Compass** provides real-time monitoring and query capabilities

---

## Features

- **Continuous Log Generation**: Simulates real-time logging from multiple services
- **Multi-Service Support**: Logs from `auth-service`, `payment-service`, and `order-service`
- **Multiple Log Levels**: INFO, WARN, and ERROR levels for different severity
- **Multi-Host Simulation**: Distributed across `server-1`, `server-2`, and `server-3`
- **Real-time Monitoring**: Watch logs appear live in MongoDB Compass
- **Powerful Querying**: Filter logs by service, level, timestamp, or host
- **NoSQL Storage**: Flexible document-based log storage in MongoDB
- **Timestamp Tracking**: Every log entry includes UTC timestamp

---

## Prerequisites

Before you begin, ensure you have the following installed:

### Required Software:
- **Python 3.7+** - [Download here](https://www.python.org/downloads/)
- **MongoDB Community Server** - [Download here](https://www.mongodb.com/try/download/community)
- **MongoDB Compass** (Optional but recommended) - [Download here](https://www.mongodb.com/try/download/compass)

### Verify Installations:
```bash
# Check Python version
python --version

# Check if MongoDB is running
mongod --version
```

---

## Installation & Setup

Follow these steps to set up the project from scratch:

### Step 1: Create Project Directory

```bash
mkdir devops_logs_explorer
cd devops_logs_explorer
```

![Directory Creation](assets/06-directory-creation-commands.png)

### Step 2: Set Up Python Virtual Environment

Create and activate a virtual environment to isolate dependencies:

```bash
# Create virtual environment
python3 -m venv .venv
```

![Virtual Environment Creation](assets/04-python-venv-creation.png)

```bash
# Activate virtual environment
# On Windows:
.venv\Scripts\activate

# On macOS/Linux:
source .venv/bin/activate
```

![Virtual Environment Activation](assets/05-python-venv-activation.png)

### Step 3: Install Dependencies

Install PyMongo, the official MongoDB Python driver:

```bash
pip install pymongo
```

![PyMongo Installation](assets/07-pymongo-installation.png)

### Step 4: Create the Log Producer Script

Create a file named `demo.py` with the following code:

```python
import time
import random
from datetime import datetime
from pymongo import MongoClient

# 1. Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["devops_logs"]
logs_collection = db["logs"]

services = ["auth-service", "payment-service", "order-service"]
levels = ["INFO", "WARN", "ERROR"]

# 2. Keep generating logs
while True:
    log = {
        "service": random.choice(services),
        "level": random.choice(levels),
        "message": "Dummy log message",
        "timestamp": datetime.utcnow(),
        "host": f"server-{random.randint(1,3)}"
    }

    logs_collection.insert_one(log)
    print("Inserted log:", log)

    time.sleep(2)  # wait 2 seconds
```

![Python Demo Script](assets/08-python-demo-script.png)

### Step 5: Start MongoDB Server

Ensure MongoDB is running on your system:

```bash
# On Windows (if MongoDB is installed as a service):
net start MongoDB

# On macOS/Linux:
sudo systemctl start mongod
# or
mongod --dbpath /path/to/data/directory
```

---

## Running the Application

### Step 1: Execute the Log Producer

Start generating logs by running the Python script:

```bash
python demo.py
```

![Script Execution Output](assets/13-python-script-execution-output.png)

You'll see logs printing continuously in the terminal:

```
Inserted log: {'service': 'auth-service', 'level': 'ERROR', 'message': 'Dummy log message', 'timestamp': datetime.datetime(2026, 1, 29, 13, 47, 53), 'host': 'server-1', '_id': ObjectId('...')}
Inserted log: {'service': 'payment-service', 'level': 'INFO', 'message': 'Dummy log message', 'timestamp': datetime.datetime(2026, 1, 29, 13, 47, 55), 'host': 'server-2', '_id': ObjectId('...')}
```

### Step 2: The Script Will:
- [√] Connect to MongoDB at `localhost:27017`
- [√] Create a database named `devops_logs`
- [√] Create a collection named `logs`
- [√] Insert a new log document every 2 seconds
- [√] Continue running until you stop it (Ctrl+C)

---

## Viewing Logs in MongoDB Compass

MongoDB Compass provides a visual interface to explore your logs in real-time.

### Step 1: Connect to MongoDB

Open MongoDB Compass and connect to:
```
mongodb://localhost:27017
```

### Step 2: Select Database

Navigate to the `devops_logs` database:

![MongoDB Database Selection](assets/01-mongodb-database-selection.png)

### Step 3: View the Logs Collection

Click on the `logs` collection to see all stored logs:

![MongoDB Collection Creation](assets/02-mongodb-collection-creation.png)

### Step 4: Real-time Monitoring

Click the **Refresh** button to see new logs appear in real-time:

![MongoDB Compass Logs View](assets/03-mongodb-compass-logs-view.png)

As your Python script continues running, you'll see the log count increasing:

![Multiple Logs in MongoDB Compass](assets/09-mongodb-compass-multiple-logs.png)

---

## Example Queries

MongoDB provides powerful querying capabilities. Try these queries while the app is running!

### Query 1: Filter by Log Level - INFO

Find all INFO level logs:

```javascript
db.logs.find({ level: "INFO" })
```

![MongoDB Query INFO Filter](assets/10-mongodb-query-info-filter.png)

### Query 2: Filter by Log Level - ERROR

Find all ERROR level logs for debugging:

```javascript
db.logs.find({ level: "ERROR" })
```

![MongoDB Query ERROR Filter](assets/11-mongodb-query-error-filter.png)

### Query 3: Filter by Service

Find logs from a specific service:

```javascript
db.logs.find({ service: "payment-service" })
```

### Query 4: Sort by Timestamp

Get the most recent logs first:

```javascript
db.logs.find().sort({ timestamp: -1 })
```

### Query 5: Complex Query

Find ERROR logs from payment-service:

```javascript
db.logs.find({ 
  service: "payment-service", 
  level: "ERROR" 
})
```

### Query 6: Count Logs by Level

```javascript
db.logs.aggregate([
  { $group: { _id: "$level", count: { $sum: 1 } } }
])
```

![MongoDB Query Operations](assets/12-mongodb-query-operations.png)

---

## Project Structure

```
devops_logs_explorer/
├── .venv/                          # Python virtual environment
├── assets/                         # Screenshots and diagrams
│   ├── architecture-diagram.png
│   └── [13 workflow screenshots]
├── logs/                           # Log directory (optional)
├── demo.py                         # Main log producer script
├── DEMO.md                         # Detailed tutorial (this file)
└── README.md                       # Project overview
```

---

## Technologies Used

| Technology | Purpose | Documentation |
|------------|---------|---------------|
| **Python 3** | Application logic and log generation | [python.org](https://www.python.org/) |
| **PyMongo** | MongoDB driver for Python | [pymongo.readthedocs.io](https://pymongo.readthedocs.io/) |
| **MongoDB** | NoSQL database for log storage | [mongodb.com](https://www.mongodb.com/) |
| **MongoDB Compass** | GUI for database visualization | [MongoDB Compass Docs](https://www.mongodb.com/products/compass) |

### Log Document Structure:
```json
{
  "_id": ObjectId("..."),
  "service": "auth-service",
  "level": "ERROR",
  "message": "Dummy log message",
  "timestamp": ISODate("2026-01-29T13:47:53.000Z"),
  "host": "server-1"
}
```

---

## Use Cases

This project is perfect for:

- **Learning MongoDB** - Hands-on experience with NoSQL databases
- **Understanding Microservices Logging** - See how distributed systems generate logs
- **DevOps Training** - Practice centralized log management
- **Database Querying** - Learn MongoDB query language (MQL)
- **Real-time Data Ingestion** - Simulate continuous data streaming
- **Monitoring & Debugging** - Practice filtering and analyzing logs
- **Portfolio Projects** - Demonstrate DevOps and database skills

---

## Troubleshooting

### Issue 1: MongoDB Connection Error
**Error:** `ConnectionFailure: [Errno 111] Connection refused`

**Solution:**
- Ensure MongoDB server is running: `mongod --version`
- Check if MongoDB is listening on port 27017
- Start MongoDB service: `sudo systemctl start mongod` (Linux) or `net start MongoDB` (Windows)

### Issue 2: PyMongo Not Found
**Error:** `ModuleNotFoundError: No module named 'pymongo'`

**Solution:**
- Activate virtual environment: `source .venv/bin/activate`
- Reinstall PyMongo: `pip install pymongo`

### Issue 3: Permission Denied
**Error:** `PermissionError: [Errno 13] Permission denied`

**Solution:**
- Run MongoDB with proper permissions
- Check MongoDB data directory permissions
- Use `sudo` if necessary (Linux/macOS)

### Issue 4: Port Already in Use
**Error:** `Address already in use`

**Solution:**
- Check if another MongoDB instance is running
- Stop existing MongoDB: `sudo systemctl stop mongod`
- Change port in `demo.py`: `MongoClient("mongodb://localhost:27018")`

---

## Next Steps & Enhancements

Want to take this project further? Consider these improvements:

- [+] Add authentication and user management
- [+] Implement email alerts for ERROR logs
- [+] Create a web dashboard using Flask/Django
- [+] Dockerize the application
- [+] Deploy MongoDB to MongoDB Atlas (cloud)
- [+] Add Slack/Discord notifications for critical errors
- [+] Implement log aggregation and analytics
- [+] Add log archiving and rotation
- [+] Create data visualizations with charts
- [+] Use MongoDB Change Streams for real-time updates

---

## Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


---

**Happy Logging!**
