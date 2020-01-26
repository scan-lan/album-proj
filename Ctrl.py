from Album import Album
from Database import Database


class Ctrl():

    def __init__(self):
        """placeholder"""
        self.fieldList = [
            "title",
            "artist",
            "price",
            "date obtained",
            "method of acquisition"
        ]
        self.database = Database()

    def add(self):
        newAlbum = []
        for field in self.fieldList:
            msg = f'\tEnter album {field}:\n\t'
            newAlbum.append(input(msg))
        print(Album(newAlbum.__dict__))
        # self.database.add(Album(newAlbum)) ready soon
