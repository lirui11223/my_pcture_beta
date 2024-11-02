import image_use
import easygui

we = image_use.welcome()
if we == True:
    yzcode = image_use.yanzhengcode()
    if yzcode == True:
        cl = ['对图片进行一定的效果','保留图片的其中一个通道']
        p = easygui.enterbox('请输入图片的路径（包括后缀名）')
        c = easygui.choicebox('请选择您想要使用的功能','my_picture',cl)
        if c == cl[0]:
            image_use.filter(p)
        elif c == cl[1]:
            image_use.keep(p)