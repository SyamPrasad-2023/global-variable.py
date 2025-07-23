def op(x):
    return x**3
class abc():
    def __init__(self,val):
        self.val = val
    def display(self):
        print("given value:",self.val)
    def modify(self):
        self.val=op(self.val)
n=int(input("enter the value of n:"))        
o=abc(n)
o.display()
o.modify()
o.display()