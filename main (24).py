def circle():
    r=int(input("Enter the radius: "))
    print("Area of circle is:", 3.14*r * r)

def square(a):
    print("Area of square is:", a * a)

def triangle():
    b=int(input("Enter the base: "))
    h=int(input("Enter the height: "))
    return 0.5*b*h

def rectangle(a,b):
    return a*b

while True:
    print("\n1. Circle")
    print("2. Square")
    print("3. Triangle")
    print("4. Rectangle")
    print("5. Exit")

    ch=int(input("Enter your choice: "))
    
    match ch:
        case 1:
            circle()
        case 2:
            a=int(input("Enter side of the square: "))
            square(a)
        case 3:
            res=triangle()
            print("Area of triangle is:", res)
        case 4:
            a=int(input("Enter the length of rectangle: "))
            b=int(input("Enter the breadth of rectangle: "))
            res = rectangle(a, b)
            print("Area of rectangle is:", res)
        case 5:
            print("Exiting...")
            break
        case _:
            print("Invalid choice. Please try again.")