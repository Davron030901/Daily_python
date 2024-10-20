# programming_dictionary={"Bug":"A moth",
#                         "dictionarry":"Amodhfh"}
# programming_dictionary["Bug"]="dshchschscjf"
# #print(programming_dictionary["Bug"])
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])
student_scores={
    "Harry":81,
    "Ron":78,
    "Hermione":99,
    "Draco":74,
    "Neville":62
}
student_grades={}
for student in student_scores:
    score=student_scores[student]
    if score>90:
        student_grades[student]="Outsanding"
    elif score>80:
        student_grades[student]="Exceeds Expectations"
    elif score>70:
        student_grades[student]="Acceptable"
    else:
        student_grades[student]="Fail"

print(student_grades)