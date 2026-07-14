from pydantic import BaseModel,Field

class RestaurantQuery(BaseModel):
    cuisine:str=""
    budget:int|None=Field(
        default=None,
        ge=0
    )
    area:str=""