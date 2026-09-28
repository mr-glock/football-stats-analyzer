def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    else:
        "Needs improvement"
def get_average(score1 , score2 , score3):
    return (score1 + score2 + score3) / 3
def get_highest(score1, score2, score3,):
    return max(score1, score2, score3)

def get_lowest(score1, score2, score3):
    return min(score1, score2, score3)

students = []

for i in range(3):

    name = input("Enter student's name:")
    score1 = float(input("Enter first score:"))
    score2 = float(input("Enter second score:"))
    score3 = float(input("Enter third score:"))
    highest = get_highest(score1 , score2, score3)
    lowest = get_lowest(score1, score2, score3)
    average = get_average(score1 ,score2 ,score3)
    grade = get_grade(average)
    print(f"{name}'s average is {average}")
    print(f"{name} got a {grade}")
    print(f"Highest score : {highest}")
    print(f"lowest score: {lowest}")
    students.append({
        "name": name,
        "average": average, 
        "grade": grade, 
        "highest": highest,
        "lowest": lowest,
    })
highest_average = 0
highest_student = ""

for student in students:
    if student["average"] > highest_average:
        highest_average = student["average"]
        highest_student = student["name"]
    print(f"{student['name']} - {student['grade']} - {student['average']}")
print(f"Top student: {highest_student}")
print(f"Highest average: {highest_average}")

lowest_average = float("inf")
lowest_student = ""
for student in students:
    if student["average"] < lowest_average:
        lowest_average = student["average"]
        lowest_student = student["name"]
print(f" Lowest studnet:, {lowest_student}")
print(f"lowest average:, {lowest_average}")
