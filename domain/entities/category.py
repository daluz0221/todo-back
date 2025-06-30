from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class Category:
    name: str
    is_deleted: bool
    id: UUID = field(default_factory=uuid4)
    user_id: UUID = field(default_factory=uuid4)
    
    def __post_init__(self):
        if not isinstance(self.id, UUID):
            raise TypeError(f"Expected UUID for id, got {type(self.id).__name__}")
        if not isinstance(self.user_id, UUID):
            raise TypeError(f"Expected UUID for user_id, got {type(self.user_id).__name__}")
        if not isinstance(self.name, str):
            raise TypeError(f"Expected str for name, got {type(self.name).__name__}")   