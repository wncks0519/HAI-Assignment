# Student class 생성 
class Student():
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
    def display_info(self):
        print("ID: %d번 / 이름: %s / 나이: %d"%(self.student_id, self.name, self.age))
class Studentmanager():
    def __init__(self):
        self.students = []
    def add_student(self, student):
        self.students.append(student)
    def display_all_students(self):
        for i in self.students:
            i.display_info()

stu1 = Student(1,"김철수",20)
stu2 = Student(2,"이영희",21)
stu3 = Student(3,"박지민",19)
studentsmanager = Studentmanager()
studentsmanager.add_student(stu1)
studentsmanager.add_student(stu2)
studentsmanager.add_student(stu3)
print("현재 등록된 목록:")
studentsmanager.display_all_students()
print()
stu4 = Student(4,"한지수",22)
studentsmanager.add_student(stu4)
print("학번 4번 학생 추가 후:")
studentsmanager.display_all_students()