from pydantic import BaseModel, Field
from typing import Optional, List

class Device(BaseModel):
    """Pydantic model for a device connected to the network."""
    id: str = Field(..., description="Unique device identifier (e.g., MAC address)")
    name: str = Field(..., description="User-friendly name of the device")
    ip_address: str = Field(..., description="Current IP address")
    status: str = Field(default="online", description="Device status (e.g., online, offline)")

class NetworkLog(BaseModel):
    """Pydantic model for a network traffic log entry."""
    timestamp: str = Field(..., description="Timestamp of the network activity")
    source_ip: str = Field(..., description="Source IP address")
    destination_ip: str = Field(..., description="Destination IP address")
    protocol: str = Field(..., description="Protocol used (e.g., TCP, UDP)")
    port: int = Field(..., description="Destination port")

class SystemEvent(BaseModel):
    """Pydantic model for a system-level event."""
    timestamp: str = Field(..., description="Timestamp of the event")
    service: str = Field(..., description="Name of the service or application")
    event_type: str = Field(..., description="Type of event (e.g., start, stop, error)")
    message: str = Field(..., description="Event message or description")

class ChatMessage(BaseModel):
    """Pydantic model for a chat message."""
    role: str = Field(..., description="Role of the sender (user or agent)")
    content: str = Field(..., description="Content of the message")
