from datetime import *

class NoteData():
    def __init__(self):
        self.notes = []

    def add_note(self, text, category):
        note = {}
        note['date'] = datetime.now()
        note['text'] = text
        note['category'] = category
        self.notes.append(note)

    def get_categories(self):
        cats = set()
        for n in self.notes:
            cats.add(n['category'])
        return list(cats)

    def get_notes(self, category = None):
        res = None
        if category is None:
            res = self.notes
        else:
            notes = []
            for n in self.notes:
                if n['category'] == category:
                    notes.append(n)
            res = notes
        return res

    def delete_note(self, date):
        #Datoformatet kan være anderledes på forskellige computere,
        # derfor specificeres det her.
        d = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
        for n in self.notes:
            if n['date'] == d:
                self.notes.remove(n)


if __name__ == '__main__':
    data = NoteData()
    data.add_note("her", "random")
    data.add_note("en note", "random")
    data.add_note("golf", "Sports")
    data.add_note("tennis", "Sports")

    print(data.get_categories())
    print(data.get_notes('Sports'))

#Opgaver:
#Persistens med pickle?
#Vis noter i tidsinterval
#Flere faner?
#Dialogbokse
