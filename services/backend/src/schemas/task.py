from pydantic import BaseModel, ConfigDict


class TaskGetOutput(BaseModel):
    model_config:ConfigDict = ConfigDict(from_attributes=True)
    
    id:int
    name:str
    description:str

class TaskCreate(BaseModel):
    name: str
    description: str

class TaskCreateOutput(BaseModel):
    message: str

class TaskDeleteInput(BaseModel):
    id:int

class TaskDeleteOutput(BaseModel):
    message: str

class TaskUpdateInput(BaseModel):
    id:int
    name:str
    description:str

class TaskUpdateOutput(BaseModel):
    message: str

class ErrorOutput(BaseModel):
    detail: str