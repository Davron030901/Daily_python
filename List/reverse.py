#1) Using the reverse method
my_list = ['red', 'green', 'blue', 'yellow', 'orange', 'pink']
my_list.reverse()
print(my_list)

# 2)Using the slicing
my_list = ['red', 'green', 'blue', 'yellow', 'orange', 'pink']
reversed_list=my_list[::-1]
print(reversed_list)

# 3)Usint the reversed function
my_list = ['red', 'green', 'blue', 'yellow', 'orange', 'pink']
reversed_list=list(reversed(my_list))
print(reversed_list)

#4)Using a loop
my_list = ['red', 'green', 'blue', 'yellow', 'orange', 'pink']
r_list=[]
for i in my_list:
    r_list.insert(0,i)
print(r_list)

#5)Using append method
my_list = ['red', 'green', 'blue', 'yellow', 'orange', 'pink']
reversed_list=[]
for i in range(len(my_list)-1,-1,-1):
    reversed_list.append(my_list[i])
print(reversed_list)
