
from dataclasses import dataclass
from typing import List
from uuid import UUID
from datetime import datetime
from domain.entities.task import Task 

@dataclass
class CategoryWithTasksDTO:
    id: UUID
    name: str
    user_id: UUID
    is_deleted: bool
    created_at: datetime
    last_updated: datetime
    tasks: List[Task]