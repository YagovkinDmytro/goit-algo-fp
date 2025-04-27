import turtle

def draw_tree(t, branch_length, level):
    if level == 0:
        return

    t.forward(branch_length)

    t.left(30)
    draw_tree(t, branch_length * 0.8, level - 1)

    
    t.right(60)
    draw_tree(t, branch_length * 0.8, level - 1)

    # Повертаємо черепашку назад до прямої позиції
    t.left(30)
    t.backward(branch_length)

def main():
    level = int(input("Введіть рівень рекурсії (наприклад, 5): "))

    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)  

    t.left(90)
    t.up()
    t.goto(0, -250)
    t.down()

    draw_tree(t, 100, level)

    turtle.done()

if __name__ == "__main__":
    main()