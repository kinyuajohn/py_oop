class OnlineCourse:
    def __init__(self, course, instructor):
        self.course = course
        self.instructor = instructor
        self.students = []

    def enroll_student(self, student):
        self.students.append(student)
        print(f"{student.name} has been enrolled in the {self.course} course.")

    def course_details(self):
        print(f"Course: {self.course.title()}")
        print(f"Instructor: {self.instructor.title()}")
        print("Enrolled Student:")

        count = 1
        for _ in self.students:
            print(f"  {count}. {(student.name).title()}")
            count += 1

    def completed_course(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                print(f"{name} has completed the course!")

        print(f"{name} is not enrolled in this course.")

    def avg_grade(self, student):
        total = sum(student.grades)
        average = total / len(student.grades)
        print(f"The average grade is: {round(average, 1)}")


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades


course_input = input("Enter a course: ").lower()
name = input("Enter an Instructor: ").lower()
course = OnlineCourse(course_input, name)

num_students = int(input("Enter number of students: "))

for _ in range(num_students):
    student_name = input("Enter student name: ").lower()

    grades = []
    for _ in range(3):
        grade = int(input("Enter grade: "))
        grades.append(grade)

    student = Student(student_name, grades)
    course.enroll_student(student)
    course.avg_grade(student)
    print("--------------------------------------")

print("--------------------------------------")
course.course_details()
