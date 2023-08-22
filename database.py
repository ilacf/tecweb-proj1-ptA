import sqlite3
class Database():
    def __init__(self, banco):
        self.banco = banco
        self.conn = sqlite3.connect(banco)
    