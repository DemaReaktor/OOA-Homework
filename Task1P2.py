from abc import abstractmethod


class ITeacher:
    @abstractmethod
    def __init__(self, name):
        pass

    @abstractmethod
    @property
    def courses(self):
        pass

    @abstractmethod
    @property
    def name(self):
        pass

    @abstractmethod
    def add_course(self, course):
        pass


class Teacher(ITeacher):
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError('name should have type "str"')
        self.__name = name
        self.__courses = set()

    @property
    def courses(self):
        return self.__courses

    @property
    def name(self):
        return self.__name

    def add_course(self, course):
        if not isinstance(course, Course):
            raise TypeError('course should have type "Course"')
        self.__courses.add(course)


class ICourse:
    @abstractmethod
    def __init__(self, name, teacher, program):
        pass

    @abstractmethod
    @property
    def name(self):
        pass

    @abstractmethod
    @property
    def teacher(self):
        pass

    @abstractmethod
    @property
    def program(self):
        pass


class Course(ICourse):
    def __init__(self, name, teacher, program):
        if not isinstance(name, str):
            raise TypeError('name should have type "str"')
        if not isinstance(teacher, Teacher):
            raise TypeError('teacher should have type "Teacher"')
        if not isinstance(program, list):
            raise TypeError('program should have type "list"')
        self.__name = name
        self.__teacher = teacher
        self.__teacher.add_course(self)
        self.__program = program

    @property
    def name(self):
        return self.__name

    @property
    def teacher(self):
        return self.__teacher

    @property
    def program(self):
        return self.__program


class ICourseFactory:
    @abstractmethod
    def create_teacher(self, name):
        pass

    @abstractmethod
    def create_course(self, name, teacher, program):
        pass


class CourseFactory(ICourseFactory):
    @classmethod
    def create_teacher(cls, name):
        return Teacher(name)

    @classmethod
    def create_course(cls, name, teacher, program):
        return Course(name, teacher, program)
