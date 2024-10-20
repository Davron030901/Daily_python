student_scores=input("Input a list of student heights: ").split()
for n in range(0,len(student_scores)):
    student_scores[n]=int(student_scores[n])
height_score=0
for score in student_scores:
    if score>height_score:
        height_score=score
print(f"The heights score in the class is:{height_score}")