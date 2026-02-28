# Simple One-Page Python Program
# Student Management Mini App

students = []

def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")
    
    student = {
        "Name": name,
        "Age": age,
        "Grade": grade
    }
    
    students.append(student)
    print("✅ Student added successfully!\n")

def view_students():
    if len(students) == 0:
        print("No students found.\n")
    else:
        print("\n--- Student List ---")
        for i, student in enumerate(students, start=1):
            print(f"{i}. Name: {student['Name']}, Age: {student['Age']}, Grade: {student['Grade']}")
        print()

def delete_student():
    view_students()
    if len(students) == 0:
        return
    
    try:
        num = int(input("Enter student number to delete: "))
        if 1 <= num <= len(students):
            removed = students.pop(num - 1)
            print(f"❌ {removed['Name']} deleted successfully!\n")
        else:
            print("Invalid number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
