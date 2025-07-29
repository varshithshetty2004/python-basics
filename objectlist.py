class abc:
    def dis(self, a, b):
        self.a = a
        self.b = b
    def greet(self):
        print("Good morning")
z = abc()
x = abc()
z.dis(20, 10)  # Fixed method name
x.dis(50, 70)
varsha = []
varsha.append(x)
varsha.append(z)

print(varsha[0].a)  # Will print 50
print(varsha[0].b)  # Will print 70
