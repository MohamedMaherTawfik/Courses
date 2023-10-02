'''
You are given a two lists a and b. Your task is to compute their cartesian product aXb.
'''
'''
m=int(input("How many lists elements : "))
A=[]
B=[]

for i in range(m):
    element=int(input("First list Element : "))
    A.append(element)

for i in range(m):
    element=int(input("Second List Element : "))
    B.append(element)
AxB=[]
c=[]
for i in A:
    for x in B:
        AxB=[f"{i}x{x}"]
        

print(AxB)    
'''


'''
You are given a string s .
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.
'''
from itertools import permutations
 
def lexicographical_permutation(str):
    perm = sorted(''.join(chars) for chars in permutations(str))
    for x in perm:
        print(x)
         
str =input("Enter String : ")
lexicographical_permutation(str)
