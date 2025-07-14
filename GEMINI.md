## Project Status Update (July 8, 2025)

This `GEMINI.md` file has been cleaned to reflect the current state and future plans for the Raspberry Pi Edge Hub project.
To be started.

Project: The Digital Guardian


  Concept: A unified system that combines a data-ingestion hub with a conversational AI agent. It actively monitors smart home devices, network traffic, and system events, acting as a centralized firewall
  and intelligent guardian. Users can interact with it via a simple chat interface to query the home's status, investigate anomalies, and receive proactive alerts.

  ---

  Key Components & Workflow


   1. Data Ingestion (MQTT & Network Sniffing): IoT devices (sensors, cameras, smart plugs) publish their status and data to a local MQTT broker. A network monitoring service logs connections and traffic
      volume.
   2. Edge Hub (FastAPI + SQLite): A central FastAPI application running on the edge (Pi or NAS) subscribes to all data streams. It parses this information and stores it chronologically in a structured SQLite
      database (guardian.db).
   3. Guardian Agent (ADK): The Google ADK agent is the system's brain. It is equipped with a specific set of tools to query the guardian.db. Its core mission, defined in its system prompt, is to monitor for
      anomalies (e.g., a camera sending data to an unknown IP, a new device appearing on the network) and respond to user queries.
   4. User Interface (Web Dashboard): A simple, clean web UI provides a chat window to interact with the Guardian Agent and a dashboard to display real-time alerts and key metrics.

  ---

  Proposed Folder Structure

  This structure organizes the project into logical components: the data hub, the agent, shared modules, and deployment configurations.



    1 /digital-guardian/
    2 ├── .gitignore
    3 ├── docker-compose.yml         # Orchestrates all services (hub, agent, mqtt)
    4 ├── README.md                  # Project overview, setup, and API guide
    5 │
    6 ├── config/
    7 │   └── guardian_config.yaml   # Central config for database paths, MQTT topics, agent model
    8 │
    9 ├── data/                      # (Git ignored) For persistent data
   10 │   └── guardian.db            # SQLite database for all operational data
   11 │
   12 ├── docs/
   13 │   └── architecture.mmd       # Mermaid diagram of the system
   14 │
   15 ├── scripts/
   16 │   ├── start.sh               # Starts all services via docker-compose
   17 │   ├── stop.sh                # Stops all services
   18 │   └── simulate_device.py     # Python script to simulate IoT device traffic for testing
   19 │
   20 └── src/
   21     ├── agent/
   22     │   ├── __init__.py
   23     │   ├── run_agent.py       # Main entrypoint to initialize and run the ADK agent
   24     │   ├── system_prompt.txt  # Defines the agent's persona and mission as the "Digital Guardian"
   25     │   └── tools/
   26     │       ├── __init__.py
   27     │       ├── hub_tools.py   # Tools to query the hub's database (e.g., get_device_status, check_network_logs)
   28     │       └── analysis_tools.py # Tools for higher-level analysis (e.g., check_for_anomalies)
   29     │
   30     ├── hub/
   31     │   ├── __init__.py
   32     │   ├── main.py            # FastAPI application entrypoint (API endpoints)
   33     │   ├── database.py        # Manages SQLite connection, schema, and queries
   34     │   ├── mqtt_client.py     # Handles MQTT subscriptions and data ingestion logic
   35     │   └── data_models.py     # Pydantic models for API data structures
   36     │
   37     └── ui/
   38         ├── __init__.py
   39         ├── main.py            # Simple Flask or FastAPI to serve the static frontend
   40         └── static/
   41             ├── index.html
   42             ├── style.css
   43             └── app.js         # Handles WebSocket connection and chat interface logic