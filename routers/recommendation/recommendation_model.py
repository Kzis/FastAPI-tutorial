class recommendation_model:

    def __init__(self, user_id):
        self.user_id = user_id

    def get_recommendation_model(self):
        return {"model": "Default"}
