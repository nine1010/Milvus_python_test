from pymilvus import Collection
from sentence_transformers import SentenceTransformer
from python_utility.base_utility import open_connection, close_connection
import config

def search_collection(query_text, top_k=3):
    """
    Perform a vector search in the Milvus collection.
    """
    open_connection()

    # Load the embedding model
    embed_model = SentenceTransformer(config.EMBED_NAME)
    query_vector = embed_model.encode(query_text, convert_to_tensor=False).tolist()

    # Load the collection
    collection = Collection(config.COLLECTION_NAME)
    collection.load()

    # Perform the search
    search_params = {"metric_type": config.METRIC_TYPE, "params": {"nprobe": config.N_PROBE}}
    results = collection.search(
        data=[query_vector],
        anns_field="embedding",
        param=search_params,
        limit=top_k,
        output_fields=["product_code", "description", "price", "category_name"]
    )

    # display the results
    for rank, hit in enumerate(results[0], start=1):
        print(f"Match {rank}: {hit.score}")
        print(f"    product_code: {hit.entity.get('product_code')}")
        print(f"    description: {hit.entity.get('description')}")
        print(f"    price: {hit.entity.get('price')}")
        print(f"    category_name: {hit.entity.get('category_name')}\n")

    close_connection()

if __name__ == "__main__":
    query = input("Enter word to query :")
    search_collection(query, top_k=config.TOP_K)
