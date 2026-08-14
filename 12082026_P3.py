from dataclasses import dataclass
from datetime import datetime

@dataclass
class Entity:
    id: int
    created_at: datetime

@dataclass
class UserEntity(Entity):
    username: str
    email: str

# Usage
# Note: Base fields (id, created_at) must be supplied first in order
user = UserEntity(1, datetime.now(), "dev_jane", "jane@example.com")
print(user.id)        # 1
print(user.username)  # "dev_jane"
