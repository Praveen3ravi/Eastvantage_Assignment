from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import sqlite3
import uvicorn

app = FastAPI()

# Global variables:
DATABASE_URL = "sqlite:///./?.db" #driver_url / path
conn = sqlite3.connect('example.db')
cursor = conn.cursor()


class Address(BaseModel):
    latitude: float
    longitude: float
    street: str
    city: str
    state: str
    postal_code: str



@app.post("/addresses/", response_model=Address)
def create_address(address: Address):
    cursor.execute(f'''CREATE TABLE IF NOT EXIST '{address}'(
                   address_id INTEGER PRIMARY KEY,
                   latitude Float,
                   longitude Float,
                   street TEXT NOT NULL,
                   city TEXT NOT NULL,
                   state TEXT NOT NULL,
                   postal_code TEXT NOT NULL);
    ''')
        

@app.put("/addresses/{address_id}", response_model=Address)
def update_address(address_id: int, address: Address):
    cursor.execute(f'''UPDATE {address}
                        SET address_id = {address_id};''')

@app.delete("/addresses/{address_id}")
def delete_address(address_id: int):
    cursor.execute(f'''DELETE FROM Address
                WHERE address_id = {address_id};''')

@app.get("/addresses/")
def get_addresses(latitude: float, longitude: float, distance: float):
    cursor.execute(F'''SELECT * FROM Address 
                   WHERE
                   latitude = {latitude}
                   AND
                   longitude = {longitude}
                   AND
                   distance = {distance};
                   ''')

# TO RUN THE CODE:
    # cmd---> "uvicorn Praveen_Ravi:app --reload"
    # Open the localhost swagger.
    # You can find 4 endpoints.
    # Each endpoint as its own operation.
    # Run it accordingly.
    # Thanks! 