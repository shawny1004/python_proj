import shape

## This lab demos inheritance

## shape1 only has a name
my_shape1 = shape.Shape("shape_1")
print(f"shape_1's name is {my_shape1.get_name()}")
## this will throw error 
# print(my_shape1.get_area())

## shape2 is a rectangle
my_shape2 = shape.Rectangle("shape_2_rectangle", 20, 10)
print(f"shape_2's name is {my_shape2.get_name()}")
print(f"shape_2's area is {my_shape2.get_area()}")

## shape3 is a square
my_shape3 = shape.Square("shape_3_square", 20)
print(f"shape_3's name is {my_shape3.get_name()}")
print(f"shape_3's area is {my_shape3.get_area()}")

## shape4 is a square with a hole
my_shape4 = shape.SquareWithAHoleInside("shape_4_square_hole", 20, 1)
print(f"shape_4's name is {my_shape4.get_name()}")
print(f"shape_4's area is {my_shape4.get_area()}")


## shape5 is a red circle
my_shape5 = shape.Circle("shape_5_circle", 10)
print(f"shape_5's name is {my_shape5.get_name()}")
print(f"shape_5's area is {my_shape5.get_area()}")
print(f"shape_5's color is {my_shape5.get_color()}")

print("#############################")

## use list
## we can do all the thing use a list
my_shapes = [my_shape1, my_shape2, my_shape3, my_shape4, my_shape5]
for s in my_shapes:
    try:
        print(f"A {s.get_color()} {s.get_name()} has area of {s.get_area()}" )
    except NotImplementedError:
        print(f"{s.get_name()}'s area function is not implemented")

## Type casting:
## say if my square's hole is fixed now, I don't want to subtract the hole 
my_shape4.__class__=shape.SquareWithAHoleInside
my_shape4.get_area = shape.Square.get_name
print(f"Now the area is {my_shape4.get_area()} without hole")