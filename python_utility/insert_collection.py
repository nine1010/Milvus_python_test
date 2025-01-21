# from pymilvus import Collection
# from base_utility import open_connection, close_connection
# import numpy as np

# def generate_data(num_records, vector_dim):
#     """
#     Generate random data for insertion into a collection.

#     Args:
#         num_records (int): Number of records to generate.
#         vector_dim (int): Dimension of the vector field.

#     Returns:
#         tuple: A tuple containing a list of IDs and a list of vectors.
#     """
#     ids = list(range(1, num_records + 1))  # Auto-generate sequential IDs
#     vectors = np.random.rand(num_records, vector_dim).tolist()  # Generate random vectors
#     return ids, vectors

# def insert_data(collection_name, num_records, vector_dim):
#     """
#     Insert data into the specified Milvus collection and flush and load it.

#     Args:
#         collection_name (str): The name of the collection to insert data into.
#         num_records (int): Number of records to insert.
#         vector_dim (int): Dimension of the vector field.
#     """
#     # Load the collection
#     collection = Collection(name=collection_name)

#     # Generate data
#     ids, vectors = generate_data(num_records, vector_dim)

#     # Insert data into the collection
#     result = collection.insert([ids, vectors])

#     collection.flush()
#     collection.load()

#     print(f"Data inserted into collection '{collection_name}' successfully.")
#     print(f"Collection '{collection_name}' now contains {collection.num_entities} entities.")
#     return result

# if __name__ == "__main__":
#     try:
#         open_connection()

#         # Define the collection name, number of records, and vector dimension
#         collection_name = "example_collection"  # Replace with your collection name
#         num_records = 50  # Number of records to insert
#         vector_dim = 128  # Replace with your collection's vector dimension

#         # Insert data
#         insert_data(collection_name, num_records, vector_dim)
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     finally:
#         close_connection()




from pymilvus import Collection, utility
from faker import Faker
import numpy as np

def insert_data(collection_name, num_rows, vector_dim):
    """
    Inserts auto-generated data into the specified collection.

    Args:
        collection_name (str): The name of the Milvus collection.
        num_rows (int): The number of rows to insert.
        vector_dim (int): The dimension of the vector field.
    """
    # Connect to the collection
    collection = Collection(name=collection_name)

    if not utility.has_collection(collection_name):
        raise ValueError(f"Collection '{collection_name}' does not exist.")

    faker = Faker()

    # Generate data
    ids = list(range(1, num_rows + 1))  # Auto-incremented IDs starting from 1
    names = [faker.name() for _ in range(num_rows)]  # Fake names
    vectors = np.random.random((num_rows, vector_dim)).tolist()  # Random vectors

    collection.insert([ids, names, vectors])
    collection.flush()
    collection.load()

    print(f"Successfully inserted {num_rows} ids into collection '{collection_name}'.")

if __name__ == "__main__":
    from base_utility import open_connection, close_connection

    try:
        open_connection()

        # Define collection details
        collection_name = "test_collection"  # Replace with your collection name
        num_rows = 40  # Number of rows to insert
        vector_dim = 128  # Vector dimension (must match the collection schema)

        # Insert data
        insert_data(collection_name, num_rows, vector_dim)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        close_connection()

