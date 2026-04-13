import threading
from model import create_groq_client
from embedding import get_embeddings
from dotenv import load_dotenv
from databases import save_chat_to_db,get_recent_context

load_dotenv()

model = create_groq_client()


# --- async wrapper ---
def save_async(role, content):
    def task():
        try:
            save_chat_to_db(role, content)
        except Exception as e:
            print("❌ Save failed:", e)

    threading.Thread(target=task, daemon=True).start()


# --- main loop ---
while True:
    query = input("========>  ")

    if query.lower() == "exit":
        break


    save_async("user", query)
    history=get_recent_context()
    result = model.invoke([
    {"role": "system", "content": "You are a helpful assistant."},
    *history,
    {"role": "user", "content": query}
    ])
   
    print(result.content)

    
    save_async("assistant", result.content)