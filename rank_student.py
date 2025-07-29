import time
an = []  
bn = []  
for i in range(5):
    a = input("Enter the name {}: ".format(i + 1))
    an.append(a)
    student_marks = []
    for j in range(3):
        b = int(input("Enter mark {} for {}: ".format(j + 1, a)))
        student_marks.append(b)
    bn.append(student_marks)
per = []
for marks in bn:
    avg = sum(marks) // 3
    per.append(avg)
time.sleep(3)
print("--------")
for i in range(5):
    print("{}. {}: {}".format(i + 1, an[i], per[i]))
