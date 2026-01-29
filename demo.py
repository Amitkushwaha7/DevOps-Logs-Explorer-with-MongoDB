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