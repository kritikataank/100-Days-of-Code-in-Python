student_scores = {
    "harry":81,
    "Ron":78,
    "Hermione":99,
    "Draco":74,
    "Neville":62,
}

student_grade = {}

for key in student_scores:
    if student_scores[key] >= 91:
        student_grade[key] = "Outstanding"
    elif student_scores[key] >= 81:
        student_grade[key] = "Exceeds Expectations"
    elif student_scores[key] >= 71:
        student_grade[key] = "Acceptable"
    else:
        student_grade[key] = "Fail"

print(student_grade)