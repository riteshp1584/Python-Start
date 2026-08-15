from dataclasses import dataclass

@dataclass
class User:
    first_name: str
    last_name: str

    @classmethod
    def from_full_name(cls, full_name: str):
        """Alternative constructor: splits a full name string automatically."""
        # 1. Split the string by space
        first, last = full_name.split(" ")

        # 2. 'cls' represents the User class itself.
        # This line is exactly like calling User(first, last)
        return cls(first_name=first, last_name=last)


# ----------------------------------------------------
# 1. Standard Entrance (Using __init__)
# ----------------------------------------------------
user1 = User(first_name="Jane", last_name="Doe")
print(user1)  # User(first_name='Jane', last_name='Doe')

# ----------------------------------------------------
# 2. Secondary Entrance (Using our @classmethod factory)
# ----------------------------------------------------
# We pass ONE string, and the classmethod builds the object for us
user2 = User.from_full_name("John Smith")
print(user2)  # User(first_name='John', last_name='Smith')
