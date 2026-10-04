from dataclasses import dataclass

@dataclass 
class Tag:
    offset: int
    length: int
    next_char: str