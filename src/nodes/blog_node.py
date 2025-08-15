from src.states.blog_state import BlogState, Blog
from langchain_core.messages import HumanMessage

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
        
    
    def translation(self,state:BlogState):
        """
        Translate the content to the specified language.
        """
        translation_title_prompt = """
            Translate the following blog title into {current_language}.

            IMPORTANT:
            - Output MUST be ONLY the translated title.
            - Do not include explanations, alternatives, or additional text.
            - Do not include quotes or phrases like "The translation is".
            - Just return the translated title exactly as it should appear.

            ORIGINAL TITLE:
            {blog_title}
            """
        
        translation_content_prompt="""
        Translate the following content into {current_language}.
        - Maintain the original tone, style, and formatting.
        - Adapt cultural references and idioms to be appropriate for {current_language}.

        ORIGINAL CONTENT:
        {blog_content}

        """

        print(state["current_language"])
        blog_content=state["blog"]["content"]
        blog_title = state["blog"]["title"]
        title_messages=[
            HumanMessage(translation_title_prompt.format(current_language=state["current_language"], blog_title=blog_title))

        ]
        content_messages=[
            HumanMessage(translation_content_prompt.format(current_language=state["current_language"], blog_content=blog_content))

        ]
        translated_title = self.llm.invoke(title_messages)
        translated_content = self.llm.invoke(content_messages)
        return {"blog": {"title":translated_title.content, "content" : translated_content.content}}

    def route(self, state: BlogState):
        return {"current_language": state['current_language'] }
    

    def route_decision(self, state: BlogState):
        """
        Route the content to the respective translation function.
        """
        if state["current_language"] == "hindi":
            return "hindi"
        elif state["current_language"] == "french": 
            return "french"
        else:
            return state['current_language']
            