import turtle

SIZE_TREE = 10


def draw_tree(size):
    if size > SIZE_TREE:
        # 

        turtle.forward(size)
        turtle.right(20)
        draw_tree(size / 1.5)
        # left
        turtle.left(40)
        draw_tree(size / 1.5)

        # Back to the previous branches
        turtle.right(20)
        # Draw the green of the last branch
        if size / 2 <= SIZE_TREE:
            turtle.color('green')
        else:
            turtle.color('brown')
        turtle.backward(size)


def main():
    # turtle.speed(1)
    turtle.hideturtle()
    turtle.penup()
    # 
    turtle.left(90)
    turtle.backward(100)
    turtle.showturtle()
    # 
    # 
    turtle.pendown()
    turtle.pensize(2)
    turtle.color('brown')
    # gives the length of the root
    draw_tree(100)


if __name__ == '__main__':
    main()
    turtle.done()