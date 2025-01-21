## Embedding Model
For multilingual data, the choice of embedding model is crucial to ensure high-quality search results across languages. Here are some of the best models for embedding multilingual data, categorized by their capabilities and compatibility:

---

### **General-Purpose Multilingual Embedding Models**
1. **[LaBSE (Language-Agnostic BERT Sentence Embedding)](https://huggingface.co/sentence-transformers/LaBSE)**  
   - **Coverage**: Over 100 languages.
   - **Highlights**:
     - Designed specifically for multilingual sentence embeddings.
     - Strong performance for cross-language tasks.
   - **Dimension**: 768.

2. **[XLM-RoBERTa](https://huggingface.co/models?search=xlm-roberta)**  
   - **Variants**:
     - XLM-RoBERTa Base.
     - XLM-RoBERTa Large.
   - **Coverage**: 100+ languages.
   - **Highlights**:
     - Supports complex multilingual tasks.
     - Works well for sentence classification and similarity.
   - **Dimension**: 768–1024.

3. **[mUSE (Multilingual Universal Sentence Encoder)](https://tfhub.dev/google/universal-sentence-encoder-multilingual/3)**  
   - **Coverage**: 16 languages.
   - **Highlights**:
     - Simple and fast.
     - Designed for sentence-level embeddings.
   - **Dimension**: 512.

4. **[distiluse-base-multilingual-cased-v1](https://huggingface.co/sentence-transformers/distiluse-base-multilingual-cased-v1)**  
   - **Coverage**: 50+ languages.
   - **Highlights**:
     - Lightweight, distilled version for efficiency.
     - Good balance of speed and performance.
   - **Dimension**: 512.

---

### **Advanced Multilingual Models**
1. **[Multilingual BERT (mBERT)](https://github.com/google-research/bert/blob/master/multilingual.md)**  
   - **Coverage**: 104 languages.
   - **Highlights**:
     - Pretrained by Google on multilingual data.
     - Versatile for various NLP tasks.
   - **Dimension**: 768.

2. **[InfoXLM](https://huggingface.co/microsoft/infoxlm-base)**  
   - **Coverage**: 94 languages.
   - **Highlights**:
     - Pretrained with translation tasks in mind.
     - Better cross-language representation.
   - **Dimension**: 768.

3. **[RemBERT](https://huggingface.co/google/rembert)**  
   - **Coverage**: 110 languages.
   - **Highlights**:
     - Specifically designed for cross-language retrieval.
     - Works well with noisy data.
   - **Dimension**: 1152.

---

### **Lightweight Multilingual Models**
1. **[MiniLM-L12-H384](https://huggingface.co/sentence-transformers/all-MiniLM-L12-v2)**  
   - **Coverage**: Limited but effective for multilingual datasets.
   - **Highlights**:
     - Faster inference for lightweight applications.
   - **Dimension**: 384.

2. **[mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2)**  
   - **Coverage**: 50+ languages.
   - **Highlights**:
     - High accuracy with reduced computational cost.
   - **Dimension**: 768.

---

### **Large-Scale Multilingual Models**
1. **[T-ULRv2](https://huggingface.co/google/mt5-large)**  
   - **Coverage**: Over 100 languages.
   - **Highlights**:
     - Excellent for multilingual and translation tasks.
     - Suitable for larger-scale systems.
   - **Dimension**: 1024.

2. **[mT5 (Multilingual T5)](https://huggingface.co/models?filter=mt5)**  
   - **Coverage**: Over 100 languages.
   - **Highlights**:
     - Powerful for both embedding and generative tasks.
   - **Dimension**: 512–1024.

---

### **Specialized Multilingual Models**
1. **[LASER (Language-Agnostic SEntence Representations)](https://github.com/facebookresearch/LASER)**  
   - **Coverage**: 93 languages.
   - **Highlights**:
     - Designed by Facebook for large-scale multilingual similarity tasks.
   - **Dimension**: 1024.

2. **[M2M-100](https://huggingface.co/facebook/m2m100_418M)**  
   - **Coverage**: 100+ languages.
   - **Highlights**:
     - Focuses on multilingual translation, suitable for embedding translation tasks.
   - **Dimension**: 512.

---

#### **Recommended Approach**
- **For General Multilingual Data**: Use **LaBSE** or **XLM-RoBERTa**.
- **For Lightweight Applications**: Try **distiluse-base-multilingual-cased-v1** or **MiniLM-L12-H384**.
- **For Advanced Cross-Language Retrieval**: Choose **RemBERT** or **InfoXLM**.
- **For Large-Scale Systems**: Use **mT5** or **LASER**.

## Variable meanings
Here's a detailed explanation of the configuration fields, their meanings, and how to adjust them based on your chosen model and use case:

---

### **1. `COLLECTION_NAME`**
- **What It Means**: 
  The name of the collection in Milvus where the data and embeddings are stored.
- **Impact**: 
  Changing this allows you to manage multiple collections (e.g., testing with different embedding models or configurations).
- **Adjustment**: 
  Use a meaningful name, often versioned (`price_list_v1`, `price_list_v2`) to track different setups.

---

### **2. `EMBED_NAME`**
- **What It Means**: 
  The name of the sentence transformer model used for generating embeddings.
- **Impact**: 
  The embedding quality, vector dimension (`DIMENSION`), and multilingual support depend on the chosen model.
- **Adjustment**: 
  - Select a model that aligns with your dataset and query needs.
  - Example:
    - For multilingual data: `sentence-transformers/LaBSE`, `distiluse-base-multilingual-cased-v1`.
    - For lightweight usage: `all-MiniLM-L6-v2`.

---

### **3. `METRIC_TYPE`**
- **What It Means**: 
  The metric used to calculate similarity between vectors during a search.
- **Common Metrics**:
  - `COSINE`: Measures the cosine of the angle between two vectors. Best for normalized embeddings.
  - `L2`: Euclidean distance. Best for unnormalized embeddings.
  - `IP` (Inner Product): Measures the dot product. Often used for dense vectors.
- **Impact**: 
  Impacts how search results are scored. For most modern embeddings, `COSINE` is preferred as embeddings are normalized.
- **Adjustment**: 
  Match the metric to your embedding model:
  - For normalized embeddings: Use `COSINE`.
  - For unnormalized embeddings: Use `L2`.

---

### **4. `DIMENSION`**
- **What It Means**: 
  The size of the embedding vectors generated by the model.
- **Impact**: 
  The schema in Milvus requires the vector field's `dim` to match the embedding dimension. If mismatched, Milvus will reject the data.
- **Adjustment**:
  - Check the dimension of the chosen model. For example:
    - `LaBSE`: 768.
    - `all-MiniLM-L6-v2`: 384.
  - Set `DIMENSION` to match the model's output.

---

### **5. `N_LIST`**
- **What It Means**: 
  Number of clusters for the IVF (Inverted File) index.
- **Impact**: 
  A higher `N_LIST`:
  - Increases index accuracy (more clusters, better search granularity).
  - Increases memory usage and index building time.
  A lower `N_LIST`:
  - Reduces accuracy.
  - Speeds up index building and lowers memory usage.
- **Adjustment**:
  - Start with a moderate value (e.g., 512).
  - For small datasets (<100,000 vectors), use 128–512.
  - For larger datasets, use 1024–4096.

---

### **6. `N_PROBE`**
- **What It Means**: 
  Number of clusters to search during a query.
- **Impact**: 
  A higher `N_PROBE`:
  - Improves accuracy but increases query latency.
  A lower `N_PROBE`:
  - Reduces latency but may return less accurate results.
- **Adjustment**:
  - Start with 32.
  - For faster searches: Use 8–16.
  - For higher accuracy: Use 64–128.

---

### **7. `TOP_K`**
- **What It Means**: 
  The number of nearest neighbors to return for each query.
- **Impact**: 
  - Higher `TOP_K`: Returns more results but increases query time.
  - Lower `TOP_K`: Speeds up queries but might omit relevant results.
- **Adjustment**:
  - Use 3–10 for most use cases.
  - For larger datasets or broad searches, consider 20–50.

---

### **Guidance for Adjustment**
1. **Based on Model**:
   - Check the model's output dimension and set `DIMENSION` accordingly.
   - Use `COSINE` for normalized embeddings.

2. **Dataset Size**:
   - Small datasets (<100k vectors): Use `N_LIST=128–512`, `N_PROBE=16–32`.
   - Large datasets (>1M vectors): Use `N_LIST=1024–4096`, `N_PROBE=64`.

3. **Query Requirements**:
   - For high accuracy: Increase `N_PROBE` and `N_LIST`.
   - For speed: Decrease `N_PROBE` and `N_LIST`.

4. **Testing**:
   - Experiment with values for `N_LIST` and `N_PROBE` to balance accuracy and latency.
   - Use evaluation metrics (e.g., recall, latency) to measure performance.


The interpretation of "higher" or "lower" distances being "good" depends on the **metric type** used in the search. Here's an explanation of how each metric works and why their behavior differs:

---

### **1. Metric Types and Their Impact**

#### **Cosine Similarity (`COSINE`)**
- **Definition**: Measures the cosine of the angle between two vectors in the embedding space.
- **Range**: From `-1` to `1` (though typically normalized to `0` to `1` for most embedding models).
  - `1` indicates identical vectors.
  - `0` indicates orthogonal vectors (completely unrelated).
- **In Milvus**: 
  - It reports **distance** as `1 - similarity`, so **lower distances** are better.
- **Example**:
  - Distance = `0.1` → High similarity (good match).
  - Distance = `0.9` → Low similarity (poor match).

---

#### **Euclidean Distance (`L2`)**
- **Definition**: Measures the straight-line distance between two points in the vector space.
- **Range**: From `0` to infinity.
  - `0` indicates identical vectors.
  - Higher values indicate more dissimilarity.
- **In Milvus**: 
  - **Lower distances** are always better.
- **Example**:
  - Distance = `2.0` → Closer match (good).
  - Distance = `15.0` → Farther match (bad).

---

#### **Inner Product (`IP`)**
- **Definition**: Measures the dot product between two vectors.
- **Range**: Can be negative, zero, or positive.
  - Higher values indicate greater similarity.
  - Lower (or negative) values indicate less similarity.
- **In Milvus**:
  - **Higher distances** (or scores) are better.
- **Example**:
  - Score = `100` → Strong similarity (good match).
  - Score = `-5` → Weak similarity (poor match).

---

### **2. Why Does the Behavior Differ?**

- **`COSINE` and `L2` prioritize lower distances** because they measure dissimilarity directly.
  - Lower distance = Higher similarity.
- **`IP` prioritizes higher distances (scores)** because it measures similarity directly.
  - Higher distance = Higher similarity.

---

### **3. How to Choose the Metric Type**
1. **When to Use `COSINE`:**
   - If your embedding model normalizes vectors (e.g., models like `LaBSE` or `all-MiniLM`).
   - Most natural language processing (NLP) tasks favor `COSINE`.

2. **When to Use `L2`:**
   - If your embedding model does **not normalize vectors**.
   - Works well for dense, high-dimensional data, such as image or video embeddings.

3. **When to Use `IP`:**
   - If you're working with embeddings designed for **maximizing dot product similarity**.
   - Often used in recommendation systems or custom-trained embeddings.

---

### **4. Best Practices for Consistency**
- Always verify the metric type (`COSINE`, `L2`, or `IP`) when interpreting search results.
- For `COSINE` or `L2`, **lower distance is better**.
- For `IP`, **higher distance (score) is better**.

---