import turtle


def draw_tri(pen, length):
	for i in range(3):
		pen.forward(length)
		pen.left(120)



def draw_art():
	window = turtle.Screen()
	window.bgcolor("white")

	tri = turtle.Turtle()
	tri.color("blue", "green")
	tri.speed(9)
	

	y = 50

	for k in range (3):
		for j in range (3):
			for i in range(3):
				tri.forward(2*y)
				tri.left(120)
				tri.begin_fill()
				draw_tri(tri, y)
				tri.end_fill()
				#tri.left(60)
			tri.forward(4*y)
			tri.left(120)
		tri.forward(8*y)
		tri.left(120)

			


		




	
	window.exitonclick()

draw_art()