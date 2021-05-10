import csv

class keycodes:
    def __init__(self):
        with open('server/tk_keycodes.csv', mode='r') as infile:
            reader = csv.reader(infile)
            self.keydict = {rows[0]:rows[3] for rows in reader}

        print(self.keydict)