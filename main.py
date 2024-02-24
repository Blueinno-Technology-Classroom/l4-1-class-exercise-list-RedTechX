##################################################
'''
Q1: 
'''

wrinkle_in_time = ['It', 'was', 'a', 'stormy', 'night', '.']
print(wrinkle_in_time)

##################################################
'''
Q2:
'''

wrinkle_in_time.insert(3, 'and')
wrinkle_in_time.insert(3, 'dark')
print(wrinkle_in_time)
##################################################
'''
Q3:
'''

# TODO: Write your code here
wrinkle_in_time[1] = 'is'

##################################################
'''
Q4:
'''

# TODO: Write your code here

for i in range(len(wrinkle_in_time) - 1, -1, -1):
    w = wrinkle_in_time[i]
    
    if 'a' in w:
        wrinkle_in_time.remove(w)

print(wrinkle_in_time)

##################################################
'''
Q5:
'''

# TODO: Write your code here

even = []

for i in range(10):
    even.append((i) * 2)

print(even)
##################################################
'''
Q6:
'''

# TODO: Write your code here

##################################################
