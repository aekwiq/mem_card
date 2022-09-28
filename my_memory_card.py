from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout,
        QGroupBox, QButtonGroup, QRadioButton,
        QPushButton, QLabel)
from random import shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('Кого рыбак всегда видит издалека?', 'Рыбака', 'Червяка', 'Рыбовода', 'Рыбнадзор'))
questions_list.append(Question('Через какую папку можно дефрагментировать диск в 95 Windows?', 'Корзина', 'Мой компьютер', 'Сетевое окружение', 'Мои документы'))
questions_list.append(Question('Чему равен периметр ромба со стороной 2 м?', '6 литров', '8 квадратных метров', '8 метров', '4 метра'))

app = QApplicition([])

btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире!')

RadionGroupBox = QGroupBox('''Варианты ответов''')

rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)   

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadionGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox("Результаты теста")
lb_Result
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter / Qt.AlignVCenter))
layout_line2.addWidget(RadionGroupBox)

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

AnsGroupBox = QGroupBox("Результаты теста")
lb_Result1 = QLabel('прав или нет?')
lb_Correct1 =  QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment = (Qt.AlignLeft / Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment = Qt.AlignHCenter, stretch = 2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment = (Qt.AlignHCenter / Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch = 2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2, stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch = 1)
layout_card.addStretch(1)
layout_card.addSpacing(5)

def show_result():
    ''' показать панель ответов '''
    RadioGruoupBox.hide()
    AnsGroupBox.show()
    ResultGroupBox.hide()
    btn_OK.setText('Следующий вопрос')

def show_question():
''' показать панель вопросов '''
    RadionGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_test_result():
    RadioGroupBox.hide()
    AnsGroupBox.hide()
    ResultGroupBox.show()
    btn_OK.setText('Начать заново')
    lb_Result.setText('Результат теста:' + str(window.points) + ' из ' + str(window.questions))


answer =[rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    ''' функция записывает значение вопроса и ответов соответвующие виджеты,
    при этом варианты ответов распределяются случайным образом '''
    shuffle(answers)
    answers[0]setText(q.right_answer)
    answers[1]setText(q.wrong1)
    answers[2]setText(q.wrong2)
    answers[3]setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    ''' показать результат - установим переданный текст в надпись "результат" и покажем нужную панель '''
    lb_Result.setText(res)
    show_result()

def check_answer():
    '''если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''
    if answers[0].isChecked():
        window.points += 1
        window.question += 1
        show_correct('Правильно!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            #неправильный ответ!
            window.question += 1
            show_correct('Неверно!')

def next_question()
    ''' задает следующий вопрос из списка '''
    window.cur_question = window.cur_question + 1
    if window.cur_question >= len(questions_list):
        lb_Correct.setText('Вопросы закончились!')
        btn_OK.setText('Завершить тест')
        window.cur_question = 0
    q = questions_list[window.cur_question]
    ask(q)

def click_OK():
    ''' определяет, надо ли показывать другой вопрос либо проверить ответ на этот '''
    is btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
ask('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский')
btn_OK.clicked.connect(check_answer)

window.show()
app.exed()
