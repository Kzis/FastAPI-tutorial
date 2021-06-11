from routers.recommendation.recommendation_model import recommendation_model


class jd_central_recommendation(recommendation_model):

    def get_recommendation_model(self):
        return {"model": "JD Central"}
