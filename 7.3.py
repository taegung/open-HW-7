from tkinter import*
from tkinter import ttk

window=Tk()
##2019038059 윤태경##
baseTab=ttk.Notebook(window)
tabDog=ttk.Frame(baseTab)
baseTab.add(tabDog,text='강아지')
tabCat=ttk.Frame(baseTab)
baseTab.add(tabCat,text='고양이')

baseTab.pack(expand=1,fill="both")
photoDog=PhotoImage(file="C:/Users/82109/Desktop/강아지.gif")
labelDog=Label(tabDog,image=photoDog)
labelDog.pack()
photoCat=PhotoImage(file="C:/Users/82109/Desktop/고양이.gif")
labelCat=Label(tabCat,image=photoCat)
labelCat.pack()

window.mainloop()
