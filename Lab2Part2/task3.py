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
        self.__name = name
        self.__surname = surname
        self.__book_number = book_number
        self.__grades = grades

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def book_number(self):
        return self.__book_number

    @property
    def grades(self):
        return self.__grades

    @book_number.setter
    def book_number(self, value):
        if not isinstance(value, int):
            raise TypeError("type of book_number should be 'int'")
        if not value <= 0:
            raise ValueError('value of book_number should be more than 0')
        self.__book_number = value

    def add_grade(self, value):
        """add grade into student`s grades"""
        if not isinstance(value, int):
            raise TypeError("type of grade should be 'int'")
        if value < 0 or value > 12:
            raise ValueError("value of grade should be not more than 12 and not less than 0")
        self.__grades.append(value)

    def remove_grade(self, value):
        """will remove grade from student`s grades if there is this grade"""
        if not isinstance(value, int):
            raise TypeError("type of grade should be 'int'")
        if value < 0 or value > 12:
            raise ValueError("value of grade should be not more than 12 and not less than 0")
        for element in self.__grades:
            if element == value:
                self.__grades.pop(value)
                return
        raise ValueError('student does not have this grade')

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
        for element in students:
            if not isinstance(element, Student):
                raise TypeError("every element should have type 'Student'")
        self.__students = []
        for element in students:
            self.add_student(element)

    @property
    def students(self):
        return self.__students

    def add_student(self, student):
        """will add student if he is new in group and number of students is allowable"""
        if not isinstance(student, Student):
            raise TypeError("type of student should be 'Student'")
        if not student:
            raise ValueError("value of student should be not 'null'")
        if len(self.__students) >= 20:
            raise ValueError('group is full')
        for group_student in self.__students:
            if student.name == group_student.name and student.surname == group_student.surname:
                raise ValueError('student already exists in this group')
        self.__students.append(student)

    def remove_student(self, student):
        """will remove student from group is there he is"""
        if not isinstance(student, Student):
            raise TypeError("type of student should be 'Student'")
        if not student:
            raise ValueError("value of student should be not 'null'")
        for group_student in self.__students:
            if student.name == group_student.name and student.surname == group_student.surname:
                self.__students.pop(student)
                return
        raise ValueError('student does not exist in this group')


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
