# 13.Write a program to print the top 3 highest values of a given dictionary.❓❓❓

# Example :-
# my_dict = {
#  'a':50, 
#  'b':58,
#  'c': 56,
#  'd':40,
#  'e':100, 
#  'f':20
#  }
# Visualize
# Output :-
# expect result:-['e','b','c']

d= {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
a=[ ]
for i in d:
    if d[i]>50:
        h=i
        a.append(i)
print(a)