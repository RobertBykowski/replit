from turtle import Turtle, Screen
from prettytable import PrettyTable

# bob = Turtle()
# bob.shape("turtle")
# bob.turtlesize(1)

# bob.forward(100)


# my_screan = Screen()
# print(my_screan.canvheight)
# my_screan.exitonclick()

table = PrettyTable()

table.add_column("Nazwisko", ["Ola","Beata","Tomasz"])
table.add_column("Wiek", ["12","37","56"])
table.align = "l"
print(table)