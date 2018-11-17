class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return "Name: {}, Score: {}".format(self.name, self.score)

student_list = []

bukki = Student('Philip Bukki', 67)
james = Student('James Smart', 75)
jane = Student('Jane Phil', 84)
john = Student('John Bat', 54)
dan = Student('Dan Hiller', 67)
karen = Student('Karen', 87)

student_list.append(bukki)
student_list.append(james)
student_list.append(jane)
student_list.append(john)
student_list.append(dan)
student_list.append(karen)

# Function that returns the highest student

def grade_students(stud_list):
    highest_score = stud_list[0].score
    highest_student = stud_list[0]
    for student in stud_list:
        if student.score > highest_score:
            highest_score = student.score
            highest_student = student
    return highest_student

highest = grade_students(student_list)

print(highest)