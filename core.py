from random import randint
from testlibrary import *

class Test:
    """Class Test for programme QuestTest"""

    def __init__(self, title='test', test_question_list=None):
        if test_question_list is None:
            test_question_list = []
        self.title = title
        self.test_question_list = test_question_list
        self.total_questions = len(test_question_list)


a = randint(1, 10)
if a == 1:
    test_question_list = test_1
    test = Test("Программа тестирования по Биологии", test_question_list)
elif a == 2:
    test_question_list = test_2
    test = Test("Программа тестирования по Биологии", test_question_list)
elif a == 3:
    test_question_list = test_3
    test = Test("Программа тестирования по Информатике", test_question_list)
elif a == 4:
    test_question_list = test_4
    test = Test("Программа тестирования по Информатике", test_question_list)
elif a == 5:
    test_question_list = test_5
    test = Test("Программа тестирования по Логике", test_question_list)
elif a == 6:
    test_question_list = test_6
    test = Test("Программа тестирования по Логике", test_question_list)
elif a == 7:
    test_question_list = test_7
    test = Test("Программа тестирования по Социологии", test_question_list)
elif a == 8:
    test_question_list = test_8
    test = Test("Программа тестирования по Социологии", test_question_list)
elif a == 9:
    test_question_list = test_9
    test = Test("Программа тестирования по Физической культуре", test_question_list)
else:
    test_question_list = test_10
    test = Test("Программа тестирования по Физической культуре", test_question_list)


