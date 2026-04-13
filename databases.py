import uuid
import datetime
import chromadb
from sqlalchemy import Column, String, DateTime, Text, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from embedding import get_embeddings


chroma_client = chromadb.PersistentClient(path="./jarvis_memory")
collection = chroma_client.get_or_create_collection(name="chat_history")


engine = create_engine(
    "sqlite:///jarvis_chats.db",
    connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class ChatMessage(Base):
    __tablename__ = "chats"

    id = Column(String, primary_key=True) 
    role = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)  


Base.metadata.create_all(engine)


def save_chat_to_db(role, content):
    msg_id = str(uuid.uuid4())

    try:
     
        vector = get_embeddings(content)

        
        db = SessionLocal()
        new_msg = ChatMessage(id=msg_id, role=role, content=content)
        db.add(new_msg)
        db.commit()
        db.close()

     
        collection.add(
            ids=[msg_id],
            embeddings=[vector],
            metadatas=[{"role": role}]
        )

        # print(f"Saved {msg_id} | len={len(vector)}")

    except Exception as e:
        print(f"Save failed: {e}")




def get_recent_context(limit=10):
    db = SessionLocal()
    
    recent_messages = db.query(ChatMessage).order_by(ChatMessage.timestamp.desc()).limit(limit).all()
    db.close()

    
    recent_messages.reverse()

    # Format for the LLM input
    context = []
    for msg in recent_messages:
        context.append({"role": msg.role, "content": msg.content})
    
    return context