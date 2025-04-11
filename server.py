from fastapi import FastAPI, HTTPException, Query
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import uvicorn

from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request




# Initialize FastAPI app
app = FastAPI(title="User Registration API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your frontend domain like ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup MongoDB connection
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["Gryork"]
    contractor_feedbackCollection = db["Contractor"]
    worker_feedbackCollection = db["Worker"]
    other_feedbackCollection = db["Other"]

    # Verify connection
    client.admin.command('ping')
    print("Connected to MongoDB successfully!")
except ConnectionFailure:
    print("Failed to connect to MongoDB. Make sure MongoDB is running.")



@app.post("/feedback/contractor")
async def submit_feedback_contractor(
    request: Request
):
    data = await request.json()
    # print(data)
    feedback_data = {
        "NAME": data.get("NAME"),
        "COMPANY_NAME": data.get("COMPANY_NAME"),
        "CONTACT_INFO": data.get("CONTACT_INFO"),
        "FEEDBACK": data.get("FEEDBACK")
    }
    contractor_feedbackCollection.insert_one(feedback_data)
    return {"message": "Feedback submitted successfully!"}



@app.post("/feedback/worker")
async def submit_feedback_worker(
    request: Request
):
    data = await request.json()
    # print(data)
    feedback_data = {
        "NAME": data.get("NAME"),
        "COMPANY_NAME": data.get("COMPANY_NAME"),
        "CONTACT_INFO": data.get("CONTACT_INFO"),
        "FEEDBACK": data.get("FEEDBACK")
    }
    worker_feedbackCollection.insert_one(feedback_data)
    return {"message": "Feedback submitted successfully!"}



@app.post("/feedback/other")
async def submit_feedback_other(
    request: Request
):
    data = await request.json()
    # print(data)
    feedback_data = {
        "NAME": data.get("NAME"),
        "INFO_SOURCES": data.get("INFO_SOURCES"),
        "CONTACT_INFO": data.get("CONTACT_INFO"),
        "FEEDBACK": data.get("FEEDBACK")
    }

    if data.get("OTHER_SOURCE_SPECIFICATION"):
       feedback_data["OTHER_SOURCE_SPECIFICATION"] = data.get("OTHER_SOURCE_SPECIFICATION")

    other_feedbackCollection.insert_one(feedback_data)
    return {"message": "Feedback submitted successfully!"}





# For local development
if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)