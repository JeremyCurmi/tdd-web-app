class NamedEntityClient():
    def __init__(self, model):
        self.model = model
    
    def get_ents(self, sentence: str) -> dict:
        return {}