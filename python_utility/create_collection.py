from pymilvus import Collection, CollectionSchema, FieldSchema, DataType, utility
from base_utility import open_connection, close_connection

def create_index(collection, index_config):
    """
    Create an index for the specified field in the collection.

    Args:
        collection (Collection): The Milvus collection object.
        index_config (dict): Configuration for the index.
    """
    print(f"Creating index for field '{index_config['field_name']}'...")
    collection.create_index(
        field_name=index_config["field_name"],
        index_name=index_config["index_name"],
        index_params=index_config["index_params"]
    )
    print(f"Index '{index_config['index_name']}' created successfully.")

def create_collection(collection_name, vector_dim):
    """
    Create a collection in the Milvus database and automatically create an index.

    Args:
        collection_name (str): The name of the collection to create.
        vector_dim (int): The dimension of the vector field.
    """
    # Check if the collection already exists
    if utility.has_collection(collection_name):
        print(f"Collection named '{collection_name}' already exists.")
        return

    # Define schema for the collection
    field1 = FieldSchema(name="id", dtype=DataType.INT64, is_primary=True)
    field2 = FieldSchema(name="name", dtype=DataType.VARCHAR, max_length=100)
    field3 = FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=vector_dim)
    schema = CollectionSchema(fields=[field1, field2, field3], description=f"Schema for {collection_name}")

    # Create collection
    collection = Collection(name=collection_name, schema=schema)
    print(f"Collection '{collection_name}' created successfully.")

    # Index configuration(vector datatype)
    index = {
        "field_name": "embedding",  # Field to index
        "index_name": "embedding_index",  # Custom index name
        "index_params": {
            "index_type": "IVF_FLAT",  # Type of index
            "metric_type": "L2",  # Metric for similarity
            "params": {"nlist": 128}  # Number of clusters
        }
    }

    # Automatically create index
    create_index(collection, index)

if __name__ == "__main__":
    try:
        open_connection()

        # Define the collection name and vector dimension
        collection_name = input("Enter your desired new collection name :")
        vector_dim = 128  # Replace with your desired vector dimension

        # Create the collection
        create_collection(collection_name, vector_dim)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        close_connection()














# from pymilvus import Collection, FieldSchema, CollectionSchema, DataType
# from base_utility import open_connection, close_connection

# def create_collection(collection_name, vector_dim):
#     """
#     Create a collection in the Milvus database.

#     Args:
#         collection_name (str): The name of the collection to create.
#         vector_dim (int): The dimension of the vector field.
#     """
#     # Define schema for the collection
#     field1 = FieldSchema(name="id", dtype=DataType.INT64, is_primary=True)
#     field2 = FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=vector_dim)
#     schema = CollectionSchema(fields=[field1, field2], description=f"Schema for {collection_name}")

#     # Create collection
#     collection = Collection(name=collection_name, schema=schema)
#     print(f"Collection '{collection_name}' created successfully.")

# if __name__ == "__main__":
#     try:
#         open_connection()

#         # Define the collection name and vector dimension
#         collection_name = "example_collection"
#         vector_dim = 128  # Replace with your desired vector dimension

#         # Create the collection
#         create_collection(collection_name, vector_dim)
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     finally:
#         close_connection()
