import json
import config
from sentence_transformers import SentenceTransformer
from pymilvus import Collection
from python_utility.base_utility import open_connection, close_connection

def insert_price_list_data(collection_name, data_file):
    """
    Embed and insert data from a JSON file into a Milvus collection.
    """
    open_connection()

    # Load the embedding model
    embed_model = SentenceTransformer(config.EMBED_NAME)
    # Load data from JSON
    with open(data_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Prepare data for insertion
    product_codes, descriptions, units, prices, categories, embeddings = [], [], [], [], [], []

    for record in data:
        product_codes.append(record.get("product_code", ""))
        descriptions.append(record.get("description", ""))
        units.append(record.get("unit", ""))
        prices.append(str(record.get("price", "")))
        categories.append(record.get("category_name", ""))
        embeddings.append(embed_model.encode(record.get("description", ""), convert_to_tensor=False).tolist())

    # Insert data into the collection
    collection = Collection(collection_name)
    entities = [
        product_codes,
        descriptions,
        units,
        prices,
        categories,
        embeddings,
    ]

    collection.insert(entities)

    collection.flush()
    collection.load()
    print(f"Inserted {len(product_codes)} records into {collection_name}.")

    close_connection()

if __name__ == "__main__":
    data_file = "flattened_price_list.json"
    insert_price_list_data(f"{config.COLLECTION_NAME}", data_file)
