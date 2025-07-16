import uvicorn
import sys
import os

# Add the project root to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from server import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
