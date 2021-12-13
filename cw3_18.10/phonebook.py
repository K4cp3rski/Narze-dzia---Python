class Phonebook:

    def __init__(self, *book):
        self.book = dict()

    def print_book(self):
        for a in self.book.keys():
            print("Zapisane numery dla osoby {} to:".format(a), ', '.join(self.book[a]))

    def print_person_numbers(self, person):
        print("Zapisane numery dla osoby {} to:".format(person), ', '.join(self.book[person]))

    def delete_person_number(self, name, number):
        if name not in self.book.keys():
            print("Nie ma takiej osoby w książce telefonicznej.\n")
        else:
            if str(number) not in self.book[f"{name}"]:
                print("Nie ma takiego numeru przypisanego do tej osoby")
            else:
                self.book[f"{name}"].remove(number)
                print("Usunięto numer {} dla osoby {}".format(str(number), name))

    def book_add(self, name, number):
        if name not in self.book.keys():
            self.book[f"{name}"] = [str(number)]
        else:
            if str(number) not in self.book[f"{name}"]:
                self.book[f"{name}"] = self.book[f"{name}"] + [str(number)]


class PhonebookTuple(Phonebook):
    def print_book(self):
        for a in self.book.keys():
            print("Zapisane numery dla osoby {} to:".format(' '.join(tuple(a))), ', '.join(self.book[a]))

    def print_person_numbers(self, person):
        print("Zapisane numery dla osoby {} to:".format(person), ', '.join(self.book[person]))

    def delete_person_number(self, name, number):
        if name not in self.book.keys():
            print("Nie ma takiej osoby w książce telefonicznej.\n")
        else:
            if str(number) not in self.book[name]:
                print("Nie ma takiego numeru przypisanego do tej osoby")
            else:
                self.book[name].remove(number)
                print("Usunięto numer {} dla osoby {}".format(str(number), name))

    def book_add(self, name, number):
        if name not in self.book.keys():
            self.book[name] = [str(number)]
        else:
            if str(number) not in self.book[name]:
                self.book[name] = self.book[name] + [str(number)]


if __name__ == "__main__":
    print("Good Morning Vietnaaaam!")
