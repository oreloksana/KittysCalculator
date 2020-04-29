from cgitb import text
from tkinter import*

from include import source


def iCalc(source, side):
    storeObj = Frame(source, borderwidth=1, bd=4, bg="pink")
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

def button (source, side, text, command = None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Kitty Calculator')

        display = StringVar()
        Entry(self, relief=RIDGE,
              textvariable=display, justify='right', bd=30, bg="pink").pack(side=TOP, expand=YES, fill=BOTH)

        for clearBut in (["CE"],["C"]):
            erase = iCalc(self, TOP)
            for ichar in clearBut:
                button(erase, LEFT, ichar,
                       lambda storeObj=display, q=ichar: storeObj.set(''))

        for NumBut in ("789/", "456*", "123-", "0.+"):
            FunctionNum = iCalc(self, TOP)
            for iEquels in NumBut:
                button(FunctionNum, LEFT, iEquels,
                       lambda storeObj=display, q=iEquels: storeObj.set(storeObj.get() + q))

        EquelsButton = iCalc(self, TOP)
        for iEquels in "=":
            if iEquels == '=':
                btniEquels = button(EquelsButton, LEFT, iEquels)
                btniEquels.bind('<ButtonRelease-1>',
                                lambda e, s=self, storeObj=display: s.calc(storeObj), '+')
            else:
                btniEquels = button(EquelsButton, LEFT, iEquels,
                                    lambda storeObj=display, s='  %s  '%iEquels: storeObj.set(storeObj.get() + s))

    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")

if __name__ == '__main__':
    app().mainloop()