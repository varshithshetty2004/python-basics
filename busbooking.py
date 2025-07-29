from datetime import datetime
class Bus:
    def __init__(self, bno, ac, cap):
        self.bno = bno
        self.ac = ac
        self.cap = cap
    def get_bno(self):
        return self.bno
    def get_cap(self):
        return self.cap
    def get_ac(self):
        return self.ac
    def display(self):
        print(f"Bus number : {self.get_bno()}")
        print(f"Bus AC : {self.get_ac()}")
        print(f"Bus capacity : {self.cap}")

class Booking:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.bno = int(input("Enter your bus number: "))
        d = input("Enter the date (dd-mm-yyyy): ")
        self.date = datetime.strptime(d, "%d-%m-%Y").date()
    def make_booking(self, BUSES, BOOKING):
        if self.is_available(BUSES, BOOKING):
            BOOKING.append(self)
            print("Booking successful!")
        else:
            print("Bus is full.")
    def is_available(self, BUSES, BOOKING):
        booked = 0
        capacity = 0
        for i in BUSES:
            if i.bno == self.bno:
                capacity = i.cap
        for i in BOOKING:
            if i.bno == self.bno and i.date == self.date:
                booked += 1
        return booked < capacity
    def display_booking_info(self):
        print(f"{'Name':<15}: {self.name}")
        print(f"{'Bus Number':<15}: {self.bno}")
        print(f"{'Date':<15}: {self.date.strftime('%d-%m-%Y')}")
      
BUSES = [Bus(1, True, 2), Bus(2, False, 60), Bus(5, True, 20)]
print("Available buses are:")
for i in BUSES:
    i.display()
    print("---------")
BOOKING = []
while True:
    print("\n1. Press 1 to book ticket \n2. Press 2 to view booking \n3. Press 3 to exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        b = Booking()
        b.make_booking(BUSES, BOOKING)
    elif ch == 2:
        if not BOOKING:
            print("No bookings made yet.")
        else:
            for i in BOOKING:
                i.display_booking_info()
    elif ch == 3:
        print("Exiting the system.")
        break
    else:
        print("Invalid choice!")
