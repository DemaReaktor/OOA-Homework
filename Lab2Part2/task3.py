# class Student:
#     def __init__(self, name="", surname="", book_number=0, grades=[]):
#         self.name = name
#         self.surname = surname
#         self.book_number = book_number
#         self.grades = grades
#
#
# class Group:
#     def __init__(self, students={Student()}):
#         self.students = students
#
#
# def average_score(student=Student()):
#     value = 0.
#     for grade in student.grades:
#         value += grade
#     try:
#         return value / float(len(student.grades))
#     except Exception as exception:
#         return 0.
#
#
# Ann = Student("Ann", "No", 0, [10, 8, 6, 8, 9])
# Bogdan = Student("Bogdan", "Yes", 0, [4, 6, 4, 9, 7])
# Fill = Student("Fill", "Fill", 0, [10, 6, 11, 11, 8])
# Olia = Student("Olia", "Ten", 0, [11, 11, 10, 12, 10])
# Anton = Student("Anton", "Igutsckiy", 0, [6, 7, 5, 6, 4])
# Bob = Student("Bob", "Armbrocken", 0, [11, 7, 9, 10, 9])
# Georgiy = Student("Georgiy", "Chida", 0, [8, 8, 9, 8, 9])
# group = Group({Ann, Bogdan, Fill, Olia, Anton, Bob, Georgiy})
# average_scores = list(map(average_score(), group.students))
# # average_scores = list(map(operator.,) map(average_score(), group.students))
# student_score = {}
# for index in range(0, len(group.students)):
#     student_score += {group.students[index], average_scores[index]}
# student_score.sort()
# print(student_score[:4])
#
