from dataclasses import dataclass, field
from uuid import UUID, uuid4

@dataclass
class Subtask:
    title: str
    is_completed: bool
    is_deleted: bool
    id: UUID = field(default_factory=uuid4)
    task_id: UUID = field(default_factory=uuid4)
    
    
    def __post_init__(self):
        if not isinstance(self.id, UUID):
            raise TypeError(f"Expected UUID for id, got {type(self.id).__name__}")
        if not isinstance(self.task_id, UUID):
            raise TypeError(f"Expected UUID for task_id, got {type(self.task_id).__name__}")
        if not isinstance(self.title, str):
            raise TypeError(f"Expected str for title, got {type(self.title).__name__}")
        if not isinstance(self.is_completed, bool):
            raise TypeError(f"Expected bool for is_completed, got {type(self.is_completed).__name__}")          