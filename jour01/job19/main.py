rectangle_width = int(input("Entrez la largeur du rectangle : "))
rectangle_height = int(input("Entrez la hauteur du rectangle : "))



def rectangle_draw(width, height):
    for item in range(width):
        if item < width:          
            print('|', end = '')
            for i in range(height):
                if item == 0 or item == width - 1:
                    if i < height - 1 :
                        print('-', end ='')
                    elif i == height -1:
                        print('|')             
                else:
                    if i < height - 1 :
                        print(' ', end ='')
                    elif i == height -1:
                        print('|')

rectangle_draw(rectangle_width, rectangle_height)