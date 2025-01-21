# ------------------------------MiniLM---------------------------------------------
# # ------- test1------- # got 0.5537 but the information is correct?
# COLLECTION_NAME = "price_list_1"
# EMBED_NAME = "sentence-transformers/all-MiniLM-L6-v2"  # Change this to your preferred model
# METRIC_TYPE = "COSINE"
# DIMENSION = 384  # Update based on the chosen model
# N_LIST = 512
# N_PROBE = 32
# TOP_K = 3

# # ------- test2------- #note : got the lowest of 0.1882... decent
# COLLECTION_NAME = "price_list_2"
# EMBED_NAME = "sentence-transformers/all-MiniLM-L6-v2"  # Change this to your preferred model
# METRIC_TYPE = "COSINE"
# DIMENSION = 384  # Update based on the chosen model
# N_LIST = 512
# N_PROBE = 32
# TOP_K = 4

# ------- test3------- # note : same result as test 1 (N-Probe has low impact) - not include AU will worsen the result
# COLLECTION_NAME = "price_list_3" 
# EMBED_NAME = "sentence-transformers/all-MiniLM-L6-v2"  # Change this to your preferred model
# METRIC_TYPE = "COSINE"
# DIMENSION = 384  # Update based on the chosen model
# N_LIST = 512
# N_PROBE = 64
# TOP_K = 3

# # # ------- test4------- # note : lowest at 0.898925464153289795 the information is accurate
# COLLECTION_NAME = "price_list_4"
# EMBED_NAME = "sentence-transformers/all-MiniLM-L6-v2"  # Change this to your preferred model
# METRIC_TYPE = "L2"
# DIMENSION = 384  # Update based on the chosen model
# N_LIST = 512
# N_PROBE = 32
# TOP_K = 3

# # ------- test5------- # lowest at 0.8925464153289795 info are correct
# COLLECTION_NAME = "price_list_5"
# EMBED_NAME = "sentence-transformers/all-MiniLM-L6-v2"  # Change this to your preferred model
# METRIC_TYPE = "L2"
# DIMENSION = 384  # Update based on the chosen model
# N_LIST = 512
# N_PROBE = 32
# TOP_K = 4

# --------------------------LaBSE------------------------
# # ------- test6-------
# COLLECTION_NAME = "price_list_6" # high distance but correct info
# EMBED_NAME = "sentence-transformers/LaBSE"  # Change this to your preferred model
# METRIC_TYPE = "COSINE"
# DIMENSION = 768  # Update based on the chosen model
# N_LIST = 512
# N_PROBE = 64
# TOP_K = 3


# ------- test7-------
COLLECTION_NAME = "price_list_7"
EMBED_NAME = "sentence-transformers/distiluse-base-multilingual-cased-v1"  # Change this to your preferred model
METRIC_TYPE = "L2"
DIMENSION = 512  # Update based on the chosen model
N_LIST = 512
N_PROBE = 32
TOP_K = 5

# # ------- test1-------
# COLLECTION_NAME = "price_list_1"
# EMBED_NAME = "sentence-transformers/all-MiniLM-L6-v2"  # Change this to your preferred model
# METRIC_TYPE = "COSINE"
# DIMENSION = 384  # Update based on the chosen model
# N_LIST = 512
# N_PROBE = 32
# TOP_K = 3

# # ------- test1-------
# COLLECTION_NAME = "price_list_1"
# EMBED_NAME = "sentence-transformers/all-MiniLM-L6-v2"  # Change this to your preferred model
# METRIC_TYPE = "COSINE"
# DIMENSION = 384  # Update based on the chosen model
# N_LIST = 512
# N_PROBE = 32
# TOP_K = 3