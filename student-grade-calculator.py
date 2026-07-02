def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"


print("=" * 35)
print("      Student Grade Calculator")
print("=" * 35)

while True:
    try:
        name = input("Enter Student Name: ")

        total_marks = float(input("Enter Total Marks: "))
        obtained_marks = float(input("Enter Obtained Marks: "))

        if total_marks <= 0:
            print("Total marks must be greater than 0.")
            continue

        if obtained_marks < 0 or obtained_marks > total_marks:
            print("Invalid obtained marks.")
            continue

        percentage = (obtained_marks / total_marks) * 100
        grade = calculate_grade(percentage)

        print("\n------ Result ------")
        print(f"Student Name : {name}")
        print(f"Percentage   : {percentage:.2f}%")
        print(f"Grade        : {grade}")
        print("--------------------")

        again = input("\nDo you want to calculate another result? (yes/no): ").lower()

        if again != "yes":
            print("\nThank you for using the Grade Calculator!")
            break

    except ValueError:
        print("Please enter valid numeric values.")