# AI Blog Generator with Translation

A FastAPI-based blog generation system powered by LangGraph and Groq LLM that creates SEO-friendly blog content and supports multi-language translation.

## 🚀 Features

- **Automated Blog Generation**: Create complete blog posts from just a topic
- **Multi-language Support**: Translate blogs to Hindi and French
- **SEO-Optimized Titles**: Generate search engine friendly titles
- **Graph-based Workflow**: Uses LangGraph for structured content generation pipeline
- **REST API**: Easy integration with web applications
- **Markdown Formatting**: Rich text formatting for blog content

## 🏗️ Architecture

The project uses a graph-based approach with LangGraph to create a structured workflow:

### Workflow Types

1. **Topic-only Workflow**:
   - Topic → Title Creation → Content Creation → End

2. **Language Translation Workflow**:
   - Topic → Title Creation → Content Creation → Route → Translation (Hindi/French) → End

## 📦 Project Structure

```
├── app.py                  # FastAPI application entry point
├── main.py                 # Alternative entry point
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

Using pip:
```bash
pip install -r requirements.txt
```

Or using UV (recommended):
```bash
uv sync
```

3. **Setup dependencies**
```bash
pip install -r requirements.txt
```

3. **Setup dependencies**
```bash
pip install -r requirements.txt
```

4. **Environment Configuration**
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
LANGCHAIN_API_KEY=your_langchain_api_key_here
```

### Dependencies
The project uses modern Python packaging with `pyproject.toml`. Key dependencies include:
- FastAPI for the web API
- LangGraph for workflow management  
- LangChain for LLM integration
- Groq for high-performance inference
- UV for fast package management

## 🚀 Usage

### Starting the Server
```bash
python app.py
```
The server will start at `http://localhost:5000`

### API Endpoints

#### Generate Blog (Topic Only)
```bash
POST /blogs
Content-Type: application/json

{
    "topic": "The Future of Artificial Intelligence"
}
```

#### Generate Blog with Translation
```bash
POST /blogs
Content-Type: application/json

{
    "topic": "The Future of Artificial Intelligence",
    "language": "hindi"
}
```

**Supported Languages:**
- `hindi`
- `french`

### Example Response
```json
{
    "data": {
        "topic": "The Future of Artificial Intelligence",
        "current_language": "hindi",
        "blog": {
            "title": "कृत्रिम बुद्धिमत्ता का भविष्य",
            "content": "# कृत्रिम बुद्धिमत्ता का भविष्य\n\n..."
        }
    }
}
```

## 🔧 Configuration

### LangGraph Studio Integration
The project includes configuration for LangGraph Studio visualization. The graph can be compiled and visualized using:
```python
from src.graphs.graph_builder import graph
```

### Environment Variables
- `GROQ_API_KEY`: Your Groq API key for LLM access
- `LANGCHAIN_API_KEY`: LangChain API key for LangSmith tracking

## 📊 Workflow Details

### Nodes
- **Title Creation**: Generates SEO-friendly blog titles
- **Content Creation**: Creates detailed blog content with markdown formatting
- **Translation**: Translates content to specified language
- **Route**: Determines translation path based on language parameter

### State Management
The system uses `BlogState` to maintain:
- Topic information
- Current language
- Blog content (title and body)
- Translation status

## 🌐 API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:5000/docs`
- ReDoc: `http://localhost:5000/redoc`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔮 Future Enhancements

- [ ] Support for additional languages
- [ ] Image generation integration
- [ ] SEO metadata generation
- [ ] Batch processing capabilities
- [ ] Content optimization suggestions
- [ ] Social media post generation

## 📞 Support

For issues and questions:
1. Check the [Issues](../../issues) section
2. Create a new issue with detailed description
3. Include error logs and environment details

## 🙏 Acknowledgments

- [LangGraph](https://langchain-ai.github.io/langgraph/) for workflow management
- [Groq](https://groq.com/) for high-performance LLM inference
- [FastAPI](https://fastapi.tiangolo.com/) for the web framework