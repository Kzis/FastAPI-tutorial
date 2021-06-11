from fastapi import APIRouter
from routers.recommendation.recommendation_model import recommendation_model
from routers.recommendation.jd_central.jd_central_model import jd_central_recommendation
from routers.recommendation.lazada.lazada_model import lazada_recommendation
from routers.recommendation.shopee.shopee_model import shopee_recommendation

router = APIRouter()

router = APIRouter(
    prefix="/recommendation-model",
    tags=["Recommendation"],
    responses={404: {"message": "Not found"}}
)


@router.get("/source/{app_source}")
async def recommendation_route(app_source: str):
    print("recommendation_route")
    model_source = get_model_source(app_source)
    json_output = get_recommendation_model(model_source)
    return json_output


def get_model_source(app_source):
    print("get_model_source")
    source = app_source.lower()
    if source == "shopee": return shopee_recommendation()
    if source == "lazada": return lazada_recommendation()
    if source == "jd_central": return jd_central_recommendation()
    return recommendation_model()


def get_recommendation_model(model):
    print("get_recommendation_model")
    return model.get_recommendation_model()