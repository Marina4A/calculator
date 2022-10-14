from tkinter import *


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"),
                         bg="#000", foreground="#FFF")
        self.lbl.place(x=11, y=50)

    def build(self):
        btns = [
            "C", "DEL", "*", "=",
            "1", "2", "3", "/",
            "4", "5", "6", "+",
            "7", "8", "9", "-",
            "+/-", "0", "%", "X^2"
        ]
        x = 10
        y = 140
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg="#FFF",
                   font=("Times New Roman", 15),
                   command=com).place(x=x, y=y,
                                      width=115,
                                      height=79)
            x += 117
            if x > 400:
                x = 10
                y += 81

    def logicalc(self, operation):
        operation_func = {'C': "", 'DEL': self.formula[0:-1], 'X^2': str((eval(self.formula)) ** 2),
                          '=': str(eval(self.formula))}
        if operation in operation_func.keys():
            self.formula = operation_func[operation]
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#000"
    root.geometry("485x550+200+200")
    root.title("Калькулятор")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()

# from operator import add, sub, mul, truediv
#
#
# def math_oper(text):
#     math_dict = {'+': add, '-': sub, '*': mul, '/': truediv}
#     operand_1, operation, operand_2 = text.split()
#
