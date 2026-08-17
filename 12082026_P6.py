from dataclasses import dataclass


@dataclass
class UserAccount:
    username: str
    age: int

    def __post_init__(self):
        # 1. Type validation
        if not isinstance(self.username, str):
            raise TypeError(f"username must be a string, got {type(self.username).__name__}")
        if not isinstance(self.age, int):
            raise TypeError(f"age must be an int, got {type(self.age).__name__}")

        # 2. Value boundary validation
        if len(self.username) < 3:
            raise ValueError("username must be at least 3 characters long")
        if self.age < 18:
            raise ValueError("User must be at least 18 years old")


# Usage
try:
    # This will fail the value validation check
    bad_user = UserAccount(username='al', age=16)
except ValueError as e:
    print(f"Validation Error: {e}")
    # Output: Validation Error: username must be at least 3 characters long
