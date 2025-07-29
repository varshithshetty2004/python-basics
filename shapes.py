def circle():
    r = float(input("Enter radius: "))
    area = 3.14 * r * r
    print("Area of circle:", area)

def square():
    s = float(input("Enter side length: "))
    area = s * s
    print("Area of square:", area)

def rectangle():
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    area = l * b
    print("Area of rectangle:", area)

def triangle():
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    area = 0.5 * b * h
    print("Area of triangle:", area)

# Menu Loop
flag = True
while flag:
    print("\nSelect Shape to Find Area:")
    print("1. Circle")
    print("2. Square")
    print("3. Rectangle")
    print("4. Triangle")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        circle()
    elif choice == '2':
        square()
    elif choice == '3':
        rectangle()
    elif choice == '4':
        triangle()
    elif choice == '5':
        print("Exiting...")
        flag = False
    else:
        print("Invalid choice! Try again.")
