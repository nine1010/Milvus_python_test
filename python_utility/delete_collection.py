from pymilvus import utility
from base_utility import open_connection, close_connection

def delete_collection(collection_name):
    """
    Delete a collection from the Milvus database.

    Args:
        collection_name (str): The name of the collection to delete.
    """
    # Check if the collection exists
    if utility.has_collection(collection_name):
        # Drop the collection
        utility.drop_collection(collection_name)
        print(f"Collection '{collection_name}' has been deleted.")
    else:
        print(f"Collection '{collection_name}' does not exist.")

if __name__ == "__main__":
    try:
        open_connection()

        # Define the collection name to delete
        collection_name = input("Enter collection name to delete :")  # Replace with the collection you want to delete

        # Delete the collection
        delete_collection(collection_name)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        close_connection()