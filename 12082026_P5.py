from dataclasses import dataclass

@dataclass
class Book:
    title: str
    year: int

    @classmethod
    def from_string(cls, raw_string: str):
        """Parses a string formatted like 'Title, Year'"""
        # 1. Split the string by the comma
        title_part, year_part = raw_string.split(",")

        # 2. Clean up whitespace and convert the year to an integer
        clean_title = title_part.strip()
        clean_year = int(year_part.strip())

        # 3. Instantiate and return the new Book object
        return cls(title=clean_title, year=clean_year)


# ==========================================
# USAGE
# ==========================================

# Standard way
book1 = Book(title="The Fellowship of the Ring", year=1954)
print(book1)  # Book(title='The Fellowship of the Ring', year=1954)

# Using our custom classmethod factory
raw_data = "The Hobbit, 1937"
book2 = Book.from_string(raw_data)
print(book2)  # Book(title='The Hobbit', year=1937)
