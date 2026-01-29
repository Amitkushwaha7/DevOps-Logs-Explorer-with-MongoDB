# DevOps Logs Explorer with MongoDB

Built a DevOps Logs Explorer that simulates real-time application logging, ingests logs into MongoDB, and enables centralized log analysis for debugging and monitoring.

![Architecture Diagram](assets/architecture-diagram.png)

## What This App Does?

- Simulates a running service
- Generates random logs every few seconds
- Pushes them into MongoDB
- Feels like real-time application logging

---

### Step 1: Install Dependency

`pip install pymongo`

We use PyMongo, MongoDB's official Python driver.

### Step 2: Dummy Python Log Producer App

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

### Step 3: Run the App

`python demo.py`

You'll see logs printing continuously:

```
Inserted log: {'service': 'auth-service', 'level': 'ERROR', ...}
```

### Step 4: View Logs Live in MongoDB Compass

- Open MongoDB Compass
- Go to `devops_logs` → `logs`
- Click Refresh
- Watch logs appear in real time

![MongoDB Compass Logs View](assets/03-mongodb-compass-logs-view.png)

---

## Example Queries (Try While App Is Running)

```javascript
// Find all ERROR logs
db.logs.find({ level: "ERROR" })

// Find logs from payment-service
db.logs.find({ service: "payment-service" })

// Get most recent logs first
db.logs.find().sort({ timestamp: -1 })
```

---

## Screenshots

<table>
  <tr>
    <td><img src="assets/09-mongodb-compass-multiple-logs.png" width="400"/></td>
    <td><img src="assets/10-mongodb-query-info-filter.png" width="400"/></td>
  </tr>
  <tr>
    <td align="center"><b>Multiple Logs in MongoDB</b></td>
    <td align="center"><b>Query Filtering - INFO Logs</b></td>
  </tr>
</table>

---

## Detailed Documentation

For complete setup instructions, troubleshooting, and advanced queries, see **[DEMO.md](DEMO.md)**

---

**Happy Logging!**
