import os
import datetime
from typing import Tuple


class Article:

    name: str
    date: datetime.date
    content: str
    path: str

    def __init__(
            self,
            name: str,
            date: datetime.date,
            content: str,
            path: str):
        self.name = name
        self.date = date
        self.content = content
        self.path = path

    def file_name(self):
        base_name: str = os.path.basename(self.path)
        splitted: Tuple[str, str] = os.path.splitext(base_name)
        return splitted[0]
