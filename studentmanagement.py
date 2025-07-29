class Students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.percentage = self.calculate_percentage()

    def calculate_percentage(self):
        total = sum(self.marks.values())
        return round((total / (len(self.marks) * 100)) * 100, 2)


class StudentManager:
    def __init__(self):
        self.student_list = []

    def add_student(self, name, marks):
        student = Students(name, marks)
        self.student_list.append(student)

    def find_topper(self):
        if not self.student_list:
            print("No students added yet.")
            return
        topper = max(self.student_list, key=lambda x: x.percentage)
        print(f"Topper is {topper.name} with {topper.percentage}%")

    def individual_status(self):
        if not self.student_list:
            print("No students added yet.")
            return
        name = input("Enter student name to view status: ")
        sorted_list = sorted(self.student_list, key=lambda x: x.percentage, reverse=True)
        found = False
       
        idx=1
        for student in sorted_list:
            if student.name == name:
                print(f"Name: {student.name}")
                print(f"Marks: {student.marks}")
                print(f"Percentage: {student.percentage}%")
                print(f"Rank: {idx}")
                idx=idx+1
                found = True
                break
        if not found:
            print("Student not found")


manager = StudentManager()

while True:
    print("MAIN MENU")
    print("1. Add new student")
    print("2. View status")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        os = int(input("Enter OS marks out of 100: "))
        ca = int(input("Enter CA marks out of 100: "))
        ds = int(input("Enter DS marks out of 100: "))
        marks = {"OS": os, "CA": ca, "DS": ds}
        manager.add_student(name, marks)
        print("Student added successfully")
   

    elif choice == '2':
        while True:
            print("STATUS MENU")
            print("1. View Topper")
            print("2. Individual Student Status")
            print("3. Back to Main Menu")
            sub_choice = input("Enter your choice: ")

            if sub_choice == '1':
                manager.find_topper()
            elif sub_choice == '2':
                manager.individual_status()
            elif sub_choice == '3':
                break
            else:
                print("Invalid choice. Try again.")

    elif choice == '3':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again")
