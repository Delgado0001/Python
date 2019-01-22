from class_quadratic import *

def main():
	print("input a,b and c from and equation ax^2 + bx + c :")
	#get inputs
	a = float(input("input a "))
	b = float(input("input b "))
	c = float(input("input c "))
	#end get inputs
	p1 = QuadraticEquation(a,b,c)
	x1 = p1.x1()
	x2 = p1.x2()
	print ("Discriminant = ",p1.discriminant())
	print ("x1 = ",x1," x2 = ",x2)
	
if __name__ == "__main__":
	main()
