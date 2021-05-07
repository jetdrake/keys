import csv

class keycodes:
    def __init__(self):
        with open('keycodes.csv', mode='r') as infile:
            reader = csv.reader(infile)
            self.keydict = {rows[0]:rows[1] for rows in reader}