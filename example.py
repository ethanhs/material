from material import *
import sys
from PySide.QtCore import *
from PySide.QtGui import *


class Page_1(Page):
    def __init__(self,parent=None):
        Page.__init__(self,parent)

class Example_App(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setStyleSheet("background-color: #ffffff")
        self.setWindowTitle("Material Design Example")
        self.backgroundwidget = QWidget(self)
        self.backgroundwidget.setStyleSheet("background-color:rgb(0,255,255,0)")
        self.backgroundwidget.resize(200, 200)
        self.button = FloatingActionButton(parent=self)
        self.button.move(100, 100)
        self.switch = Switch(QColor(50, 50, 255), 30, self)
        self.switch.move(100, 200)
        self.button2 = RaisedButton("Hi",'#29b6f6', parent=self)
        self.button2.move(100, 275)
        self.button3 = FlatButton("Hi", parent=self)
        self.button3.move(100, 350)
        self.topbar = TopBar("#bbbbbb", 50, self)
        self.tab = TabBar(self.topbar)
        self.tabspace = QTabWidget(self)
        self.tabspace.setTabBar(self.tab)
        self.tab.addTab("Foo")
        self.tab.addTab("bar")
        self.tab.addTab("Networks")
        self.tab.addTab("Nothing")
        self.tabspace.resize(self.tabspace.parent().width(), self.tab.tabSizeHint(0).height())
        self.slide = Slider(self)
        self.slide.move(200, 450)
        self.slide.resize(20, 100)
        self.slide2 = Slider(self)
        self.slide2.move(100, 400)
        self.slide2.setOrientation(Qt.Horizontal)
        self.check = CheckBox(self)
        self.check.move(300, 450)
        self.progbar = ProgressBar(self)
        self.progbar.move(300, 500)
        self.progbar.resize(150, 10)
        self.progbar.setValue(30)
        self.line=LineEdit("#29b6f6",self)
        self.line.move(400,200)
        self.line.resize(150,50)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Example_App()
    win.showMaximized()
    sys.exit(app.exec_())