# STUDENT GRADE MANAGEMENT AND PERFORMANCE ANALYZER

# FUNCTION: Determine Letter Grade
def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

# FUNCTION: Determine Academic Status
def get_status(average, attendance):
    # Logical AND operator
    if average >= 75 and attendance >= 80:
        return "PASSED"

    # Logical OR operator
    elif average < 75 or attendance < 80:
        return "FAILED"

# FUNCTION: Determine Performance Description
def get_performance(average):
    if average >= 95:
        return "Outstanding"

    elif average >= 90:
        return "Excellent"

    elif average >= 85:
        return "Very Good"

    elif average >= 80:
        return "Good"

    elif average >= 75:
        return "Satisfactory"

    elif average >= 60:
        return "Needs Improvement"

    else:
        return "Poor"


# FUNCTION: Validate Grade
def get_valid_grade(subject):
    while True:
        grade = float(input(f"Enter grade in {subject} (0-100): "))

        # Range checking
        if 0 <= grade <= 100:
            return grade
        else:
            print("Invalid grade!")
            print("Grade must be between 0 and 100.\n")

# FUNCTION: Validate Attendance
def get_valid_attendance():
    while True:
        attendance = float(input("Enter attendance percentage (0-100): "))

        if 0 <= attendance <= 100:
            return attendance
        else:
            print("Invalid attendance percentage!\n")

# MAIN PROGRAM

print("=" * 65)
print("     STUDENT GRADE MANAGEMENT AND PERFORMANCE ANALYZER")
print("=" * 65)


# Ask number of students
while True:
    number_of_students = int(
        input("\nHow many students do you want to process? ")
    )

    if number_of_students > 0:
        break

    print("Number of students must be greater than zero.")

# Class statistics variables

total_class_average = 0

passed_students = 0
failed_students = 0

highest_average = 0
lowest_average = 101

highest_student = ""
lowest_student = ""

excellent_students = 0

# FOR LOOP - PROCESS MULTIPLE STUDENTS
for student_number in range(1, number_of_students + 1):
    print("\n" + "=" * 65)
    print(f"STUDENT #{student_number}")
    print("=" * 65)

    name = input("Enter student name: ").strip().title()

    # Subject Grades
    programming = get_valid_grade("Programming")
    database = get_valid_grade("Database")
    mathematics = get_valid_grade("Mathematics")
    networking = get_valid_grade("Networking")
    web_development = get_valid_grade("Web Development")

    # Attendance
    attendance = get_valid_attendance()

    # Calculate Average
    # Arithmetic Operators
    total_grade = (
        programming
        + database
        + mathematics
        + networking
        + web_development
    )

    average = total_grade / 5

    # Determine Grade and Status

    letter_grade = get_letter_grade(average)

    status = get_status(
        average,
        attendance
    )

    performance = get_performance(average)

    # Determine Scholarship Eligibility
    if average >= 90 and attendance >= 90:
        scholarship = "QUALIFIED"
    else:
        scholarship = "NOT QUALIFIED"

    # Determine Academic Warning
    academic_warning = False

    if average < 75 or attendance < 80:
        academic_warning = True

    # Count Passed / Failed

    if status == "PASSED":
        passed_students += 1
    else:
        failed_students += 1

    # Count Excellent Students

    if average >= 90:
        excellent_students += 1

    # Find Highest Student

    if average > highest_average:
        highest_average = average
        highest_student = name

    # Find Lowest Student

    if average < lowest_average:
        lowest_average = average
        lowest_student = name

    # Add average to class total
    total_class_average += average

    # INDIVIDUAL STUDENT REPORT

    print("\n" + "-" * 65)
    print("STUDENT PERFORMANCE REPORT")
    print("-" * 65)
    print(f"Student Name       : {name}")
    print("\nSUBJECT GRADES")
    print(f"Programming        : {programming:.2f}")
    print(f"Database           : {database:.2f}")
    print(f"Mathematics        : {mathematics:.2f}")
    print(f"Networking         : {networking:.2f}")
    print(f"Web Development    : {web_development:.2f}")

    print("-" * 65)
    print(f"Average            : {average:.2f}")
    print(f"Letter Grade       : {letter_grade}")
    print(f"Performance        : {performance}")
    print(f"Attendance         : {attendance:.2f}%")
    print(f"Academic Status    : {status}")
    print(f"Scholarship        : {scholarship}")

    # Nested Selection

    if academic_warning:
        print("\nACADEMIC WARNING:")
        if average < 75 and attendance < 80:
            print(
                "Student has both low grades "
                "and low attendance."
            )

        elif average < 75:
            print(
                "Student needs to improve "
                "academic performance."
            )

        elif attendance < 80:
            print(
                "Student needs to improve "
                "class attendance."
            )

    else:
        print("\nNo academic warning.")

    # Subject Analysis
    print("\nSUBJECT PERFORMANCE ANALYSIS")

    subject_names = [
        "Programming",
        "Database",
        "Mathematics",
        "Networking",
        "Web Development"
    ]

    subject_grades = [
        programming,
        database,
        mathematics,
        networking,
        web_development
    ]

    # Nested for loop
    for i in range(len(subject_names)):
        if subject_grades[i] >= 90:
            remark = "Excellent"
        elif subject_grades[i] >= 75:
            remark = "Passed"
        else:
            remark = "Needs Improvement"

        print(
            f"{subject_names[i]:20} "
            f"{subject_grades[i]:6.2f} "
            f"{remark}"
        )

# CLASS SUMMARY

class_average = total_class_average / number_of_students
pass_percentage = (
    passed_students / number_of_students
) * 100

fail_percentage = (
    failed_students / number_of_students
) * 100

print("\n\n" + "=" * 65)
print("                    CLASS SUMMARY")
print("=" * 65)
print(f"Total Students       : {number_of_students}")
print(
    f"Passed Students      : "
    f"{passed_students}"
)

print(
    f"Failed Students      : "
    f"{failed_students}"
)

print(
    f"Pass Percentage      : "
    f"{pass_percentage:.2f}%"
)

print(
    f"Failure Percentage   : "
    f"{fail_percentage:.2f}%"
)

print(
    f"Excellent Students   : "
    f"{excellent_students}"
)

print(
    f"Class Average        : "
    f"{class_average:.2f}"
)

print(
    f"Highest Average      : "
    f"{highest_average:.2f}"
)

print(
    f"Top Student          : "
    f"{highest_student}"
)

print(
    f"Lowest Average       : "
    f"{lowest_average:.2f}"
)

print(
    f"Lowest Student       : "
    f"{lowest_student}"
)

# OVERALL CLASS PERFORMANCE
print("\nOVERALL CLASS PERFORMANCE:")
if class_average >= 90:
    print("Excellent Class Performance")
elif class_average >= 80:
    print("Very Good Class Performance")
elif class_average >= 75:
    print("Satisfactory Class Performance")
else:
    print("Class Performance Needs Improvement")

print("\n" + "=" * 65)
print("               END OF PROGRAM")
print("=" * 65)