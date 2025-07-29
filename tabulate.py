from tabulate import tabulate
headers=["name","Age","department"]
data=[
    ["Ravi","20","ISE"],
    ["pavi","21","CSE"],
    ["ram","21","aiml"],
    ["mohan","21","ecc"],
    ["sita","21","cv"]]
print(tabulate(data,headers=headers,tablefmt="fancy_grid"))
