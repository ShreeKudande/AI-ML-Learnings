#Q. Write a program to check whether two lists share no common elements.

#share no common elements
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

s1 = set()
s1.update(list1)

s2 = set()
s2.update(list2)

if len(s1.intersection(s2)) == 0:
    print("Share no common elements")
else:
    print("Share common elements")

#share common elements
list3 = [1, 2, 3]
list4 = [3, 4]

s3 = set()
s3.update(list3)
s4 = set()
s4.update(list4)

if len(s3.intersection(s4)) == 0:
    print("Share no common elements")
else:
    print("Share common elements")

    