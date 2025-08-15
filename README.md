# AI Blog Generator with Translation

A Streamlit-based blog generation system powered by LangGraph and Groq LLM. It creates SEO-friendly blog content and supports multi-language translation (currently Hindi and French).  

🌐 **Live Demo:** [Streamlit App](https://bloggeneratorgit-bgkj9c8a2rbu3ojejng4ef.streamlit.app/)  

---

## 🚀 Features

- Automated Blog Generation: Generate complete blog posts from just a topic  
- Multi-language Support: Translate blogs to Hindi and French  
- SEO-Optimized Titles: Generate search engine friendly titles  
- Graph-based Workflow: Uses LangGraph for structured content generation pipeline  
- Interactive UI: User-friendly Streamlit interface  
- Markdown Formatting: Rich text formatting for blog content  

---

## 🏗️ Architecture

The project uses a graph-based approach with LangGraph to create a structured workflow:

### Workflow Types

1. **Topic-only Workflow**  
   - Topic → Title Creation → Content Creation → End  

2. **Language Translation Workflow**  
   - Topic → Title Creation → Content Creation → Route → Translation (Hindi/French) → End  

---

## 📦 Project Structure

```
├── main.py                 # Streamlit application entry point
├── langgraph.json          # LangGraph configuration
├── pyproject.toml          # Project configuration and dependencies
├── requirements.txt        # Python dependencies
├── uv.lock                 # UV package manager lock file
├── README.md               # Project documentation
├── src/
│   ├── __init__.py         # Package initialization
│   ├── graphs/             # LangGraph workflow definitions
│   │   └── graph_builder.py
│   ├── nodes/              # Workflow nodes
│   │   └── blog_node.py
│   ├── states/             # State management
│   │   └── blog_state.py
│   └── LLMs/               # LLM integrations
│       └── groq_llm.py
└── __pycache__/            # Python cache (auto-generated)
```

---

## 🛠️ Installation

### Prerequisites
- Python 3.8+  
- Groq API Key  
- LangChain API Key (for LangSmith tracking)  

### Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd blog-generator
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

Or using UV:
```bash
uv sync
```

3. **Environment Configuration**  
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
LANGCHAIN_API_KEY=your_langchain_api_key_here
```

---

## 🚀 Usage

### Running Locally
Start the Streamlit app:
```bash
streamlit run main.py
```

The app will launch in your browser at `http://localhost:8501`

### Live Deployment
You can try the hosted version here:  
👉 [Streamlit App](https://bloggeneratorgit-bgkj9c8a2rbu3ojejng4ef.streamlit.app/)  

---

## 📊 Workflow Details

### Nodes
- Title Creation: Generates SEO-friendly blog titles  
- Content Creation: Creates detailed blog content with markdown formatting  
- Translation: Translates content to specified language  
- Route: Determines translation path based on language parameter  

### State Management
The system uses `BlogState` to maintain:
- Topic information  
- Current language  
- Blog content (title and body)  
- Translation status  

---

## 🔮 Future Enhancements

- [ ] Support for additional languages  
- [ ] Image generation integration  
- [ ] SEO metadata generation  
- [ ] Batch processing capabilities  
- [ ] Content optimization suggestions  
- [ ] Social media post generation  

---

## 📞 Support

For issues and questions:
1. Check the [Issues](../../issues) section  
2. Create a new issue with detailed description  
3. Include error logs and environment details  

---

## 🙏 Acknowledgments

- [LangGraph](https://langchain-ai.github.io/langgraph/) for workflow management  
- [Groq](https://groq.com/) for high-performance LLM inference  
- [Streamlit](https://streamlit.io/) for the UI framework  