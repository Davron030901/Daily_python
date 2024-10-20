import random
names_string=input('Give me verybody\'s names, sperated by a camera.')
names=names_string.split(', ')
num_items=len(names)
random_choice=random.randint(0,num_items-1)
person_who_will_pay=names[random_choice]
#person_who_will_pay=random.choice(names)
print(person_who_will_pay+' is going to buy the meal today.')