import tkinter

def calc_bmi():
    h = float(ht_val.get())   # fixed ht.val_get -> ht_val.get()
    c = float(wt_val.get())   # fixed ct.val_get -> wt_val.get()
    h1 = h / 100
    bmi = c / h1**2           # fixed m -> c (since weight is 'c')
    
    if(bmi < 18.5):
        status = "underweight"
    elif(bmi >= 18.5 and bmi <= 24.9):
        status = "normal"
    elif(bmi >= 24.9 and bmi < 29.9):
        status = "overweight"
    else:
        status = "obesity"
        
    res.config(text=f"BMI is {bmi:.2f} ({status})")  # fixed res=config() -> res.config()

root = tkinter.Tk()
root.geometry("500x500")  # fixed "500*500" -> "500x500"
root.title("BMI Calculator")
root.configure(bg="#f0f0f0")

head = tkinter.Label(root, text="BMI Calculator", bg="#f0f0f0")
head.pack(pady=50)

fr = tkinter.Frame(root, bg="#f0f0f0")  # fixed bg color from "0f0f0f0" to "#f0f0f0"
fr.pack(pady=5)

ht = tkinter.Label(fr, text="Height(in cm)", font=("Arial", 19))
ht.grid(row=1, column=0, padx=5, pady=5)

ht_val = tkinter.Entry(fr)
ht_val.grid(row=1, column=1, padx=5, pady=5)

wt = tkinter.Label(fr, text="Weight(in kg)", font=("Arial", 15))
wt.grid(row=2, column=0, padx=5, pady=5)

wt_val = tkinter.Entry(fr)  # added missing weight entry box
wt_val.grid(row=2, column=1, padx=5, pady=5)

btn = tkinter.Button(root, text="Calculate BMI", command=calc_bmi)
btn.pack(pady=20)

res = tkinter.Label(root, text="", font=("Arial", 15), bg="#f0f0f0")
res.pack(pady=10)

root.mainloop()
