student_heights=input("Input a list of student heights: ").split()
for n in range(0,len(student_heights)):
    student_heights[n]=int(student_heights[n])
total_height=0
for height in student_heights:
    total_height+=height
numer_of_height=0
for student in student_heights:
    numer_of_height+=1
print(round(total_height/numer_of_height))