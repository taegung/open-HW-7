from tkinter import*
from tkinter.colorchooser import*
from tkinter.simpledialog import*

def mouseclick(event):
    global x1,y1,x2,y2
    x1=event.x
    y1=event.y

def mousedrop(event):
    global x1,y1,x2,y2,penwidth,pencolor
    x2=event.x
    y2=event.y
    canvas.create_line(x1,y1,x2,y2,width=penWidth,fill=pencolor)


def getcolor():
    global pencolor
    color=askcolor()
    pencolor=color[1]

def getwidth():
    global penWidth
    penWidth=askinteger("선 두께","선 두께(1~10)를 입력하세요",
                      minvalue=1,maxvalue=10)

##2019038059 윤태경##
window=None
canvas=None
x1,y1,x2,y2=None,None,None,None
pencolor='black'
penWidth=5

window=Tk()
window.title("그림판 비슷한 프로그램")
canvas=Canvas(window,height=300,width=300)
canvas.bind("<Button-1>",mouseclick)
canvas.bind("<ButtonRelease-1>",mousedrop)
canvas.pack()
mainMenu=Menu(window)
window.config(menu=mainMenu)
fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label="설정",menu=fileMenu)
fileMenu.add_command(label="선 색상 선택",command=getcolor)
fileMenu.add_separator()
fileMenu.add_command(label="선 두께 설정",command=getwidth)

window.mainloop()
                    


