# класс Тестовый вопрос
class TestQuestion:
    def __init__(self, text, correct_variant, variant_of_answer):
        self.text = text
        self.correct_variant = correct_variant
        self.variant_of_answer = variant_of_answer


test_1 = [TestQuestion("Биология:\nНа нашей планете представлены несколько сред жизни", 'c',
                       {'a': 'океаны и материки', 'b': 'вода и суша',
                        'c': 'водная, наземно-воздушная, почва и живой организм',
                        'd': 'литосфера, гидросфера, атмосфера, биосфера', 'e': 'среда обитания и местообитание'}),
          TestQuestion(
              "Биология:\nСовокупность особей населяющих толщу воды и не способных переноситься течением, называется",
              "a",
              {'a': 'нейстон', 'b': 'бентос', 'c': 'планктон'}),
          TestQuestion(
              "Биология:\nПлотность популяции как правило на ранних стадиях её развития стремительно возрастает, "
              "далее несколько снижается и практически останавливается. Выберите причину этого процесса",
              "c",
              {'a': 'исчерпывается ресурс размножения особей, они больше не могут оставлять потомство',
               'b': 'это продиктовано биологическими особенностями вида',
               'c': 'достигается предел ёмкости среды в данных условиях'}),
          TestQuestion("Биология:\nОрганизмы, обитающие в толще воды и свободно плавающие, входят в группу", 'c',
                       {'a': 'нейстона', 'b': 'бентоса', 'c': 'нектона'}),
          TestQuestion("Биология:\nВ чем особенность организма как среды обитания?", 'c',
                       {'a': 'постоянное движение', 'b': 'постоянная влажность', 'c': 'постоянная температура'})]

test_2 = [TestQuestion(
    "Биология:\nКоличество особей данного вида на единице площади или в единице объема (например, для планктона)", 'a',
    {'a': 'плотность популяции', 'b': 'все перечисленное', 'c': 'биомасса видовое разнооразие'}),
          TestQuestion("Биология:\nСовокупность организмов обитающих на дне водоемов называется", "c",
                       {'a': 'планктон', 'b': 'нектон', 'c': 'бентос'}),
          TestQuestion("Биология:\nУсловиями среды можно назвать", "d",
                       {
                           'a': 'факторы, воздействие которых на организм не зависит от их потребления другими '
                                'организмами',
                           'b': 'климат', 'c': 'взаимоотношения организмов в сообществе',
                           'd': 'все факторы, оказывающие влияние на организм', 'e': 'абиотические факторы'}),
          TestQuestion(
              "Биология:\nВсе компоненты природной среды, влияющие на состояние организмов, популяций, сообществ, "
              "называют",
              "d",
              {'a': 'движущими силами эволюции', 'b': 'биотическими факторами', 'c': 'абиотическими факторами',
               'd': 'экологическими факторами'}),
          TestQuestion(
              "Биология:\nРыбы, обитающие в постоянно холодных водах у берегов Антарктиды, иногда при температурах "
              "ниже 0 С, относятся к группе",
              "c",
              {'a': 'мезотермофилов', 'b': 'эвритермофилов', 'c': 'криофилов', 'd': 'термофилов'})]

test_3 = [TestQuestion("Информатика:\nПредшественницей сети Internet можно считать", "a",
                       {'a': 'Сеть ARPANET', 'b': 'Сеть MSN', 'c': 'Сеть AOL', 'd': 'Сеть RELCOM'}),
          TestQuestion("Информатика:\nИнформационное общество – это общество, в котором.", "c",
                       {'a': 'Изобретены компьютеры.', 'b': 'Созданы глобальные компьютерные сети.',
                        'c': 'Большая часть работоспособного населения занимается обработкой информации.',
                        'd': 'Большая часть населения владеет персональным компьютером.'}),
          TestQuestion("Информатика:\nЧто такое датаграмма?", "b",
                       {'a': 'Пакет сеансового уровня сети Internet.',
                        'b': 'Пакет системного (сетевого и транспортного) уровня сети Internet.',
                        'c': 'Пакет аппаратного уровня сети Internet', 'd': 'Пакет прикладного уровня сети Internet.'}),
          TestQuestion("Информатика:\nСпам это", "c",
                       {'a': 'Поток приглашений от постоянных корреспондентов',
                        'b': 'Поток писем с предложением работы',
                        'c': 'Поток рекламных писем, засоряющих почтовый ящик',
                        'd': 'Поток писем с предложением услуг'}),
          TestQuestion("Информатика:\nЧто такое октет?", "c",
                       {'a': 'Часть доменного имени', 'b': 'Часть URL-адреса', 'c': 'Часть IP-адреса',
                        'd': 'Часть mail– адреса'})]

test_4 = [TestQuestion("Информатика:\nПротокол TCP/IPотносится", "c",
                       {'a': 'К аппаратному уровню сети Internet.', 'b': 'К сеансовому уровню сети Internet.',
                        'c': 'К системному (сетевому или транспортному) уровню сети Internet.',
                        'd': 'К прикладному уровню сети Internet.'}),
          TestQuestion("Информатика:\nВ каком году создана сеть ARPANET?", "b",
                       {'a': '1982', 'b': '1969', 'c': '1973', 'd': '1981'}),
          TestQuestion("Информатика:\nЧто такое программа-сервер ?", "a",
                       {'a': 'Программа, принимающая и выполняющая запросы',
                        'b': 'Программа, формирующая запросы и обрабатывающая результаты этих запросов.',
                        'c': 'Программа, управляющая трафиком сети',
                        'd': 'Программа, контролирующая целостность передачи данных.'}),
          TestQuestion("Информатика:\nВ IP-заголовок записывается.", "a",
                       {'a': 'IP-адрес назначения иIP-адрес отправителя.', 'b': 'URL-адрес запрашиваемого ресурса.',
                        'c': 'Контрольная сумма байт и информация для сборки прикладного пакета.',
                        'd': 'Информация о формате передаваемого файла.'}),
          TestQuestion("Информатика:\nВ каком году появилась сеть CERN?", "b",
                       {'a': '1982', 'b': '1981', 'c': '1969', 'd': '1973'})]

test_5 = [TestQuestion("Логика:\nПростое суждение «Некоторые простые числа не являются четными» является", "d",
                       {'a': 'общеотрицательным', 'b': 'общеутвердительным', 'c': 'единичным',
                        'd': 'частноотрицательным', 'e': 'частноутвердительным'}),
          TestQuestion("Логика:\nПонятия «литературный жанр» и «роман», «пьеса» находятся в отношении", "d",
                       {'a': 'противоречия', 'b': 'подчинения', 'c': 'пересечения', 'd': 'соподчинения',
                        'e': 'противоположности'}),
          TestQuestion("Логика:\nПростое суждение «Лень никогда не приводит к добру» является", "c",
                       {'a': 'общеутвердительнымя', 'b': 'единичным', 'c': 'общеотрицательным',
                        'd': 'частноутвердительным', 'e': 'частноотрицательным'}),
          TestQuestion("Логика:\nПонятия «чувство» и «нежность» находятся в отношении", "c",
                       {'a': 'соподчинения', 'b': 'пересечения', 'c': 'подчинения', 'd': 'противоположности',
                        'e': 'противоречия'}),
          TestQuestion(
              "Логика:\nОпределите модальность суждения: «По мнению ряда ученых, некоторые континенты разобщены в "
              "результаты дрейфа»:",
              "c",
              {'a': 'суждение возможное', 'b': 'суждение фактически необходимое', 'c': 'суждение проблематично',
               'd': 'суждение невозможное', 'e': 'суждение случайное'})]

test_6 = [TestQuestion("Логика:\nПонятия «юрист» и «адвокат» находятся в отношении", "c",
                       {'a': 'противоречия', 'b': 'соподчинения', 'c': 'подчинения', 'd': 'противоположности',
                        'e': 'пересечения'}),
          TestQuestion("Логика:\nПонятия «чувство» и «восхищение» находятся в отношении", "c",
                       {'a': 'противоречия', 'b': 'соподчинения', 'c': 'подчинения', 'd': 'противоположности',
                        'e': 'пересечения'}),
          TestQuestion("Логика:\nПростое суждение «Ни один человек не является себе врагом» является", "c",
                       {'a': 'частноутвердительным', 'b': 'общеутвердительным', 'c': 'общеотрицательным',
                        'd': 'частноотрицательным', 'e': 'единичным'}),
          TestQuestion("Логика:\nПонятия «спортивная игра» и «теннис» находятся в отношении", "e",
                       {'a': 'противоречия', 'b': 'пересечения', 'c': 'соподчинения', 'd': 'противоположности',
                        'e': 'подчинения'}),
          TestQuestion("Логика:\nПонятия «литературный жанр» и «очерк», «рассказ», «роман» находятся в отношении", "e",
                       {'a': 'противоречия', 'b': 'пересечения', 'c': 'подчинения', 'd': 'противоположности',
                        'e': 'соподчинения'})]

test_7 = [TestQuestion("Социология:\nПричиной появления слухов социологи считают", "c",
                       {'a': 'активность позиции официальных властей', 'b': 'активность средств массовой информации',
                        'c': 'отсутствие интереса к событиям', 'd': 'недоверие к официальным источникам информации'}),
          TestQuestion(
              "Социология:\nЯзыковой союз отличается от языковой семьи первостепенной значимостью _________ языков",
              "b",
              {'a': 'схожей морфологии', 'b': 'фонологического сходства', 'c': 'генетической общности',
               'd': 'территориальной близости'}),
          TestQuestion(
              "Социология:\nМеры воздействия социальной группы на поведение индивида, отклоняющееся от социальных "
              "ожиданий, норм и ценностей, называются",
              "b",
              {'a': 'бойкоты', 'b': 'санкции', 'c': 'прессинги', 'd': 'наказания'}),
          TestQuestion(
              "Социология:\nСреди социальных движений выделяют «старые» и «новые». Разновидностью «новых» является "
              "________ движение",
              "d",
              {'a': 'рабочее', 'b': 'экологическое', 'c': 'фермерское', 'd': 'монархическое'}),
          TestQuestion("Социология:\nДве черты характерные для массовой коммуникации — это", "b",
                       {'a': 'бесцельный характер общения и приватность сообщений',
                        'b': 'организованный характер общения и публичность сообщений'})]

test_8 = [TestQuestion("Социология:\nОсновной функцией семьи выступает", "a",
                       {'a': 'функция социализации', 'b': 'функция репродуктивная', 'c': 'бытовая функция',
                        'd': 'сексуальная функция'}),
          TestQuestion(
              "Социология:\n________ – это тип социальной стратификации, основывающийся на крайней форме социального "
              "неравенства, когда одни члены общества являются собственностью других",
              "b",
              {'a': 'Посткапиталистическое общество', 'b': 'Рабство', 'c': 'Капитализм', 'd': 'Феодализм'}),
          TestQuestion("Социология:\nСогласно парсоновской концепции общества, подсистема «родство» обеспечивает", "d",
                       {'a': 'приспособление индивидов и групп к окружающей среде',
                        'b': 'интеграцию индивидуумов и общностей в единый коллектив',
                        'c': 'реализацию целей общественного развития',
                        'd': 'поддержание устойчивости и стабильности социальных взаимосвязей'}),
          TestQuestion("Социология:\n______ следует считать обладателем такого социального статуса, как люмпен", "b",
                       {'a': 'Студента', 'b': 'Бомжа', 'c': 'Рабочего', 'd': 'Банкира'}),
          TestQuestion("Социология:\nОбраз мудрого правителя у Н. Макиавелли ассоциировался с", "d",
                       {'a': 'лисой', 'b': 'волком', 'c': 'ослом', 'd': 'тигром'})]

test_9 = [TestQuestion("Физическая культура:\nСамый высокий ранг соревнований:", "b",
                       {'a': 'чемпионат мира', 'b': 'Олимпийские игры'}),
          TestQuestion(
              "Физическая культура:\nНаилучшие показатели работоспособности человека характеризуются следующими "
              "значениями индекса Руффье:",
              "c",
              {'a': '0,7', 'b': '0,8', 'c': '0,5', 'd': '0,6'}),
          TestQuestion("Физическая культура:\nК показателям физического развития относятся:", "a",
                       {'a': 'масса тела', 'b': 'рост', 'c': 'частота сердечных сокращений'}),
          TestQuestion("Физическая культура:\nК показателям физического развития относятся:", "a",
                       {'a': 'вес и рост', 'b': 'время задержки дыхания и окружность грудной клетки',
                        'c': 'артериальное давление и частота сердечных сокращений',
                        'd': 'сила, выносливость, скорость'}),
          TestQuestion("Физическая культура:\nС увеличением значения индекса Руффье работоспособность:", "a",
                       {'a': 'снижается', 'b': 'возрастает'})]

test_10 = [TestQuestion("Физическая культура:\nСамый быстрый бег:", "c",
                        {'a': 'марафонский', 'b': 'стайерский', 'c': 'спринтерский', 'd': 'трусцой'}),
           TestQuestion("Физическая культура:\nК тестам функционального состояния относятся:", "a",
                        {'a': 'частота сердечных сокращений и время задержки дыхания',
                         'b': 'сила и частота сердечных сокращений', 'c': 'частота дыхания и сила'}),
           TestQuestion("Физическая культура:\nС увеличением значения весоростового индекса:", "a",
                        {'a': 'возрастает избыток массы тела', 'b': 'снижается избыток массы тела',
                         'c': 'возрастает дефицит массы тела', 'd': 'снижается дефицит массы тела'}),
           TestQuestion("Физическая культура:\nФизическое развитие весоростовой индекс:", "a",
                        {'a': 'характеризует', 'b': 'не характеризует'}),
           TestQuestion("Физическая культура:\nВзрывную силу характеризуют тесты:", "b",
                        {'a': 'прыжки в длину и челночный бег', 'b': 'прыжки в длину и высоту',
                         'c': 'прыжки в длину и через скакалку'})]
