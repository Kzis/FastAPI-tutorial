from routers.recommendation.recommendation_model import recommendation_model


class shopee_recommendation(recommendation_model):

    def get_recommendation_model(self):
        return {"model": "Shopee"}
