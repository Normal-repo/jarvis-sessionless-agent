import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from sentence_transformers import SentenceTransformer



load_dotenv()

MODEL_ID = "microsoft/harrier-oss-v1-0.6b"
HF_TOKEN = os.getenv("HF_TOKEN")

def get_embeddings(text: str):


    client = InferenceClient(provider="hf-inference", api_key=HF_TOKEN)
    result = client.feature_extraction(text, model=MODEL_ID)

    if hasattr(result, "tolist"):
        result = result.tolist()

    if isinstance(result, list) and result and isinstance(result[0], (int, float)):
        return result

    if isinstance(result, list) and result and isinstance(result[0], list):
        return result[0]

    raise RuntimeError(f"Unexpected response format: {result}")


def get_embedding_model(text: str):
    return SentenceTransformer("BAAI/bge-m3")

      