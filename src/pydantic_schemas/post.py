from pydantic import BaseModel, validator, ValidationError, Field

class Post(BaseModel):
    id: int
    title: str
    # name: str = Field(alias='_name')

    # @validator('id')
    # def check_that_id_is_less_than_two(cls, v):
    #     if v > 2:
    #         raise ValidationError('ID is not less than two')
    #     else:
    #         return v