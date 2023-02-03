from rectangle import Rectangle, Square, Circle

# создаем 2 прямоугольника

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)
# выводим площиди прямоугольников
print(rect_1.get_area(),
      rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)
print(square_1.get_area_square(),
      square_2.get_area_square())

radius_1 = Circle(13.6)
radius_2 = Circle(20.6)
print(round(radius_1.get_area_circle(), 2),
      round(radius_2.get_area_circle(), 2))
# создаем колекцию figures, которая содержит список полученных значений

figures = [rect_1, rect_2, square_1, square_2, radius_1, radius_2]
for figure in figures:
      if isinstance(figure, Square):
            print(figure.get_area_square())
            if isinstance(figure, Rectangle):
                  print(figure.get_area())
            else:
                  print(figure.get_area_circle())


