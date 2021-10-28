from random import randint
from testlibrary import *

class Test:
    def __init__(self, title='test', test_question_list=None):
        if test_question_list is None:
            test_question_list = []
        self.title = title
        self.test_question_list = test_question_list
        self.total_questions = len(test_question_list)


a = randint(1, 10)
if a == 1:
    test_question_list = test_1
elif a == 2:
    test_question_list = test_2
elif a == 3:
    test_question_list = test_3
elif a == 4:
    test_question_list = test_4
elif a == 5:
    test_question_list = test_5
elif a == 6:
    test_question_list = test_6
elif a == 7:
    test_question_list = test_7
elif a == 8:
    test_question_list = test_8
elif a == 9:
    test_question_list = test_9
else:
    test_question_list = test_10

test = Test("Программа тестирования", test_question_list)
