student_heights=input("Enter list of student height: ").split(" ")
for n in range(0, len(student_heights)):
    student_heights[n]= int(student_heights[n])
print(student_heights)

sum = 0
l =0 

for i in student_heights:
    sum += i
    l +=1
avg = round(sum/l)
print(avg)
