class Student:
    def __init__(self, name, address, course):
        self.name = name
        self.address = address
        self.course = course

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Course: {self.course}")

if __name__ == "__main__":
    students = {} 
    students[500200001] = Student("Naham Sec", "Belleville", "Project Management")
    students[500200002] = Student("John Hammond", "Belleville", "CyberSecurity")
    students[500200003] = Student("Nirmal Dahal", "Belleville", "International Business")
    students[500200004] = Student("Suvam Adhikari", "Belleville", "CSTN")
    student_id = int(input("Enter a student ID: "))

    if student_id in students:
        students[student_id].display_info()
    else:
        print(f"Student with ID {student_id} not found.")


