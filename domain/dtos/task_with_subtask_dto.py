
from dataclasses import dataclass
from typing import List
from uuid import UUID
from datetime import datetime
from domain.entities.subtask import Subtask 

@dataclass
class TaskWithSubTasksDTO:
    id: UUID
    title: str
    description: str
    dificulties: str
    solution: str
    is_completed: bool
    deadline: datetime
    category_id: UUID 
    user_id: UUID
    is_deleted: bool
    progress: float
    created_at: datetime
    last_updated: datetime
    subtasks: List[Subtask]