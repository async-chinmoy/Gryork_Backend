from fastapi import FastAPI, HTTPException, Query
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import uvicorn

# Initialize FastAPI app
app = FastAPI(title="User Registration API")

# Setup MongoDB connection
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["Gryork"]
    feedbackCollection = db["Feedback"]
    # Verify connection
    client.admin.command('ping')
    print("Connected to MongoDB successfully!")
except ConnectionFailure:
    print("Failed to connect to MongoDB. Make sure MongoDB is running.")



@app.post("/feedback")
async def submit_feedback(
    NAME: str = Query(..., description="User's name"),
    EMAIL : str = Query(..., description="User's email address"),
    SUBJECT: str = Query(..., description="Feedback subject"),
    MESSAGE: str = Query(..., description="Feedback message")
):
    pass

# For local development
if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)