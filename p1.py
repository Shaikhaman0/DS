
#This Python program is used to mark the attendance of students in a class of 30 students. Initially, all students are marked Absent ('A'). The user enters the roll number of a student who is present, and the program changes the attendance of that student from 'A' (Absent) to 'P' (Present). Finally, it displays the updated attendance list.

a=['A']*30
print(a)
roll=int(input("Enter roll no."))
a[roll-1]="P"
print(a)