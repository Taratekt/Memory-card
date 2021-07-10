
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,
QPushButton, QLabel, QVBoxLayout, QHBoxLayout,
QMessageBox, QRadioButton, QGroupBox, QButtonGroup
)
from random import shuffle

class Question():
    def __init__(self, question, right_ans, wrong1, wrong2, wrong3):
        self.question = question
        self.right_ans = right_ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

q_list = []
q_list.append(Question('Государственный язык Бразилии', 'Португальский',
'Испанский', 'Бразильский', 'Итальянский'))
q_list.append(Question('Какого цвета нет на флаге РФ', 'Зелёный',
'Красный', 'Синий', 'Белый'))
q_list.append(Question('Национальная хижина якутов', 'Ураса',
'Юрта', 'Иглу', 'Хата'))
q_list.append(Question('При каком правителе Россия стала империей', 'Пётр I',
'Екатерина II', 'Александр I', 'Алексей Михайлович'))

#создание окна приложения
app = QApplication

#создание окна приложения
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(420,280)

text = QLabel('Вопрос') #текст вопроса
title = 'Ответить'
button = QPushButton(title) #кнопка

#группа вопроса с ответами
radiogroup = QGroupBox('Варианты ответа')
var1 = QRadioButton('Ответ 1')
var2 = QRadioButton('Ответ 2')
var3 = QRadioButton('Ответ 3')
var4 = QRadioButton('Ответ 4')
radio = QButtonGroup()
radio.addButton(var1)
radio.addButton(var2)
radio.addButton(var3)
radio.addButton(var4)
lan1 = QHBoxLayout()
lan2 = QVBoxLayout()
lan3 = QVBoxLayout()
lan2.addWidget(var1)
lan2.addWidget(var2)
lan3.addWidget(var3)
lan3.addWidget(var4)
lan1.addLayout(lan2)
lan1.addLayout(lan3)
radiogroup.setLayout(lan1)

#группа проверки ответа
ansgroup = QGroupBox('Результат')
text2 = QLabel('Правильно/неправильно')
ans = QLabel('Правильный ответ')
lal = QVBoxLayout()
lal.addWidget(text2, alignment=Qt.AlignLeft)
lal.addWidget(ans, alignment=Qt.AlignCenter)
ansgroup.setLayout(lal)

#основные направялющие окна
lnai1 = QHBoxLayout()
lnai3 = QHBoxLayout()
lnai1.addWidget(text, alignment = Qt.AlignHCenter)
lnai3.addWidget(button, stretch = 2)
lnai = QVBoxLayout()
lnai.addLayout(lnai1)
lnai.addWidget(radiogroup)
lnai.addWidget(ansgroup)
lnai.addLayout(lnai3)
lnai.setSpacing(50)
main_win.setLayout(lnai)

#функции обработчики
def show_q():
    ansgroup.hide()
    radiogroup.show()
    title = 'Ответить'
    button.setText(title)
    radio.setExclusive(False)
    var1.setChecked(False)
    var2.setChecked(False)
    var3.setChecked(False)
    var4.setChecked(False)
    radio.setExclusive(True)
def show_r():
    radiogroup.hide()
    ansgroup.show()
    title = 'Следующий вопрос'
    button.setText(title)

answers = [var1, var2, var3, var4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_ans)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    text.setText(q.question)
    ans.setText(q.right_ans)
    show_q()

def show_correct(res):
    text2.setText(res)
    show_r()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')

def next_q():
    main_win.cur_q += 1
    main_win.total += 1
    if main_win.cur_q >= len(q_list):
        result = QMessageBox()
        rating = round(main_win.score / main_win.total * 100, 2)
        if rating >= 50:
            result.setText('Молодец!\nТы прошел тест!\n'+str(rating)+'%')
        else:
            result.setText('Увы!\nТы не прошел тест!\n'+str(rating)+'%')
        result.exec_()
        main_win.close()
    else:
        q = q_list[main_win.cur_q]
        ask(q)

def click_ok():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_q()

#запуск программы
main_win.cur_q = -1
main_win.total = -1
main_win.score = 0
next_q()
ansgroup.hide()

button.clicked.connect(click_ok)
main_win.show()
app.exec_()