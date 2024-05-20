

class PromptEntry:
    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content
    
    def __str__(self) -> str:
        return f"{self.role}: {self.content}"