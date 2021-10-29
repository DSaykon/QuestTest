from tkinter import *
from tkinter import messagebox
import testlibrary
from interface import TestInterface


class Test:
    """Class Test for programme QuestTest"""

    def __init__(self, title='test', test_question_list=None):
        if test_question_list is None:
            test_question_list = []
        self.title = title
        self.test_question_list = test_question_list
        self.total_questions = len(test_question_list)


class TestWindow:

    def __init__(self, root):
        self.root = root
        self.root.title('Выберите тест')
        self.root.geometry('250x150')
        window = Frame(self.root, relief='raised', bd=5)
        self.statuslabel = Label(window, text="Введите номер теста от 1 до 10\n1-2 Биология\n3-4 Информатика\n5-6 "
                                              "Логика\n7-8 Социология"
                                              "\n9-10 Физическая культура", wraplength=600)
        self.entry = Entry(window)
        self.loadbutton = Button(window, text="Выбрать тест", command=self.open_test)
        self.statuslabel.pack()
        self.entry.pack()
        self.loadbutton.pack()
        window.pack()

    def open_test(self):
        try:
            a = int(self.entry.get())
            if a not in range(1, 11):
                raise ValueError
        except ValueError:
            messagebox.showerror('Ошибка ввода', 'Введите число от 1 до 10')
        else:
            if a == 1:
                test = Test("Программа тестирования по Биологии", testlibrary.test_1)
            elif a == 2:
                test = Test("Программа тестирования по Биологии", testlibrary.test_2)
            elif a == 3:
                test = Test("Программа тестирования по Информатике", testlibrary.test_3)
            elif a == 4:
                test = Test("Программа тестирования по Информатике", testlibrary.test_4)
            elif a == 5:
                test = Test("Программа тестирования по Логике", testlibrary.test_5)
            elif a == 6:
                test = Test("Программа тестирования по Логике", testlibrary.test_6)
            elif a == 7:
                test = Test("Программа тестирования по Социологии", testlibrary.test_7)
            elif a == 8:
                test = Test("Программа тестирования по Социологии", testlibrary.test_8)
            elif a == 9:
                test = Test("Программа тестирования по Физической культуре", testlibrary.test_9)
            elif a == 10:
                test = Test("Программа тестирования по Физической культуре", testlibrary.test_10)

            TestInterface(test)
