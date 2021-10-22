from tkinter import *
from core import *


class Test:
	def __init__(self, title='test', test_question_list=[]):
		self.title = title
		self.test_question_list = test_question_list
		self.total_questions = len(test_question_list)

# интерфейс для теста
class TestInterface:
	def __init__(self, test):
		self.root = Tk()
		self.root.title(test.title)
		self.root.geometry("900x300")
		self.font = "Arial 12 bold"
		self.lbl_text = StringVar()
		self.lbl_text.set('Для начала теста нажмите "Старт"')
		self.lbl = Label(textvariable=self.lbl_text, font=self.font, wraplength=600)
		self.lbl.pack(side=TOP)
		self.checkbtn_list = []
		self.score = 0
		self.variant = StringVar()
		self.variant.set(0)
		self.n = 0
		self.lbl_checked = Label(font="Arial 12 bold")
		self.lbl_checked.pack(side=BOTTOM)
		self.btn = Button(text="Старт", font="Arial 12 bold", command=self.change_lbl_text)
		self.btn.pack(side=BOTTOM)
		self.root.mainloop()

	# изменение надписей
	def change_lbl_text(self):
		if self.n < test.total_questions:
			self.btn.config(text="Следующий вопрос", state=DISABLED, command=self.next_quest)
			self.lbl_text.set("Вопрос № {}\n{}".format(self.n+1, test.test_question_list[self.n].text))
			self.set_check_btn()
			self.lbl_checked.config(text="\nНабрано баллов: {} / {}".format(self.score, self.n+1))
		else:
			print("Вопросов больше нет")
			self.end()

	# создание выбора через галочку
	def set_check_btn(self):
		for key, value in test.test_question_list[self.n].variant_of_answer.items():
			ch = Checkbutton(text="{}) {}".format(key, value), font="Arial 12 bold", onvalue=key, variable=self.variant, command=self.checked)
			ch.pack()
			self.checkbtn_list.append(ch)

	# очистка окна
	def remove_check_btn(self):
		if self.checkbtn_list:
			for ch in self.checkbtn_list:
				ch.destroy()
			self.checkbtn_list.clear()

	# изменение цвета при проверке ответа
	def change_check_btn(self):
		for ch in self.checkbtn_list:
			ch.config(state=DISABLED)
			if ch["onvalue"] == test.test_question_list[self.n].correct_variant:
				ch.config( disabledforeground="#000", bg="#0f0")
			elif ch["onvalue"] == self.variant.get():
				ch.config(disabledforeground="#000", bg="#f00")

	# проверка правильности ответа
	def checked(self):
		if self.variant.get() == test.test_question_list[self.n].correct_variant:
			self.score += 1
			self.btn.config(state=NORMAL)
			self.lbl_checked.config(text="Правильно\nНабрано баллов: {} / {}".format(self.score, self.n+1))
		else:
			self.lbl_checked.config(text="Вы ошиблись\nНабрано баллов: {} / {}".format(self.score, self.n+1))
			self.btn.config(state=NORMAL)
		self.change_check_btn()

	# обнуляет переменные в начальное положение
	def reset(self):
		self.n = 0
		self.score = 0
		self.variant.set(0)
		self.remove_check_btn()
		self.lbl_text.set('Для начала теста нажмите "Старт"')
		self.lbl_checked.config(text='')
		self.btn.config(text="Старт", command=self.change_lbl_text)

	# обновления для каждого нового вопроса в тесте
	def next_quest(self):
		self.n += 1
		self.variant.set(0)
		self.remove_check_btn()
		self.change_lbl_text()

	# Завершение теста и вывод результата
	def end(self):
		self.remove_check_btn()
		self.lbl_checked.config(text="Тест завершён\nНабрано баллов: {} / {}".format(self.score, self.n))
		self.lbl_text.set("Вопросы закончились\nДля прохождения другого случайного теста перезапустите программу"
						  "\nДля прохождения теста повторно нажмите кнопку внизу")
		self.btn.config(text="Пройти этот тест снова", command=self.reset)

test = Test("Программа тестирования", test_question_list)