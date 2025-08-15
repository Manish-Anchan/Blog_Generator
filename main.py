import streamlit as st
import os
from dotenv import load_dotenv
from src.graphs.graph_builder import GraphBuilder
from src.LLMs.groq_llm import GroqLLM
import time
import markdown
from io import BytesIO

# Load environment variables
load_dotenv()

# Set up the page config
st.set_page_config(
    page_title="AI Blog Generator",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    
    .success-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
        margin: 1rem 0;
    }
    
    .info-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        color: #0c5460;
        margin: 1rem 0;
    }
    
    .stButton > button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        border: none;
        padding: 0.75rem;
        border-radius: 0.5rem;
        font-weight: bold;
    }
    
    .stButton > button:hover {
        background-color: #0d5aa7;
        border: none;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'generated_blog' not in st.session_state:
    st.session_state.generated_blog = None
if 'generation_history' not in st.session_state:
    st.session_state.generation_history = []

def initialize_llm():
    """Initialize the LLM and return it"""
    try:
        os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "")
        groqllm = GroqLLM()
        return groqllm.get_llm()
    except Exception as e:
        st.error(f"Error initializing LLM: {str(e)}")
        st.error("Please check your API keys in the .env file")
        return None

def generate_blog(topic, language=None):
    """Generate blog using the LangGraph workflow"""
    llm = initialize_llm()
    if not llm:
        return None
    
    try:
        graph_builder = GraphBuilder(llm)
        
        if topic and language:
            graph = graph_builder.setup_graph(usecase="language")
            state = graph.invoke({"topic": topic, "current_language": language.lower()})
        elif topic:
            graph = graph_builder.setup_graph(usecase="topic")
            state = graph.invoke({"topic": topic})
        else:
            return None
            
        return state
    except Exception as e:
        st.error(f"Error generating blog: {str(e)}")
        return None

def save_to_history(topic, language, blog_data):
    """Save generated blog to session history"""
    history_item = {
        'timestamp': time.strftime("%Y-%m-%d %H:%M:%S"),
        'topic': topic,
        'language': language if language else 'English',
        'title': blog_data.get('blog', {}).get('title', 'No title'),
        'content': blog_data.get('blog', {}).get('content', 'No content')
    }
    st.session_state.generation_history.append(history_item)
    # Keep only last 10 items
    if len(st.session_state.generation_history) > 10:
        st.session_state.generation_history.pop(0)

def create_download_link(content, filename, file_type="markdown"):
    """Create a download link for the blog content"""
    if file_type == "markdown":
        file_data = content.encode('utf-8')
        mime_type = "text/markdown"
    else:  # txt
        file_data = content.encode('utf-8')
        mime_type = "text/plain"
    
    return st.download_button(
        label=f"📥 Download as {file_type.upper()}",
        data=file_data,
        file_name=filename,
        mime=mime_type,
        key=f"download_{file_type}"
    )

# Main App Layout
def main():
    # Header
    st.markdown('<h1 class="main-header">🤖 AI Blog Generator</h1>', unsafe_allow_html=True)
    st.markdown("---")
    
    # Sidebar
    with st.sidebar:
        st.header("🔧 Configuration")
        
        # API Status Check
        if os.getenv("GROQ_API_KEY") and os.getenv("LANGCHAIN_API_KEY"):
            st.markdown('<div class="success-box">✅ API Keys Configured</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="info-box">⚠️ Please configure API keys in .env file</div>', unsafe_allow_html=True)
        
        st.subheader("📊 Generation History")
        if st.session_state.generation_history:
            for i, item in enumerate(reversed(st.session_state.generation_history[-5:])):
                with st.expander(f"{item['timestamp']} - {item['language']}"):
                    st.write(f"**Topic:** {item['topic']}")
                    st.write(f"**Title:** {item['title'][:50]}...")
        else:
            st.write("No blogs generated yet.")
        
        if st.button("🗑️ Clear History"):
            st.session_state.generation_history = []
            st.rerun()
    
    # Main Content Area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("📝 Blog Generation")
        
        # Input Form
        with st.form("blog_form"):
            topic = st.text_area(
                "Enter your blog topic:",
                height=100,
                placeholder="e.g., The Future of Artificial Intelligence, Climate Change Solutions, Digital Marketing Trends..."
            )
            
            language_option = st.selectbox(
                "Select language (optional):",
                ["None (English)", "Hindi", "French"],
                index=0
            )
            
            # Convert language selection
            language = None
            if language_option == "Hindi":
                language = "hindi"
            elif language_option == "French":
                language = "french"
            
            col_btn1, col_btn2 = st.columns([1, 1])
            with col_btn1:
                generate_btn = st.form_submit_button("🚀 Generate Blog", use_container_width=True)
            with col_btn2:
                if st.form_submit_button("📋 Use Example", use_container_width=True):
                    st.session_state.example_topic = "The Impact of Machine Learning on Modern Healthcare"
        
        # Handle example topic
        if 'example_topic' in st.session_state:
            topic = st.session_state.example_topic
            del st.session_state.example_topic
            st.rerun()
        
        # Generate blog
        if generate_btn and topic:
            with st.spinner("🔄 Generating your blog... This may take a moment."):
                progress_bar = st.progress(0)
                for i in range(100):
                    time.sleep(0.02)
                    progress_bar.progress(i + 1)
                
                result = generate_blog(topic, language)
                
                if result:
                    st.session_state.generated_blog = result
                    save_to_history(topic, language_option, result)
                    st.success("✅ Blog generated successfully!")
                    progress_bar.empty()
                    st.rerun()
                else:
                    st.error("❌ Failed to generate blog. Please try again.")
                    progress_bar.empty()
        
        elif generate_btn and not topic:
            st.warning("⚠️ Please enter a topic first!")
    
    with col2:
        st.header("📖 Generated Blog")
        
        if st.session_state.generated_blog:
            blog_data = st.session_state.generated_blog
            blog_info = blog_data.get('blog', {})
            
            # Display blog metadata
            st.subheader("📋 Blog Details")
            col_meta1, col_meta2 = st.columns([1, 1])
            with col_meta1:
                st.write(f"**Topic:** {blog_data.get('topic', 'N/A')}")
            with col_meta2:
                current_lang = blog_data.get('current_language', 'english')
                lang_display = current_lang.title() if current_lang != 'english' else 'English'
                st.write(f"**Language:** {lang_display}")
            
            # Display title
            if blog_info.get('title'):
                st.subheader("📌 Title")
                st.markdown(f"**{blog_info['title']}**")
            
            # Display content
            if blog_info.get('content'):
                st.subheader("📄 Content")
                
                # Content display options
                display_option = st.radio(
                    "Display format:",
                    ["Rendered Markdown", "Raw Markdown"],
                    horizontal=True
                )
                
                if display_option == "Rendered Markdown":
                    st.markdown(blog_info['content'])
                else:
                    st.code(blog_info['content'], language='markdown')
                
                # Download options
                st.subheader("💾 Download Options")
                col_dl1, col_dl2 = st.columns([1, 1])
                
                with col_dl1:
                    # Clean title for filename
                    safe_title = "".join(c for c in blog_info.get('title', 'blog') if c.isalnum() or c in (' ', '-', '_')).rstrip()
                    safe_title = safe_title.replace(' ', '_')[:50]
                    
                    create_download_link(
                        f"# {blog_info.get('title', 'Blog Title')}\n\n{blog_info['content']}", 
                        f"{safe_title}.md",
                        "markdown"
                    )
                
                with col_dl2:
                    # Convert markdown to plain text for txt download
                    plain_content = f"{blog_info.get('title', 'Blog Title')}\n\n{blog_info['content']}"
                    create_download_link(
                        plain_content,
                        f"{safe_title}.txt",
                        "txt"
                    )
        
        else:
            st.info("👆 Generate a blog to see it here!")
            st.markdown("""
            ### 🌟 Features:
            - **Smart Content Generation**: AI-powered blog creation
            - **Multi-language Support**: Hindi and French translation
            - **SEO-Optimized Titles**: Search engine friendly titles
            - **Markdown Formatting**: Rich text formatting
            - **Download Options**: Save as MD or TXT files
            - **Generation History**: Track your created blogs
            """)

# Footer
def show_footer():
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: #666; padding: 1rem;'>
            🤖 Powered by LangGraph • Built with Streamlit • 
            <a href='https://github.com/yourusername/blog-generator' target='_blank'>View Source</a>
        </div>
        """, 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
    show_footer()