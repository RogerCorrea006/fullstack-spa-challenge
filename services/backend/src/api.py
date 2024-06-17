from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from src.services.task import TaskService
from src.schemas.task import TaskCreate, TaskCreateOutput, TaskGetOutput, TaskDeleteOutput, TaskDeleteInput, TaskUpdateInput, TaskUpdateOutput

task_router = APIRouter(prefix='/task')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@task_router.get('/getTasks', response_model=List[TaskGetOutput])
async def get_tasks():
    try:
        
        

        tasks = await TaskService.get_tasks() 
            
        return tasks
    except Exception as error:
        raise HTTPException(400, message=str(error))

@task_router.post('/createTask', response_model=TaskCreateOutput)
async def create_task(task_input: TaskCreate):
    try:
        await TaskService.create_task(name=task_input.name, description=task_input.description)

        return TaskCreateOutput(message='tarefa criada com sucesso')
    except Exception as error:
        raise HTTPException(400, message=str(error))
    
@task_router.post('/deleteTask', response_model=TaskDeleteOutput)
async def delete_task(task: TaskDeleteInput):
    try:
        await TaskService.delete_task(task_id=task.id)

        return TaskDeleteOutput(message='tarefa deletada com sucesso')
    except Exception as error:
        raise HTTPException(400, message=str(error))
    
@task_router.post('/updateTask', response_model=TaskUpdateOutput)
async def update_task(task: TaskUpdateInput):
    try:
        await TaskService.update_task(task_id=task.id, task_name=task.name, task_description=task.description)

        return TaskUpdateOutput(message='tarefa atualizada com sucesso')
    except Exception as error:
        raise HTTPException(400, message=str(error))  

@app.get("/")
async def index():
    return {"status": "todo api is running"}

app.include_router(task_router)