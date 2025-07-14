
from fastapi import FastAPI
from . import database, mqtt_client

app = FastAPI()

database.create_db_and_tables()

mqtt_client.client.loop_start()

@app.get("/")
def read_root():
    return {"message": "Aegis Hub is running"}
