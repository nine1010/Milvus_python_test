import os
from pymilvus import connections
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

MILVUS_HOST = os.getenv("MILVUS_HOST")
MILVUS_PORT = os.getenv("MILVUS_PORT")
# print(MILVUS_HOST)
# print(MILVUS_PORT)

def open_connection(alias="default"):
    """
    Open a connection to the Milvus database.
    """
    if not MILVUS_HOST or not MILVUS_PORT:
        raise ValueError("MILVUS_HOST and MILVUS_PORT must be defined in the .env file.")
    connections.connect(alias=alias, host=MILVUS_HOST, port=MILVUS_PORT)
    print(f"Connected to Milvus at {MILVUS_HOST}:{MILVUS_PORT}.")

def close_connection(alias="default"):
    """
    Close the connection to the Milvus database.
    """
    connections.disconnect(alias=alias)
    print("Disconnected from Milvus.")
