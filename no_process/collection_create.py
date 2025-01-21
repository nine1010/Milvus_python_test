from pymilvus import FieldSchema, CollectionSchema, DataType, Collection, utility
from python_utility.base_utility import open_connection, close_connection
import config

def create_price_list_collection(collection_name):
    """
    Create a collection in Milvus for the price list with the necessary schema.
    """
    open_connection()

    # Define schema fields
    field1 = FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True, description="Primary Key")
    field2 = FieldSchema(name="product_code", dtype=DataType.VARCHAR, max_length=100, description="Product Code")
    field3 = FieldSchema(name="description", dtype=DataType.VARCHAR, max_length=1024, description="Product Description")
    field4 = FieldSchema(name="unit", dtype=DataType.VARCHAR, max_length=50, description="Unit of Product")
    field5 = FieldSchema(name="price", dtype=DataType.VARCHAR, max_length=255, description="Product Price")
    field6 = FieldSchema(name="category_name", dtype=DataType.VARCHAR, max_length=255, description="Category Name")
    field7 = FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=config.DIMENSION, description="Vector Embeddings")

    schema = CollectionSchema(fields=[field1, field2, field3, field4, field5, field6, field7],
                              description="Price list collection with embeddings.")

    # Check if collection exists
    existing_collections = utility.list_collections()
    if config.COLLECTION_NAME in existing_collections:
        print(f"Collection {config.COLLECTION_NAME} already exists. Dropping it.")
        collection = Collection(config.COLLECTION_NAME)
        collection.drop()

    # Create the collection
    collection = Collection(name=collection_name, schema=schema)
    print(f"Collection {collection_name} created successfully.")
    
    # Config index
    index_params = {
        "index_type": "IVF_FLAT",  # Use IVF_FLAT, IVF_SQ8, or other index types
        "metric_type": config.METRIC_TYPE,
        "params": {"nlist": config.N_LIST}
    }
    collection.create_index(field_name="embedding", index_params=index_params)

    close_connection()

if __name__ == "__main__":
    create_price_list_collection(f"{config.COLLECTION_NAME}")
