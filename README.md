# 🧠 Jarvis-like Persistent AI Agent

A sophisticated AI assistant with unified memory, RAG (Retrieval-Augmented Generation), and adaptive preferences. Unlike traditional chatbots that reset with each session, Jarvis maintains a continuous identity with persistent, intelligent memory.

## 🎯 Project Goals

- **Sessionless**: Single identity that persists across conversations
- **Intelligent Memory**: Retrieves relevant past information automatically
- **Adaptive Learning**: Learns preferences and adapts behavior over time
- **Knowledge Integration**: Supports RAG for enhanced context understanding
- **Tool Integration**: Extensible system for future tools (web search, OCR, etc.)

## 🏗️ System Architecture

### 🧩 Three-Layer Storage System

```
┌─────────────────────────────────────────────┐
│           PERSISTENCE LAYER                 │
├─────────────────────────────────────────────┤
│  SQLite        ChromaDB       MongoDB       │
│  (Structure)   (Vectors)      (Semantics)   │
└─────────────────────────────────────────────┘
         ↓              ↓              ↓
┌─────────────────────────────────────────────┐
│         UNIFIED MEMORY SYSTEM               │
└─────────────────────────────────────────────┘
         ↓              ↓              ↓
    Structured       Vector         Semantic
    (Chat History) (Similarity)    (Preferences)
```

#### 1. 📋 **SQLite** (Structured Memory)
- Chat history with full context
- Message metadata (timestamps, user_id)
- Transactional integrity

#### 2. 🔍 **ChromaDB** (Vector Memory)
- Embeddings of all messages
- Similarity search for RAG retrieval
- Semantic matching of historical context

#### 3. 🧠 **MongoDB** (Semantic Memory)
- User preferences and behaviors
- Important long-term facts
- Confidence scoring for learned patterns

### 🔄 Data Flow

```
User Input
   ↓
[Memory Check] → Do we need context?
   ↓
[RAG Retrieval] → Fetch similar past messages
   ↓
[Preferences] → Load user settings from MongoDB
   ↓
[Recent Chat] → Get last N messages from SQLite
   ↓
[Prompt Building] → Combine all context
   ↓
[LLM Response] → Generate intelligent response
   ↓
[Memory Update] → Store message + update embeddings
```

## ✅ Current Implementation Status

### ✔️ Completed
- ✅ Persistent chat system (single user_id, no session reset)
- ✅ SQLite integration for message storage
- ✅ LLM integration (response generation)
- ✅ ChromaDB setup with embeddings
- ✅ Basic memory recall (system remembers user context)
- ✅ .gitignore for sensitive files

### ⚠️ Not Yet Implemented
- ❌ Intelligent RAG retrieval
- ❌ Preference system (MongoDB integration)
- ❌ Decay system for memory relevance
- ❌ Tool system (extensible actions)
- ❌ Document/OCR support

## 🚀 Implementation Roadmap

### 🔥 **PHASE 1** — RAG Integration (PRIORITY)
Implement intelligent context retrieval
- Embed user queries
- Retrieve top-5 similar messages from ChromaDB
- Format retrieved context for LLM prompt
- **Outcome**: AI recalls relevant past conversations

### 🧠 **PHASE 2** — MongoDB Integration
Add structured preference and importance storage
- `preferences` collection: learned user behaviors
- `important_memory` collection: significant facts
- **Outcome**: Personalized responses based on history

### ⚙️ **PHASE 3** — Self-RAG Decision Layer
Optimize when to retrieve memory
- Keyword detection ("remember", "before", "last time")
- LLM-based retrieval decisions
- **Outcome**: Efficient memory usage

### ⚖️ **PHASE 4** — Decay System
Keep memory relevant over time
- Score-based ranking
- Exponential decay with refresh on usage
- **Outcome**: Important memories stay accessible, noise fades

### 🧰 **PHASE 5** — Tool System
Enable agentic capabilities
- Example: `delete_memory`, `web_search`
- Extensible interface for future tools
- **Outcome**: AI can perform actions beyond chat

### 📄 **PHASE 6** — Document Memory
Store documents as memory
- File upload → text extraction → chunking → embedding
- Treat as extended memory layer

### 🖼️ **PHASE 7** — OCR Support
Process images as memory
- Extract text from images using Tesseract
- Store as embedded knowledge

### ⚡ **PHASE 8** — Performance Optimization
- Parallel database operations
- Query caching
- Batch embedding

### 🧠 **PHASE 9** — Intelligence Layer
- Importance scoring algorithms
- Chat summarization for long histories
- Preference conflict resolution

## 🛠️ Technology Stack

- **Python 3.x**: Core language
- **SQLite**: Structured message history
- **ChromaDB**: Vector embeddings and similarity search
- **MongoDB**: Semantic memory and preferences
- **Anthropic Claude API**: LLM backbone
- **Sentence Transformers**: Embedding generation

## 📦 Installation

```bash
# Clone repository
git clone https://github.com/Normal-repo/jarvis-sessionless-agent.git
cd jarvis-sessionless-agent

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env with your API keys
```

## 🚀 Quick Start

```bash
# Run the agent
python main.py

# Example interaction
> Tell me about your preferences
> Remember I like short responses
> Tell me about yourself
```

## 📁 Project Structure

```
jarvis-sessionless-agent/
├── main.py              # Entry point
├── model.py             # LLM integration
├── embedding.py         # Vector embedding logic
├── databases.py         # Database connections (SQLite, ChromaDB, MongoDB)
├── tools.py             # Tool system (future)
├── .gitignore          # Git ignore configuration
└── README.md           # This file
```

## 🔑 Key Concepts

### Sessionless Design
Instead of isolated sessions, the system maintains a unified `user_id` that persists all conversations. All memory operations reference this identity.

### Intelligent RAG
Rather than retrieving all context, the system:
1. Embeds the current query
2. Searches for semantically similar past messages
3. Ranks by relevance and recency
4. Includes only the most relevant context

### Adaptive Memory
The system learns:
- User preferences (style, tone, depth)
- Important facts about the user
- Patterns in conversation

Memory decays naturally—important memories stay fresh, irrelevant ones fade.

## 🎓 Learning Outcomes

Building this system teaches:
- Multi-database architecture
- Vector embeddings and semantic search
- Agentic AI patterns
- Memory management at scale
- LLM prompt engineering

## 🤝 Contributing

This is an active development project. Future contributions welcome for:
- Additional storage backends
- Tool implementations
- Performance optimization
- Advanced memory algorithms

## 📊 Project Complexity

| Aspect | Rating |
|--------|--------|
| Complexity | ⭐⭐⭐⭐⭐ |
| Innovation | ⭐⭐⭐⭐⭐ |
| Practical Value | ⭐⭐⭐⭐⭐ |

## 💡 What Makes This Different

This is **not** a:
- ❌ Chat session system
- ❌ Simple RAG pipeline
- ❌ Single-database solution

This **is** a:
- ✅ Persistent AI system with continuous identity
- ✅ Unified memory architecture
- ✅ Adaptive learning framework
- ✅ Extensible agentic platform

## 🧭 Next Steps

**START HERE:**
1. Implement RAG retrieval (Phase 1)
2. Integrate MongoDB for preferences (Phase 2)
3. Add decision layer for smart memory usage (Phase 3)

**DO NOT ADD YET:**
- Tools/actions (implement foundation first)
- OCR/documents (scale after core works)
- Complex decay algorithms (start simple)

## 📝 License

MIT License - See LICENSE file for details

## 👤 Author

**Normal-repo** - Building the next generation of persistent AI

---

**One-Line Summary:**
*You've built the memory foundation. Now build the intelligence layer on top.*