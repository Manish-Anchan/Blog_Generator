from src.states.blog_state import BlogState

class BlogNode:

    def __init__(self, llm):
        self.llm = llm

    def title_creation(self, state:BlogState):

        if "topic" in state and state["topic"]:
            prompt = """
                You are an expert blog content writer. 
                Return ONLY a short, SEO-friendly blog title for the topic: {topic}.
                Do not include subtitles, meta description, tags, or any extra text.
                Output must be a single line of plain text, no markdown formatting.
                """
            
            system_message = prompt.format(topic = state["topic"])
            response = self.llm.invoke(system_message)

            return {"blog" : {"title" : response.content}}
    
    def content_creation(self, state:BlogState):
        
        if "topic" in state and state["topic"]:
            system_prompt = """You are expert blog writer. Use markdown formating.
            Generate a detailed blog content with the detailed breakdown for the {topic}"""
            system_message = system_prompt.format(topic = state["topic"])
            response = self.llm.invoke(system_message)
            return {"blog" : {"title":state["blog"]["title"], "content" :response.content}}