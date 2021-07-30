import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton
from PyQt5.QtCore import QCoreApplication
import os

def start_tetris():
    os.system('python tetris.py')

def start_snake():
    os.system('python zmeika.py')

def start_space():
    os.system('python test.py')

class Example(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.init_ui()

    def init_ui( self ):
        self.setFixedSize(700,700)
        self.move(300,300)
        self.setWindowTitle('ARCADE')
        self.setStyleSheet('background-color: rgb(184, 205, 228);'
                                    'color: rgb(37, 16, 37);'
                                    'font-size: 22px;')
        self.label = QLabel(self)
        self.label.setText('ARCADE')
        self.label.move(250,100)
        self.label.setStyleSheet('font-size:52px;')
        self.button_tetris = QPushButton('Тетрис ',self)
        self.button_tetris.resize(200,50)
        self.button_tetris.move(250,300)
        self.button_tetris.clicked.connect(start_tetris)
        self.button_tetris.setStyleSheet( 'background-color: rgb(24, 48, 73);color: honeydew;' )
        self.button_snake = QPushButton( 'Змейка' , self )
        self.button_snake.resize( 200 , 50 )
        self.button_snake.move( 250 ,200 )
        self.button_snake.clicked.connect( start_snake )
        self.button_snake.setStyleSheet( 'background-color: rgb(24, 48, 73);color: honeydew;' )
        self.button_space = QPushButton( 'Space invaidors' , self )
        self.button_space.resize( 200 , 50 )
        self.button_space.move( 250 ,400 )
        self.button_space.clicked.connect( start_space )
        self.button_space.setStyleSheet( 'background-color: rgb(24, 48, 73);color: honeydew;' )
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Example()
    sys.exit(app.exec())