from pymilvus import Collection, utility
from delete_by_id import delete_by_id
from base_utility import open_connection, close_connection


def edit_by_id(collection_name, target_id, new_name):
    """
    Edit the name of a record by its ID.

    Args:
        collection_name (str): The name of the collection.
        target_id (int): The ID of the record to edit.
        new_name (str): The new name to assign to the record.
    """
    # Check if the collection exists
    if not utility.has_collection(collection_name):
        raise ValueError(f"Collection '{collection_name}' does not exist.")

    # Connect to the collection
    collection = Collection(name=collection_name)

    # Search for the record to ensure it exists
    results = collection.query(expr=f"id == {target_id}", output_fields=["id", "name", "embedding"])
    if not results:
        raise ValueError(f"Record with ID {target_id} does not exist or is out of range.")

    # Extract the original vector
    original_vector = results[0]["embedding"]

    # Delete the record with the specified ID
    delete_by_id(collection_name, [target_id])

    # Reinsert the record with the updated name
    data = [[target_id], [new_name], [original_vector]]
    collection.insert(data)

    print(f"Successfully updated record with ID {target_id} to name '{new_name}'.")

if __name__ == "__main__":

    try:
        open_connection()

        # Define collection details
        collection_name = input("Enter collection name want to edit: ")
        target_id = int(input("Enter the ID of the record you want to edit: "))
        new_name = input("Enter the new name: ")

        # Edit the record
        edit_by_id(collection_name, target_id, new_name)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        close_connection()
