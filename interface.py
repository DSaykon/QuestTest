from tkinter import *


class TestInterface(Toplevel):
    """Class Interface for programme QuestTest"""

    def __init__(self, test):
        self.root = Toplevel()
        self.root.title(test.title)
        self.root.geometry("850x350")
        self.font = "Helvetica 12 bold"
        self.lbl_text = StringVar()
        self.lbl_text.set('{}\nДля начала нажмите "Старт"'.format(test.title))
        self.lbl = Label(self.root, textvariable=self.lbl_text, font=self.font, wraplength=600)
        self.lbl.pack(side=TOP)
        self.checkbtn_list = []
        self.score = 0
        self.variant = StringVar()
        self.variant.set(0)
        self.n = 0
        self.lbl_checked = Label(self.root, font="Helvetica 12 italic")
        self.lbl_checked.pack(side=BOTTOM)
        self.btn = Button(self.root, text="Старт", font="Helvetica 12 bold", command=self.change_lbl_text)
        self.btn.pack(side=BOTTOM)
        self.test = test

    # Изменение надписей
    def change_lbl_text(self):
        if self.n < self.test.total_questions:
            self.btn.config(text="Следующий вопрос", state=DISABLED, command=self.next_quest)
            self.lbl_text.set("Вопрос № {}\n{}".format(self.n + 1, self.test.test_question_list[self.n].text))
            self.set_check_btn()
            self.lbl_checked.config(text="\nНабрано баллов: {} / {}".format(self.score, self.n + 1))
        else:
            self.end()

    # Обновления для каждого нового вопроса в тесте
    def next_quest(self):
        self.n += 1
        self.variant.set(0)
        self.remove_check_btn()
        self.change_lbl_text()

    # Создание выбора через галочку
    def set_check_btn(self):
        for key, value in self.test.test_question_list[self.n].variant_of_answer.items():
            ch = Checkbutton(self.root, text="{}) {}".format(key, value), font="Helvetica 12",
                             onvalue=key, variable=self.variant, command=self.checked)
            ch.pack()
            self.checkbtn_list.append(ch)

    # Проверка правильности ответа
    def checked(self):
        if self.variant.get() == self.test.test_question_list[self.n].correct_variant:
            self.score += 1
            self.btn.config(state=NORMAL)
            self.lbl_checked.config(text="Правильно!\nНабрано баллов: {} / {}".format(self.score, self.n + 1))
        else:
            self.lbl_checked.config(text="Вы ошиблись.\nНабрано баллов: {} / {}".format(self.score, self.n + 1))
            self.btn.config(state=NORMAL)
        self.change_check_btn()

    # Изменение цвета при проверке ответа
    def change_check_btn(self):
        for ch in self.checkbtn_list:
            ch.config(state=DISABLED)
            if ch["onvalue"] == self.test.test_question_list[self.n].correct_variant:
                ch.config(disabledforeground="#000", bg="#0f0")
            elif ch["onvalue"] == self.variant.get():
                ch.config(disabledforeground="#000", bg="#f00")

    # Очистка окна от галочек
    def remove_check_btn(self):
        if self.checkbtn_list:
            for ch in self.checkbtn_list:
                ch.destroy()
            self.checkbtn_list.clear()

    # Завершение теста и вывод результата
    def end(self):
        self.remove_check_btn()
        self.lbl_checked.config(text="Тест завершён.\nНабрано баллов: {} / {}".format(self.score, self.n))
        self.lbl_text.set("Вопросы закончились.\nДля прохождения другого теста - закройте окно."
                          "\nДля прохождения теста повторно - нажмите кнопку внизу.")
        self.btn.config(text="Пройти этот тест снова", command=self.reset)

    # Обнуляет переменные в начальное положение
    def reset(self):
        self.n = 0
        self.score = 0
        self.variant.set(0)
        self.remove_check_btn()
        self.lbl_text.set('{}\nДля начала нажмите "Старт"'.format(self.test.title))
        self.lbl_checked.config(text='')
        self.btn.config(text="Старт", command=self.change_lbl_text)
