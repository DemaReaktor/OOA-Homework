import json
from abc import abstractmethod


class ITeacher:
    """Interface for teacher class"""

    @abstractmethod
    def __init__(self, name: str):
        pass

    @abstractmethod
    def courses(self) -> set:
        pass

    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def add_course(self, course):
        """add courses to teacher"""
        pass


class Teacher(ITeacher):
    """teacher class
    properties:
        name -> name
        courses -> set of courses which are with this teacher
    class property:
     teachers -> dictionary of teachers where keys are names of teachers and values are teacher classes"""
    __teachers = dict()

    def __init__(self, name: str):
        if not isinstance(name, str):
            raise TypeError('name should have type "str"')
        for element in Teacher.__teachers.keys():
            if name == element.name:
                raise ValueError('teacher with this name already exists')
        self.__name = name
        self.__courses = set()
        Teacher.__teachers[name] = self

    @property
    def courses(self) -> set:
        return self.__courses

    @classmethod
    def teachers(cls) -> dict:
        """return dictionary, where keys are names of teachers and values are teacher classes"""
        return cls.__teachers

    @property
    def name(self) -> str:
        return self.__name

    def add_course(self, course):
        """add course to teacher"""
        if not isinstance(course, Course):
            raise TypeError('course should have type "Course"')
        self.__courses.add(course)

    def __str__(self):
        return self.__name


class ICourse:
    """Interface for course"""

    @abstractmethod
    def __init__(self, name: str, teacher: Teacher, program: list):
        pass

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def teacher(self):
        pass

    @abstractmethod
    def program(self):
        pass


class Course(ICourse):
    """course class
    properties:
        name -> name of course
        teacher -> teacher class who is in this course
        program -> list of parts of program"""

    def __init__(self, name: str, teacher: Teacher, program: list):
        if not isinstance(name, str):
            raise TypeError('name should have type "str"')
        if not isinstance(teacher, str) and not isinstance(teacher, Teacher):
            raise TypeError('teacher should have type "str" or "Teacher"')
        if not isinstance(program, list):
            raise TypeError('program should have type "list"')
        self.__name = name
        self.__teacher = teacher if isinstance(teacher, str) else teacher.name
        Teacher.teachers()[self.__teacher].add_course(self)
        self.__program = program

    @property
    def name(self) -> str:
        return self.__name

    @property
    def teacher(self) -> Teacher:
        return Teacher.teachers()[self.__teacher]

    @property
    def program(self) -> list:
        return self.__program

    def __str__(self):
        program = ""
        for element in self.__program:
            program += element + '\n'
        return 'name: ' + self.__name + ', teacher: ' + str(self.__teacher) + ', program: \n' + program


class ICourseFactory:
    """Interface for course factory, where are creating courses and teachers"""

    @abstractmethod
    def create_teacher(self, name: str) -> Teacher:
        pass

    @abstractmethod
    def create_course(self, name: str, program: list, **kwargs) -> Course:
        pass


class CourseFactory(ICourseFactory):
    """factory for creating courses and teachers"""

    @classmethod
    def create_teacher(cls, name: str) -> Teacher:
        """create teacher with this name and without courses"""
        return Teacher(name)

    @classmethod
    def create_course(cls, name: str, program: list, **kwargs) -> Course:
        """create course with name and program
        has attribute 'teacher' where value is name or class of teacher
        if attribute 'teacher' is not written course will get teacher with the smallest count of courses"""
        if 'teacher' in kwargs.keys():
            return Course(name, kwargs['teacher'], program)
        teacher = None
        for element in Teacher.teachers().values():
            if not teacher or len(teacher.courses) > len(element.courses):
                teacher = element
        return Course(name, teacher, program)


class CourseEncoder(json.JSONEncoder):
    """class that can write all teachers and courses into json file
    also can read teachers and courses from json file"""

    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        if isinstance(obj, Teacher) or isinstance(obj, Course):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)

    @classmethod
    def write(cls, file_name: str):
        """write all teachers and courses into json file with this name"""
        with open(file_name, 'w') as file:
            file.write(json.dumps(Teacher.teachers(), cls=CourseEncoder))

    @classmethod
    def read(cls, file_name: str):
        """read teachers with courses from json file with this name"""
        with open(file_name, 'r') as file:
            teacher_dictionary = json.loads(file.read())
            for teacher in teacher_dictionary.values():
                teacher_object = CourseFactory.create_teacher(teacher["_Teacher__name"])
                courses = teacher["_Teacher__courses"]
                for course in courses:
                    teacher_object.add_course(CourseFactory.create_course(course["_Course__name"], \
                                                                          course["_Course__program"], \
                                                                          teacher=course["_Course__teacher"]))


if __name__ == "__main__":
    # teacher = CourseFactory.create_teacher("Bob")
    # print(CourseFactory.create_course("OOP", ["1.start", "2.process", "3.end"]))
    # CourseEncoder.write("teachers.json")

    #

    CourseEncoder.read("teachers.json")
    Bob = Teacher.teachers()["Bob"]
    print(Bob)
