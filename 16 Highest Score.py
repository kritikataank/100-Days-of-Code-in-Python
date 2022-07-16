student_scores=input("Enter list of student scores: ").split(" ")
for n in range(0, len(student_scores)):
    student_scores[n]= int(student_scores[n])
print(student_scores)

high = 0
for i in student_scores:
    if i > high:
        high = i
print(f"The highest score is {high}")
