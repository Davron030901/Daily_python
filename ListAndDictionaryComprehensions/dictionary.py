# import random
#
# names=["Alex","Beth","Caroline","Dave","Eleanor",'Freddie']
# student_scores={student:random.randint(1,100) for student in names}
#
# passed_student={student:score for (student,score) in student_scores.item() if score>=60}
# print(passed_student)

# sentence = input()
#
# result={word:len(word) for word in sentence.split()}
# print(result)

#evil() converts correctly formatted string to dict
weather_c=eval(input())
#dictionary comprehension
# weather_f= {print(day,temp) for (day,temp) in weather_c.items()}
weather_f= {day:temp*9/5+32 for (day,temp) in weather_c.items()}
print(weather_f)

