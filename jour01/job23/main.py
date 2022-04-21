triangle = int(input("Entrez la hauteur du triangle : "))

def draw_triangle(height):
    for i in range(height):
        base = " "
        if i == height -1:
            base = '_'
        print(' ' * (height - i), end='')
        print('/', end='')
        print(base * i * 2, end='')
        print('\\')

draw_triangle(triangle)