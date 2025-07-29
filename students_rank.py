students = [
    {"name": "raju", "dept": "cse", "marks": [20, 30, 40]},
    {"name": "vijay", "dept": "cse", "marks": [10, 70, 43]},
    {"name": "pavi", "dept": "ece", "marks": [22, 38, 56]},
    {"name": "rose", "dept": "ece", "marks": [26, 36, 89]},
    {"name": "virat", "dept": "ece", "marks": [16, 90, 43]}
]
for i in students:
    sums = sum(i["marks"])
    per = sums / 3   
    i["per"] = per
des = ["FIRST", "SECOND", "THIRD", "FOURTH", "FIFTH"]
b = sorted(students, key=lambda x: x["per"], reverse=True)
for index in range(len(b)):
    student = b[index]
    print("{}. {} stands {} with {:.2f}%".format(index+1, student["name"], des[index], student["per"]))
