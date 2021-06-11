from routers.recommendation.recommendation_model import recommendation_model


class lazada_recommendation(recommendation_model):

    def get_recommendation_model(self):
        return {"model": "Lazada"}
