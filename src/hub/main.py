from fastapi import FastAPI, HTTPException
from typing import List
from . import database as db
from .data_models import Device, NetworkLog, ChatMessage

app = FastAPI(
    title="Digital Guardian Hub",
    description="API for monitoring and interacting with the smart home environment.",
    version="1.0.0",
)

@app.on_event("startup")
def startup_event():
    """Initialize the database on application startup."""
    db.init_db()
    from . import mqtt_client
    mqtt_client.start_mqtt_client()

@app.on_event("shutdown")
def shutdown_event():
    """Close the database connection on application shutdown."""
    db.close_db_connection(None)

@app.get("/devices", response_model=List[Device], tags=["Devices"])
def list_devices():
    """Retrieve a list of all connected devices."""
    return db.get_all_devices()

@app.get("/network/logs", response_model=List[NetworkLog], tags=["Network"])
def get_network_logs(limit: int = 100):
    """Get the latest network traffic logs."""
    return db.get_network_logs(limit=limit)

@app.post("/chat", response_model=ChatMessage, tags=["Agent"])
def chat_with_agent(message: ChatMessage):
    """
    Send a message to the Digital Guardian agent and get a response.
    (This is a placeholder and will be integrated with the agent later)
    """
    # Placeholder logic
    if message.role == "user":
        # In a real implementation, this would call the agent's processing logic
        response_content = f"Agent received: '{message.content}'"
        return ChatMessage(role="agent", content=response_content)
    raise HTTPException(status_code=400, detail="Invalid message role")

@app.get("/health", tags=["System"])
def health_check():
    """Check the health of the API."""
    return {"status": "ok"}
