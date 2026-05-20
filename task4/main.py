import sys
import os

from fastapi import FastAPI
from pydantic import BaseModel
from task4.agent import run_agent

# initialize fastapi app
app = FastAPI(
    title="Text-to-SQL Agent",
    description="An AI-powered agent that converts natural language questions to SQL and executes them",
    version="1.0.0"
)


# this defines what the input should look like
class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    """Home endpoint to check if API is running"""
    return {
        "message": "Text-to-SQL Agent is running!",
        "usage": "Send a POST request to /agent/sql with your question"
    }


@app.post("/agent/sql")
def sql_agent(request: QuestionRequest):
    """
    Main agent endpoint.
    Takes a natural language question and returns SQL result
    with a natural language summary.
    """
    result = run_agent(request.question)
    return result


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}