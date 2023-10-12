import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer, util

# Load the pre-trained sentence transformer model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def inference(text1, text2):
    # Encode the input sentences into sentence embeddings
    embeddings1 = model.encode(text1, convert_to_tensor=True)
    embeddings2 = model.encode(text2, convert_to_tensor=True)

    # Calculate the cosine similarity between the two sentence embeddings
    similarity_score = util.pytorch_cos_sim(embeddings1, embeddings2).item()

    return round(similarity_score, 2)
    