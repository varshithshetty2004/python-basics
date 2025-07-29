str1 = input("Enter the sentence: ")
c = 0
for i in range(len(str1) - 1):  # stop at len - 1 to avoid IndexError
    if str1[i] == " " and str1[i + 1] != " ":
        c += 1
print("Number of words:", c + 1) 
