# from pymilvus import utility
# from base_utility import open_connection, close_connection

# def delete_collection(collection_name):
#     """
#     Delete a collection from the Milvus database.

#     Args:
#         collection_name (str): The name of the collection to delete.
#     """
#     # Check if the collection exists
#     if utility.has_collection(collection_name):
#         # Drop the collection
#         utility.drop_collection(collection_name)
#         print(f"Collection '{collection_name}' has been deleted.")
#     else:
#         print(f"Collection '{collection_name}' does not exist.")

# if __name__ == "__main__":
#     try:
#         open_connection()

#         # Define the collection name to delete
#         collection_name = "test_collection"  # Replace with the collection you want to delete

#         # Delete the collection
#         delete_collection(collection_name)
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     finally:
#         close_connection()





from pymilvus import Collection
from base_utility import open_connection, close_connection

def delete_by_id(collection_name, ids_to_delete):
    """
    Delete entities from a Milvus collection by their IDs.

    Args:
        collection_name (str): The name of the collection to delete entities from.
        ids_to_delete (list): List of IDs to delete.
    """
    # Load the collection
    collection = Collection(name=collection_name)

    # Prepare the delete expression
    id_list = ", ".join(map(str, ids_to_delete))  # Convert list of IDs to a comma-separated string
    expr = f"id in [{id_list}]"

    # Deletion Notice
    collection.delete(expr)
    print(f"Deleted IDs {ids_to_delete} from collection '{collection_name}'.")

    # Flush to persist the deletion
    collection.flush()
    print("Deletion persisted to storage.")

if __name__ == "__main__":
    try:
        open_connection()

        # Define the collection name
        collection_name = input("Enter the collection name: ")

        # Input the IDs to delete
        ids_to_delete = input("Enter the IDs to delete (comma-separated): ")
        ids_to_delete = list(map(int, ids_to_delete.split(",")))

        # Delete the entities by ID
        delete_by_id(collection_name, ids_to_delete)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        close_connection()
