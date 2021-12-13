from phonebook import Phonebook as pb
B1 = pb()
B1.book_add("Ania Kowalska", "787-936-866")
B1.book_add("Ania Kowalska", "787-936-865")
B1.book_add("Olek Zieliński", "787-936-444")
B1.book_add("Ania Kowalska", "787-936-865")
B1.print_person_numbers("Ania Kowalska")
B1.delete_person_number("Ania Kowalska", "787-936-866")
B1.print_person_numbers("Ania Kowalska")
print("\n")
B1.print_book()

if __name__ == "__main__":
    print("Good Morning Vietnaaaam!")
