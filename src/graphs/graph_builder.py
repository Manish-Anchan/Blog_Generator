from langgraph.graph import StateGraph, START, END
from src.LLMs.groq_llm import GroqLLM
from src.states.blog_state import BlogState
from src.nodes.blog_node import BlogNode


class GraphBuilder:
    def __init__(self, llm):
        self.llm = llm
        self.graph = StateGraph(BlogState)

    
    def build_topic_graph(self):

        self.blog_node_obj = BlogNode(self.llm)

        self.graph.add_node("title_creation",self.blog_node_obj.title_creation)
        self.graph.add_node("content_creation", self.blog_node_obj.content_creation)

        self.graph.add_edge(START, "title_creation")
        self.graph.add_edge("title_creation", "content_creation")
        self.graph.add_edge("content_creation", END)

        return self.graph

    def setup_graph(self, usecase):
        if usecase == "topic":
            self.build_topic_graph()

        return self.graph.compile()