# 1. Write a Python program to sum all the items in a list.
"""lst=[1, 2, 3, 4, 5]
total=0
for i in range(0,len(lst)):
    total=total+lst[i]
print("sum of list in elements=", total)

#2. Write a Python program to multiply all the items in a list.
lst1=[1,2,3,5]
tl=1
for a in range(0, len(lst1)):
    tl = tl * lst1[a]
print("multiply all the lst item=", tl)

#by using numpy
import numpy as np
list1=[7,8,9]
list2=[4,5,6]
result=np.product(list1)
result2=np.product(list2)
print(result2)
print(result)

#3. Write a Python program to get the largest number from a list.
list3=int(input("enter a number"))
lt=[]
for c in range(0,list3+1):
    d=int(input("elemnt:"))
    lt.append(d)
print("max ", max(lt))"""
import random

# 4. Write a Python program to get the smallest number from a list.
"""def Mymin(list4):
    min = list4[0]
    for i in list4:
        if i>min:
            min=i
        return min

list4=[11,12,13,14,15]
print("minimum number:",Mymin(list4))"""

# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
#		Expected Result : 2
"""def match_word(list5):
    lt=0
    for wrd in list5:
        if len(wrd)>1 and (wrd[0]==wrd[-1]):
            lt += 1
    return lt
list5=['asdf','abba','byhyt','1221','racecar']
print("count in word same char",((match_word(list5))))"""

"""list6=['asdf','abba','byhyt','1221','racecar','g','gg']
c=0
for wd in list6:
    if len(wd)>1 and (wd[0]==wd[-1]):
        c=c+1
print(c)"""

# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
# using sort
"""def sort_tuple(n):
        return n[-1]
def srt(tuple):
    return sorted(tuple, key=sort_tuple)   # return sorted(tuple,key=sort_tuple) or # return sorted(tuple,key=lambda x:x[-1])
list6=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print("sorted:",srt(list6))

#7. Write a Python program to remove duplicates from a list.
list7=[1, 1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 7, 9]
s1=set(list7)
l1=list(s1)
print(l1)

def remov(duplicates):
    fnl=[]
    for num in duplicates:
        if(num not in fnl):
            fnl.append(num)
    return fnl
duplicates=[1, 1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 7, 9]
print("remove duplicates in list:",remov(duplicates))

#8. Write a Python program to check a list is empty or not.
list8=[1, 2, 3, 4, 5, "tc", "amma", "nanna"]
list81=[]
if list81 :
    print("list81 is not empty")
else:
    print("list is empty")

def enquiry(list82):
    if len(list82) == 0:
        return 0
    else:
        return 1
list82=[]
if enquiry(list82):
    print("list 82 is not empty")
else:
    print("list is empty")"""

# 9. Write a Python program to clone or copy a list
"""lista = [1, 2, 3, 4, 5]
listb = []
for i in lista:
    listb.append(i)
print("listb copy from lista:",listb)
print(lista)
print(listb)


#10. Write a Python program to find the list of words that are longer than n from a given list of words.
def given_words(listc,n):
    listd=[]
    txt=str.split(" ")
    for m in txt:
        if len(m) > n:
            listd.append(m)
    return listd
listc=["hare krishna hare krishna krishna krishna hare hare"]
print("longer then from given list:",given_words(4,listc))

#11. Write a Python function that takes two lists and returns True if they have at least one common member.
def comn_list(liste, listf):
    same=0
    for b in liste:
        for v in listf:
            if (b)==(v):
                same += 1
                return True
            else:
                    return False
liste=["tana","sujatha","suma", 1,2,3]
listf=["tana","veena","nanna",7,8,9]
print("common words are both list:",comn_list(liste,listf))

#12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
#		Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#		Expected Output : ['Green', 'White', 'Black']
listg=['red', 'green', 'white', 'black', 'pink', 'yellow']
listh=[]
for c,d in enumerate(listg):
    if c not in [0,3,4]:
        listh.append(d)
print(listh)

color=['red', 'green', 'white', 'black', 'pink', 'yellow']
color=[x for (i,x) in enumerate(color) if i not in (0, 4, 5)]
print(color)



#11.Write a Python program to generate a 3*4*6 3D array whose each element is *.

array=[[['*' for a in range(6)]for b in range(4)]for f in range(3)]
print(array)

import pprint
def threeD(a, b, c):
    lst=[[['@' for g in range(a)]
          for h in range(b)]
         for j in range(c)]
    return lst
c1=4
c2=3
c3=5
pprint.pprint(threeD(c1,c2,c3))


# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.
list14 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for t in list14:
    if (t%2 != 0):
        print(t)"""

# 15. Write a Python program to shuffle and print a specified list.
"""import random
list15 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(list15)
print(list15)

#16. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).
list16=[x**2 for x in range(1, 31)]
print(list16[:5], list16[-5:])   #1,2,3,4,5  and 26, 27, 28, 29, 30

#def method
def list162():
    lt = []
    for b in range(1, 31):
        lt.append(b**2)
    print(lt[:5])
    print(lt[-5:])
list162()"""

# 17. Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included).
"""def list17():
    lt2 = list()
    for c in range(1, 21):
        lt2.append(c**2)
    print(lt2[5:])
list17()

list171=[d**2 for d in range(1, 31)]
print(list171[5:])"""

# write a python program in a given list to print highest palindrom of in alist
li = ["amma", "abba", "malayalam", "racecar", "pop"]
ml = 0
cl = 0
pos = [-1]
for i in range(0, len(li)):
    cv = (str(li[i]))
    if (cv == cv[::-1]):
        cl = len(cv)
    if (cl > ml):
        ml = cl
        pos = i
print(li[pos])

"""def print_mylist(alpha_list,num_list):
    for alpha in alpha_list:
        for num in num_list:
            print(alpha,num)
    return
print_mylist(alpha_list=['a','b','c'],num_list=[1,2,3])
number=3
print(f"The number is{number}")
a=[1,2,3,4]
b=a[-2]
print(b)"""
"""y=("stuff";"match";"ram")
z=y.split(';')
len(z)"""
# x=1j
# print(x**2 == -1)


"""for i in range(5):
    print(i)
else:
    print("done")

n=int(input("enter some number:"))
li=[]
command=[]
for input in range(0, n):
    command.append(input)
for cmd in command:
    if cmd == 'print':
        print(li)
    else:
        cmdarg=cmd.split()
        operation_arg=','.join(cmdarg[1:])
        exec=('list.'+cmdarg[0]+'('+ operation_arg + ')')"""

# maxi plindrome in gopi
lis = ["racecar", "malayalam", "liril", "amma", "tana", "raja"]
ml = 0
for i in lis:
    if i == i[::-1]:
        n = len(i)
    if n > ml:
        ml = n
for i in lis:
    if len(i) == ml:
        print(i)

# 18. Write a Python program to generate all permutations of a list in Python.
"""import itertools
list18=["t","a","n","a"]
l181=((list(itertools.permutations((list18)))))
print(l181,len(l181))


#19. Write a Python program to get the difference between the two lists.
li19a=[1,2,3,4,5,"red", "orange"]
s1=set(li19a)
li19b=[1,4,8,7,9,"yellow", "green"]
s2=set(li19b)
diff_list1=s1-s2
diff_list2=s2-s1
l1=list(diff_list1)
l2=list(diff_list2)
print(l1, "\n",l2)

#20.Write a Python program access the index of a list.
list20=[11,22,33,44,55]
for k,v in enumerate(list20):
    print(k,v)
#21.Write a Python program to convert a list of characters into a string.
list21=["t","a","n","a", "g","a","n","n","o","j"]
string21="".join(list21)
print(string21)
#22. Write a Python program to find the index of an item in a specified list.
list22=["t","n","a", "g","o","j"]
list221=list22.index("j")
print(list221)
#23. Write a Python program to flatten a shallow list.
list23=[[9,8,7],[6,5,4],[3,2,1],["t","a","n"]]
nl=[]
for i in list23:
    for j in i:
        nl.append(j)
print(nl)
#solution2
from itertools import chain
nl=list(chain(*list23))
print(nl)
#24.Write a Python program to append a list to the second list
list24=[1,2,3,4,5]
list241=["tana","vishnu","krishna","minnu"]
list242=[]
list243=list24 + list241
for i in list243:
    list242.append(i)
print(list242)
#25. Write a Python program to select an item randomly from a list.
import random
list25=[1,2,3,4,5,6]
element=random.choice(list25)
print(element)
#26.Write a python program to check whether two lists are circularly identical.
def circular_ident(list261,list262):
    if len(list261) != len(list262):
        return print("not circular_identical")
    dbl_a=list261*2
    strng=map(str, list262)
    dbl_strng=map(str, dbl_a)
    if ''.join(strng) in ''.join(dbl_strng):
        return print("circular_identical")
    else:
        return print("not circular_identical")
#main program
circular_ident(list261=[9, 8, 7, 6, 5, 4, 3], list262=[9, 8, 7, 6, 5, 4, 3])

#27. Write a Python program to find the second smallest number in a list.
list27=[1,3,6,5,4,8]
list271=sorted(list27)
print(list271[1])

#28.Write a Python program to find the second largest number in a list.
list284=[1,3,6,5,4,8]
list285=sorted(list284)
print(list285[-2])

#WAPP to print largest string in list
list28=["tana","vishnu","naresh","veeeeeeena"]
list281=0
list282=0
list283=[0]
for i in range(0,len(list28)):
    j=(str(list28[i]))
    if len(j) > list281:
        list282 = len(j)
        if (list281 > list282):
            list282 = list281
            list283=i
print(list28[i])"""

# 29. Write a Python program to get unique values from a list.
list29 = [1, 2, 3, 4, 5, 2, 3, 4, 8, 9, 7, 1]
list291 = set(list29)
list292 = []
for i in list291:
    list292.append(i)
print(list292)

# 30. Write a Python program to get the frequency of the elements in a list.
list30 = [1, 2, 3, 4, 5, 6, 7, 2, 2, 4, 1, 3, 5, "green", "red", "white"]
list301 = []
for i in set(list30):
    list301.append((i, list30.count(i)))
print(list301)
# okokka char enni sarlu vachhindo(repeate) ayyindo dict form lo print cheyyali.
# solution2
list302 = dict(map(lambda x: (x, 0), list30))
for i in list302:
    list302[i] = list30.count(i)
print(list302)

# string reverse
"""s1="gopi"
#s2=reversed(s1)
#print(list(s2))
for k in range(len(s1)-1,-1,-1):
    print(s1[k])
p"""
# WAPP reapeting charcetr to print onetime
"""s2="muppuri  1212"
s3=set()
for l in s2:
    if (s2.count(l)>1):
        s3.add(l)
print(s3)"""

"""str="muppurigopi117@gmail.com"
#o/p=muppurigopi117gamilcom
import re
char=re.finditer("\w",str)
for m in char:
    print(m.group(),end="")"""

"""s4=[]
for m in str:
    if(m.isalnum()== True):
        s4.append(m)
        print(m)
    else:pass
print(s4)"""


# 31. Write a Python program to count the number of elements in a list within a specified range.
# prgrm type:3
"""def count_range_in_list(lst31, min, max):
    ctr = 0
    for x in lst31:
        if min <= x <= max:
            ctr += 1
    return ctr

lst311 = [1, 2, 3, 4, 5, 6, 7, 8]
print(count_range_in_list(lst311, 1, 9))

lst312 = ['a', 'b', 'c', 'd', 'e', 'f']
print(count_range_in_list(lst312, 'a', 'd'))

lst313 = [1,2,4,5,6,7,8]
print(count_range_in_list(lst313,1,4))"""

#32 Write a Python program to check whether a list contains a sublist
l1=[1,2,3,5,6,8]
l2=[1,5,8,4,6]
if(l2==l1) and (l1!=l2):
    print(True)
else:
    print(False)

