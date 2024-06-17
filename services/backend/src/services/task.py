from src.database.models import Task
from src.database.connection import async_session
from sqlalchemy.future import select
from fastapi import HTTPException

class TaskService:
    async def create_task(name, description):
        async with async_session() as session:
            async with session.begin(): 
                session.add(Task(name=name, description=description))
                await session.commit()

    async def get_tasks():
        async with async_session() as session: 
                result = await session.execute(select(Task))

                tasks = result.scalars().all()

                return tasks
        
    async def delete_task(task_id):
        async with async_session() as session:
            result = await session.execute(select(Task).filter(Task.id == task_id))
            task = result.scalars().first()

            if not task:
                raise Exception('tarefa não encontrada')

            await session.delete(task)
            await session.commit()

    async def update_task(task_id, task_name, task_description):
        async with async_session() as session:
            result = await session.execute(select(Task).filter(Task.id == task_id))
            task = result.scalars().first()

            if not task:
                raise Exception('tarefa não encontrada')

            task.name = task_name
            task.description = task_description
            
            await session.commit()
