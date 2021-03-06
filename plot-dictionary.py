# plot-dictionary.py
import tkinter as tk
import turtle

def main():
	#table is a dictionary
	table = {-100:6,-90:3,-80:0,-70:3,-60:6,-50:9,
				-40:12,-30:9,-20:6,-10:3,0:0,
					10:3,20:6,30:9,40:12,50:9,
					60:6,70:3,80:0,90:3,100:6
			}
	print(" KEYS ")
	print(table.keys())
	print(" VALUES ")
	print(table.values())
	#turtle graphics
	twin = turtle.Screen()
	twin.clear()
	t = turtle.Turtle()
	#tWin = turtle.Screen()
	for h,k in table.items(): #get the items in the dictionary
		print(h,k) # trace code
		#x,y = table[n]
		t.penup()
		t.goto(h,k)
		t.pendown()
		t.circle(6)
	twin.exitonclick()
	
main()

"""
This code uses a dictionary with keys ranging from
-100 to 100 incrementing by 10.
Each key has a value of 0 as an integer.
To retrive the values in the dictionary "table" a for loop is used.
The x coordinate on a python turtle screen corresponds to h while
the y value cooresponds to k.
***************************************
for h,k in table.items(): #get the items in the dictionary
		print(h, k) #trace code
h and k are then ploted using
		t.goto(h,k)
		t.pendown()
		t.circle(6)
"""
