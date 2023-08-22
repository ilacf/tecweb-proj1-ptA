import sqlite3
from dataclasses import dataclass

@dataclass
class Note:
    id: int=None
    title: str=None
    content: str=''

class Database():
    def __init__(self, banco):
        self.banco = banco
        self.conn = sqlite3.connect(banco+".db")
        self.cur = self.conn.cursor()

        self.cur.execute("CREATE TABLE IF NOT EXISTS note (id INT PRIMARY KEY, title STRING, content STRING NOT NULL);")

    def add(self, note):
        comando = f'INSERT INTO {self.banco} (title, content) VALUES (\'{note.title}\', \'{note.content}\');'
        print(f'\n\n{comando}\n\n')
        self.cur.execute(comando)