import os
import sys
from pathlib import Path

# Simulation of Vercel environment
os.environ["RUNNING_ON_VERCEL"] = "true"

# Add current dir to path
sys.path.insert(0, str(Path(__file__).parent))

from main import app, CERT_DIR, CONFIG_FILE, IS_VERCEL

print(f"IS_VERCEL: {IS_VERCEL}")
print(f"CERT_DIR: {CERT_DIR}")
print(f"CONFIG_FILE: {CONFIG_FILE}")

# Test Scan route
with app.test_client() as client:
    response = client.post('/scan/fast')
    data = response.get_json()
    print(f"Scan Fast Response: {data}")
    
    if data.get("is_vercel") and not data.get("ok"):
        print("SUCCESS: Scan disabled on Vercel as expected.")
    else:
        print("FAILURE: Scan not properly disabled on Vercel.")

# Check if CERT_DIR is indeed /tmp
if CERT_DIR == "/tmp":
    print("SUCCESS: CERT_DIR correctly points to /tmp")
else:
    print(f"FAILURE: CERT_DIR is {CERT_DIR}, expected /tmp")
