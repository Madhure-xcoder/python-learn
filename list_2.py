marks=[34,45,56,67,]
print(type(marks))
print(marks[0])
print(marks[3])
marks[3]=88
print(marks)

#slicing of list
print(marks[:5])
print(marks[::-1])

#Methods of list
marks.append(5)
print(marks)

#accending order
marks.sort()
print(marks)

#decending order
marks.sort(reverse=True)
print(marks)

marks.insert(1,50)
print(marks)

marks.sort()
print(marks)

marks.remove(56)
print(marks)

marks.pop(2)
print(marks)