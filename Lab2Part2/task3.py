class Student:
    """simulate student"""
    def __init__(self, name, surname, book_number, grades):
        if not isinstance(name, str):
            raise TypeError("type of name should be 'str'")
        if not isinstance(surname, str):
            raise TypeError("type of surname should be 'str'")
        if not isinstance(book_number, int):
            raise TypeError("type of book_number should be 'int'")
        if not isinstance(grades, list):
            raise TypeError("grades should be list")
        for element in grades:
            if not isinstance(element, int):
                raise TypeError("type of grades should be 'int'")
            if element < 0 or element > 12:
                raise ValueError("values of grades should be not more than 12 and not less than 0")
        self.name = name
        self.surname = surname
        self.book_number = book_number
        self.grades = grades

    def average_score(self):
        """count average grade"""
        value = 0.
        for grade in self.grades:
            value += grade
        return value / len(self.grades)


class Group:
    """list of students"""
    def __init__(self, students):
        if not isinstance(students, list):
            raise TypeError("type of students should be 'list'")
        if not students:
            raise ValueError("value of students should be not 'null'")
        self.students = []
        for element in students:
            is_new = True
            for group_student in self.students:
                if element.name == group_student.name and element.surname == group_student.surname:
                    is_new = False
            if is_new and len(self.students) < 20:
                self.students.append(element)

    def add_student(self, student):
        """will add student if he is new in group and number of students is allowable"""
        if not isinstance(student, Student):
            raise TypeError("type of student should be 'Student'")
        if not student:
            raise ValueError("value of student should be not 'null'")
        if len(self.students) >= 20:
            return
        for group_student in self.students:
            if student.name == group_student.name and student.surname == group_student.surname:
                return
        self.students.append(student)


Ann = Student("Ann", "No", 0, [10, 8, 6, 8, 9])
Bogdan = Student("Bogdan", "Yes", 0, [4, 6, 4, 9, 7])
Fill = Student("Fill", "Fill", 0, [10, 6, 11, 11, 8])
Olia = Student("Olia", "Ten", 0, [11, 11, 10, 12, 10])
Anton = Student("Anton", "Igutsckiy", 0, [6, 7, 5, 6, 4])
Bob = Student("Bob", "Armbrocken", 0, [11, 7, 9, 10, 9])
Georgiy = Student("Georgiy", "Chida", 0, [8, 8, 9, 8, 9])
group = Group([Ann, Bogdan, Fill, Olia, Anton, Bob])
group.add_student(Georgiy)
average_scores = {}
for student in group.students:
    average_scores[student] = student.average_score()
students = [key for key, value in sorted(average_scores.items(), key=lambda item: item[1], reverse=True)]
for student in students[:5]:
    print(student.name, student.surname, average_scores[student])
