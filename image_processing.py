import random
from PIL import Image
im = Image.open("images/1111.jpg")
Height=im.size[1]
Width=im.size[0]

def one():
    while True:
        name = str(input('Введите название файла'))
        try:
            symbols_list = [':', '/', '|', '\\', '*', '?', '@', '#', "'", '<', '>', ]
            for symbol  in symbols_list:
               if symbol in name :
                   print('в названии есть запрещенный символ!')

            else:
                im.save(f'./{name}.jpg')
                print(f'Файл"{name}.jpg" успешно сохранен!')
                break
        except Exception as error:
            print(
                'В названии допускаются только буквы, цифры, дефис (-) и подчеркивание (_)')
            print('Придумайте другое название')


print(f"Width: {im.size[0]}")
print(f"Height: {im.size[1]}")
print(f"Mode: {im.mode}")
print(f"Format: {im.format}")
choose=input('Что вы хотите сделать с картинкой? 1)Применить эффект; 2)Сохранить')
if choose=='1':
    effect = input('''Как хотите изменить картину? 
    1)сделать изображение черно-белым;
    2)Отразить изображение по веритикальной оси; 
    3)Отразить изображение по горизоньальной оси
    4)Закрасить случайный квадрат 
       ''')
    if effect=='1':
        for x in range(im.size[0]):
            for y in range(im.size[1]):
                pix = im.getpixel((x, y))
                avg = (pix[0] + pix[1] + pix[2]) // 3
                im.putpixel((x,y), (avg, avg, avg))
        im.show()
        one()
    elif effect=='2':
        horz= im.transpose(Image.Transpose.ROTATE_90)
        horz.show()
        one()
    elif effect=='3':
        vert = im.transpose(Image.Transpose.ROTATE_270)
        vert.show()
        one()
    elif effect=='4':
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        if Height > Width:
            size = random.randint(1, Width - 1)
            x = random.randint(0, Width - size)
            y = random.randint(0, Width - size)
        else:
            size = random.randint(1, Height - 1)
            x = random.randint(0, Height - size)
            y = random.randint(0, Height - size)
        for n in range(x, x + size):
            for m in range(y, y + size):
                pix = im.getpixel((n, m))
                im.putpixel((n, m), (r, g, b))
        im.show()
        one()