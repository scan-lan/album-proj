import csv
import os


class Database():

    def __init__(self, fieldList):
        self.fieldList = fieldList
        self.csvPath = "data/albums.csv"
        self.checkFile()

    def checkFile(self):
        if os.stat(self.csvPath).st_size != 0:
            with open(self.csvPath, "r") as readAlbums:
                reader = csv.reader(readAlbums)
                topRow = next(reader)
                if topRow == self.fieldList:
                    return
        with open(self.csvPath, "w") as writeAlbum:
            csv.DictWriter(
                writeAlbum,
                self.fieldList).writeheader()

    def add(self, album):
        with open(self.csvPath, "a", newline="") as albums:
            writer = csv.writer(albums)
            writer.writerow([
                album.title,
                album.artist,
                album.price,
                album.dateObtained,
                album.acquisitionMethod
            ])

    def show(self):
        with open(self.csvPath, "r") as albums:
            reader = csv.reader(self.csvPath)
            for line in reader:
                print(line)
