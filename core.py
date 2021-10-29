from testlibrary import *


class Test:
    """Class Test for programme QuestTest"""

    def __init__(self, title='test', test_question_list=None):
        if test_question_list is None:
            test_question_list = []
        self.title = title
        self.test_question_list = test_question_list
        self.total_questions = len(test_question_list)


a = 0
while a not in range(1, 10):
    try:
        a = int(input("Введите номер теста от 1 до 10.\n1-2 Биология\n3-4 Информатика\n5-6 Логика\n7-8 Социология"
                      "\n9-10 Физическая культура\n"))
    except:
        print("Введите число!!!")
if a == 1:
    test = Test("Программа тестирования по Биологии", test_1)
elif a == 2:
    test = Test("Программа тестирования по Биологии", test_2)
elif a == 3:
    test = Test("Программа тестирования по Информатике", test_3)
elif a == 4:
    test = Test("Программа тестирования по Информатике", test_4)
elif a == 5:
    test = Test("Программа тестирования по Логике", test_5)
elif a == 6:
    test = Test("Программа тестирования по Логике", test_6)
elif a == 7:
    test = Test("Программа тестирования по Социологии", test_7)
elif a == 8:
    test = Test("Программа тестирования по Социологии", test_8)
elif a == 9:
    test = Test("Программа тестирования по Физической культуре", test_9)
elif a == 10:
    test = Test("Программа тестирования по Физической культуре", test_10)
