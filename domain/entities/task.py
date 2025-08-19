from typing import Optional
from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4

@dataclass
class Task:
    title: str
    description: Optional[str] = None
    is_completed: bool = False
    is_deleted: bool = False
    dificulties: Optional[str] = None
    solution: Optional[str] = None
    deadline: Optional[datetime] = None
    id: UUID = field(default_factory=uuid4)
    category_id: UUID = field(default_factory=uuid4)
    user_id: UUID = field(default_factory=uuid4)
    progress: float = 0.0

    def __post_init__(self):
        if not isinstance(self.id, UUID):
            raise TypeError(f"Expected UUID for id, got {type(self.id).__name__}")
        if not isinstance(self.category_id, UUID):
            raise TypeError(f"Expected UUID for category_id, got {type(self.category_id).__name__}")
        if not isinstance(self.title, str):
            raise TypeError(f"Expected str for title, got {type(self.title).__name__}")
        if not isinstance(self.description, str):
            raise TypeError(f"Expected str for description, got {type(self.description).__name__}")
        if not isinstance(self.is_completed, bool):
            raise TypeError(f"Expected bool for is_completed, got {type(self.is_completed).__name__}")

    def __str__(self):
        return f"Task(id={self.id}, category_id={self.category_id}, title='{self.title}', description='{self.description}', is_completed={self.is_completed})"

