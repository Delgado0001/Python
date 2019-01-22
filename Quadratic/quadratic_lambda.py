#quadratic_lambda.py DDG

def quadratic_function(a,b,c):
	return lambda x: a*(x**2) + b*x + c
	
a1 = quadratic_function(1,2,1)
print("a1 ",a1(1))
print("Input a,b and c from a quadratic equation in the form of")
print("f(x) = ax^2 + bx + C")

a = int(input("input a "))
b = int(input("input b "))
c = int(input("input c "))
x = int(input("input x "))
a2 = quadratic_function(a,b,c)
fx = a2(x)
print("f(x) = ",fx)
