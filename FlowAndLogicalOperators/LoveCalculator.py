print('Welcome to the Love Calculator!')
name1=input('What is your name?\n')
name2=input('What is their name?\n')
combined_string=name1+name2
lover_case_string=combined_string.lower()
t=lover_case_string.count('t')
r=lover_case_string.count('r')
u=lover_case_string.count('u')
e=lover_case_string.count('e')
true=t+r+u+e
l=lover_case_string.count('l')
o=lover_case_string.count('o')
v=lover_case_string.count('v')
e=lover_case_string.count('e')
love=l+o+v+e
love_score=int(str(true)+str(love))
if (love_score<10) or (love_score>90):
 print(f'Your love score is {love_score} , you go together like coke and mentos.')
elif (love_score>=40) and (love_score<=50):
 print(f'Your score is {love_score}, you are all right together')
else:
 print(f'Your score is {love_score}')