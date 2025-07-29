def find(exp):
    operand = []
    operator = []
    priority = {'+':2, '-':2, '*':3, '//':3}
    i = 0
    while i < len(exp):
        if exp[i].isdigit():
            num = ""
            while i < len(exp) and exp[i].isdigit():
                num += exp[i]
                i += 1
            operand.append(int(num))
        else:
            # Check for '//' operator
            if exp[i] == '/' and i + 1 < len(exp) and exp[i+1] == '/':
                op_token = '//'
                i += 2
            else:
                op_token = exp[i]
                i += 1

            while operator and priority[operator[-1]] >= priority[op_token]:
                op = operator.pop()
                num2 = operand.pop()
                num1 = operand.pop()
                if op == '+':
                    operand.append(num1 + num2)
                elif op == '-':
                    operand.append(num1 - num2)
                elif op == '*':
                    operand.append(num1 * num2)
                elif op == '//':
                    operand.append(num1 // num2)
            operator.append(op_token)

    while operator:
        op = operator.pop()
        num2 = operand.pop()
        num1 = operand.pop()
        if op == '+':
            operand.append(num1 + num2)
        elif op == '-':
            operand.append(num1 - num2)
        elif op == '*':
            operand.append(num1 * num2)
        elif op == '//':
            operand.append(num1 // num2)
    return operand[0]

exp = "10+2*3//4+3"
res = find(exp)
print(res)

write a prog to schedule task usig round robin
def find(task,time):
    
task =(10,5,8)
time = 4
find(task,time)
