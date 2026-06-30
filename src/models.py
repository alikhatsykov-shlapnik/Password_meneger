from dataclasses import dataclass
from datetime import datetime


@dataclass
class Note:
    id: int
    title: str
    text: str
    created_at: str

    @classmethod
    def create(cls, title: str, text: str) -> "Note":
        "Фабричный метод для создания новой заметки"
        return cls(
            id = 0,
            title = title,
            text = text,
            create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )