import csv


class Database():

    def __init__(self):
        self.csvPath = "data/albums.csv"
        self.albumDB = []

    def add(self):

        with open(self.csvPath, "a") as albums:
            writer = csv.writer(albums)
            writer.writeRow()

    def show(self):
        with open(self.csvPath, "r") as albums:
            reader = csv.reader(self.csvPath)
            for line in reader:
                print(line)
