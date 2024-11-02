import easygui
import random
from PIL import Image,ImageFilter,ImageDraw,ImageFont

def yanzhengcode():
    w = 100
    h = 50
    img = Image.new('RGB', (w, h), 'white')  # 图片对象
    t = ImageDraw.Draw(img)  # 可绘制图片对象
    for x in range(w):
        for y in range(h):
            r = random.randint(100, 255)
            g = random.randint(100, 255)
            b = random.randint(100, 255)
            t.point((x, y), (r, g, b))
    f = ImageFont.truetype('simhei.ttf', 36)  # 字体对象
    col = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'black', 'white']
    leter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    p1 = random.choice(['n', 's'])
    if p1 == 'n':
        c1 = str(random.randint(0, 9))
        c1c = random.choice(col)
    else:
        c1 = random.choice(leter)
        c1c = random.choice(col)
    p2 = random.choice(['n', 's'])
    if p2 == 'n':
        c2 = str(random.randint(0, 9))
        c2c = random.choice(col)
    else:
        c2 = random.choice(leter)
        c2c = random.choice(col)
    p3 = random.choice(['n', 's'])
    if p3 == 'n':
        c3 = str(random.randint(0, 9))
        c3c = random.choice(col)
    else:
        c3 = random.choice(leter)
        c3c = random.choice(col)
    p4 = random.choice(['n', 's'])
    if p4 == 'n':
        c4 = str(random.randint(0, 9))
        c4c = random.choice(col)
    else:
        c4 = random.choice(leter)
        c4c = random.choice(col)
    p5 = random.choice(['n', 's'])
    if p5 == 'n':
        c5 = str(random.randint(0, 9))
        c5c = random.choice(col)
    else:
        c5 = random.choice(leter)
        c5c = random.choice(col)
    num = c1 + c2 + c3 + c4 + c5
    t.text((5, 8), text=num, fill='red', font=f)
    t.line((0, 20, w, h - 20), 'green', 3)
    t.line((20, h, w - 20, 0), (0, 255, 0), 3)
    img.save('img.png')
    abcd = easygui.enterbox('请输入验证码', '验证码', image='img.png')
    if abcd == num:
        easygui.msgbox('验证码正确', '验证码')
        return True
    else:
        easygui.msgbox('验证码错误', '验证码')
        return False
def welcome():
    yzc = 'FSD3420FVKL343RFSO94'
    easygui.msgbox('欢迎使用my_picture的beta1.8版本,此beta版本需要输入您在我们官网上的激活密钥才可以使用','my_picture','好的')
    ye = easygui.enterbox('请输入本版本的激活密钥','my_picture')
    if ye == yzc:
        easygui.msgbox('密钥输入正确，欢迎使用my_picture的beta1.8版本')
        return True
    else:
        easygui.msgbox('密钥输入错误，请重新启动程序并重试')
        return False
def filter(path):
    img = Image.open(path)
    m = ['进行模糊效果', '进行轮廓效果', '进行细节效果', '边缘加强效果', '让边缘部分更加明显', '进行浮雕效果','进行边界效果', '进行平滑效果', '让图片更平滑', '进行锐化效果']
    use = easygui.choicebox('请选择要对图片的编辑选择','my_picture',m)
    while True:
        if use == '进行模糊效果':
            b = img.filter(ImageFilter.BLUR)
        elif use == '进行轮廓效果':
            b = img.filter(ImageFilter.CONTOUR)
        elif use == '进行细节效果':
            b = img.filter(ImageFilter.DETAIL)
        elif use == '边缘加强效果':
            b = img.filter(ImageFilter.EDGE_ENHANCE)
        elif use == '让边缘部分更加明显':
            b = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
        elif use == '进行浮雕效果':
            b = img.filter(ImageFilter.EMBOSS)
        elif use == '进行边界效果':
            b = img.filter(ImageFilter.FIND_EDGES)
        elif use == '进行平滑效果':
            b = img.filter(ImageFilter.SMOOTH)
        elif use == '让图片更平滑':
            b = img.filter(ImageFilter.SMOOTH_MORE)
        elif use == '进行锐化效果':
            b = img.filter(ImageFilter.SHARPEN)
        elif use == None:
            c = easygui.msgbox('是否退出此功能？', 'my_picture', '是')
            if use != None:
                img.show()
                break
def keep(path):
    img = Image.open(path)
    color_choice = easygui.choicebox('请选择要保留的通道','my_picture',['保留红色通道','保留绿色通道','保留蓝色通道'])
    if color_choice == '保留红色通道':
        color = 'r'
    elif color_choice == '保留绿色通道':
        color = 'g'
    elif color_choice == '保留蓝色通道':
        color = 'b'
    w = img.width
    h = img.height
    for x in range(w):
        for y in range(h):
            l = img.getpixel((x, y))
            r = l[0]
            g = l[1]
            b = l[2]
            if color == 'r':
                img.putpixel((x, y), (r, 0, 0))
            elif color == 'g':
                img.putpixel((x, y), (0, g, 0))
            elif color == 'b':
                img.putpixel((x, y), (0, 0, b))
    img.show()
def text(path):
    img = Image.open(path)
    # img.show()
    img = img.convert('LA')
    w = img.width
    h = img.height
    for x in range(w):
        for y in range(h):
            pixel = img.getpixel((x, y))
            if pixel[0] < 100:
                img.putpixel((x, y), (0, 255))
            else:
                img.putpixel((x, y), (255, 0))
    img = img.resize((int(w * 0.5), int(h * 0.5)))
    bgc = easygui.msgbox('请输入文件名（包括后缀名）','my_picture')
    bg = Image.open(f'images/{bgc}')
    be = easygui.enterbox("请输入图片的坐标（(x,y)，如(500,450)）", "my_picture")
    bg.paste(img, (157, 55), mask=img)
    draw = ImageDraw.Draw(bg)
    fc = easygui.msgbox('请输入字体名（包括后缀名）','my_picture')
    font = ImageFont.truetype(fc, 40)
    text = easygui.enterbox("请输入文本", "my_picture")
    tc = easygui.easygui.enterbox("请输入字体的坐标（(x,y)，如(500,450)）", "my_picture")
    draw.text((500, 450), text=text, fill=(0, 0, 0), font=font)
    bg.show()
def vcode(path):
    w = 100
    h = 50
    img = Image.new('RGB', (w, h), 'white')  # 图片对象
    t = ImageDraw.Draw(img)  # 可绘制图片对象
    for x in range(w):
        for y in range(h):
            r = random.randint(100, 255)
            g = random.randint(100, 255)
            b = random.randint(100, 255)
            t.point((x, y), (r, g, b))
    f = ImageFont.truetype('simhei.ttf', 36)  # 字体对象
    col = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'black', 'white']
    leter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    p1 = random.choice(['n', 's'])
    if p1 == 'n':
        c1 = str(random.randint(0, 9))
        c1c = random.choice(col)
    else:
        c1 = random.choice(leter)
        c1c = random.choice(col)
    p2 = random.choice(['n', 's'])
    if p2 == 'n':
        c2 = str(random.randint(0, 9))
        c2c = random.choice(col)
    else:
        c2 = random.choice(leter)
        c2c = random.choice(col)
    p3 = random.choice(['n', 's'])
    if p3 == 'n':
        c3 = str(random.randint(0, 9))
        c3c = random.choice(col)
    else:
        c3 = random.choice(leter)
        c3c = random.choice(col)
    p4 = random.choice(['n', 's'])
    if p4 == 'n':
        c4 = str(random.randint(0, 9))
        c4c = random.choice(col)
    else:
        c4 = random.choice(leter)
        c4c = random.choice(col)
    p5 = random.choice(['n', 's'])
    if p5 == 'n':
        c5 = str(random.randint(0, 9))
        c5c = random.choice(col)
    else:
        c5 = random.choice(leter)
        c5c = random.choice(col)
    num = c1 + c2 + c3 + c4 + c5
    t.text((5, 8), text=num, fill='red', font=f)
    t.line((0, 20, w, h - 20), 'green', 3)
    t.line((20, h, w - 20, 0), (0, 255, 0), 3)
    sac = easygui.choicebox('已为你创建验证码，是否保存','my_picture',['是','否'])
    if sac == '是':
        sana = easygui.msgbox('请输入保存的文件名','my_picture','保存')
        img.save(sana)
    abcd = easygui.enterbox('请输入验证码', '验证码', image='img.png')
    if abcd == num:
        easygui.msgbox('验证码正确', '验证码')
    else:
        easygui.msgbox('验证码错误', '验证码')