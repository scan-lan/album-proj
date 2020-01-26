import csv


class Database():

    def __init__(self):
        self.csvPath = "data/albums.csv"
        self.albumDB = []

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
