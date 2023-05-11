#создай приложение для запоминания информации
#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
QApplication, QWidget, QPushButton, QHBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QButtonGroup, QVBoxLayout)
from random import randint, shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(
Question('Государственный язык Бразилии', 'Португальский','Английский', 'Испанский','Бразильский'))
question_list.append(
Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
question_list.append(
Question('Национальная хижина якутов?', 'Ураса', 'Юрта', 'Иглу', 'Хата'))



app = QApplication([])
button_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире!')
RadioGroupBox = QGroupBox("Варианты ответов")
answer1 = QRadioButton('Вариант 1')
answer2 = QRadioButton('Вариант 2')
answer3 = QRadioButton('Вариант 3')
answer4 = QRadioButton('Вариант 4')
RadioGroup = QButtonGroup()
RadioGroup.addButton(answer1)
RadioGroup.addButton(answer2)
RadioGroup.addButton(answer3)
RadioGroup.addButton(answer4)
layout_answer1 = QHBoxLayout()
layout_answer2 = QHBoxLayout()
layout_answer3 = QHBoxLayout()
layout_answer2.addWidget(answer1)
layout_answer2.addWidget(answer2)
layout_answer3.addWidget(answer3)
layout_answer3.addWidget(answer4)
layout_answer1.addLayout(layout_answer2)
layout_answer1.addLayout(layout_answer3)
RadioGroupBox.setLayout(layout_answer1)

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('Прав ты или нет')
lb_Correct = QLabel('Ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment = Qt.AlignHCenter, stretch = 2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)

AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(button_OK, stretch = 2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2, stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch = 1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button_OK.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    button_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    answer1.setChecked(False)
    answer2.setChecked(False)
    answer3.setChecked(False)
    answer4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [answer1, answer2, answer3, answer4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика: \n - Всего вопросов: ', window.total, '\n - Правильно!')
        print('Рейтинг:', (window.score/window.total * 100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг: ', (window.score/window.total * 100), '%')

def next_question():
    window.total += 1
    print('Статистика: \n - Всего вопросов: ', window.total, '\n - Правильно!')
    cur_question = randint(0, len(question_list) - 1)

    q = question_list[cur_question]
    ask(q)

def click_OK():
    if button_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()
window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')

button_OK.clicked.connect(click_OK)

window.score = 0
window.total = 0
next_question()
window.resize(400, 300)
window.show()
app.exec()