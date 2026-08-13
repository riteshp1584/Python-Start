from dataclasses import dataclass, field

@dataclass
class BlogPost:
    title: str
    content: str
    # Ensures every instance gets its own independent list
    tags: list[str] = field(default_factory=list)

# Usage
post1 = BlogPost("Python Tips", "Use dataclasses.")
post2 = BlogPost("AI Trends", "LLMs are changing dev.")

post1.tags.append("programming")
print(post1.tags)  # ['programming']
print(post2.tags)  # [] (Unaffected)
