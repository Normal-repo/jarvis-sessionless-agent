# 🧠 Jarvis - Sessionless AI Agent

A persistent AI assistant that maintains a single identity across conversations using a unified memory system. Unlike traditional chatbots that reset with each session, Jarvis remembers conversations, user context, and adapts behavior accordingly.

## 📋 What It Does

- **No Sessions**: Single identity that persists across all conversations
- **Persistent Memory**: Automatically stores and retrieves conversation history
- **Vector Search**: Uses embeddings to find relevant past interactions
- **Stateful**: Maintains context without reinitializing

## 🏗️ How It Works

### Three-Layer Storage

```
User Input
    ↓
[SQLite] - Store messages & metadata
    ↓
[ChromaDB] - Embed & index for search
    ↓
[Retrieve Context] - Find relevant past messages
    ↓
[LLM Response] - Generate response with context
    ↓
[Memory Update] - Save new interaction
```

1. **SQLite** - Chat history database
   - Stores all messages with timestamps
   - Maintains user identity
   - Transaction support

2. **ChromaDB** - Vector embeddings
   - Converts messages to embeddings
   - Enables similarity search
   - Finds relevant past conversations

3. **Anthropic Claude API** - Language model
   - Processes queries with context
   - Generates intelligent responses

## 🛠️ Tech Stack

- **Python 3.x** - Core language
- **SQLite** - Message storage
- **ChromaDB** - Vector embeddings & search
- **Anthropic Claude API** - LLM
- **Sentence Transformers** - Embedding generation

## 📁 Project Structure

```
jarvis-sessionless-agent/
├── main.py          # Entry point & main loop
├── model.py         # LLM integration (Claude API)
├── embedding.py     # Embedding & similarity search
├── databases.py     # Database connections (SQLite, ChromaDB)
├── tools.py         # Tool system (extensible)
└── README.md        # Documentation
```

## 🔧 Key Features

### Persistent User ID
```python
user_id = "normal_001"  # Same across all sessions
```

### Message Storage
```python
# Automatically saves every message
# Includes: content, user_id, timestamp, role
```

### Vector Search
```python
# Retrieves similar past messages
# Used to build context for responses
```

### Tool System
```python
# tools.py structure for extensible actions
# Ready for: delete_memory, web_search, etc.
```

## 📦 Installation

```bash
git clone https://github.com/Normal-repo/jarvis-sessionless-agent.git
cd jarvis-sessionless-agent

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

## ⚙️ Environment Setup

Create `.env` file:
```
ANTHROPIC_API_KEY=your_api_key_here
CHROMA_DB_PATH=./chroma_data
SQLITE_DB_PATH=./jarvis_chats.db
USER_ID=normal_001
```

## 🚀 Running

```bash
python main.py
```

## 💾 Database Schema

### SQLite Messages Table
```sql
CREATE TABLE messages (
    id INTEGER PRIMARY KEY,
    user_id TEXT,
    role TEXT,  -- "user" or "assistant"
    content TEXT,
    timestamp DATETIME,
    embedding_id TEXT
)
```

### ChromaDB Collections
```
Collection: "messages"
- Stores embeddings of all messages
- Enables similarity search
```

## 🎯 Current Capabilities

✅ Persistent chat without session resets
✅ Message history storage
✅ Vector similarity search
✅ Context-aware responses
✅ User identity persistence
✅ Extensible tool framework

## 🔮 Future Tools (Ready for Extension)

The `tools.py` file is structured for adding:
- Memory deletion
- Preference learning  
- Web search integration
- Advanced filtering

Tools can be added without modifying core system.

## 📝 License

MIT License

## 👤 Author

**Normal-repo** - Persistent AI Systems