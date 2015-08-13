from material import *
import sys
from PySide.QtGui import QApplication


class Page_1(Page):
    def __init__(self,parent=None):
        Page.__init__(self,parent)
        person=svg2icon("icons\\person.svg",img_type=QPixmap)
        '''self.list=ListView(self)
        '''
        names=["Will","Jane","Alex","Sara","Peter","Maria"]
        messages=["Hello","How are you?","What's up?","About the app...","Out of the office","Material Design rocks!"]
        self.list=QWidget(self)
        self.list.move(4,20)
        self.list.resize(self.window().width(),self.window().height()-120)
        for name in names:
            item=ListItem(person,name,text=messages[names.index(name)],parent=self.list)
            item.resize(self.window().width(),64)
            item.move(0,names.index(name)*76)

        self.button = FloatingActionButton(parent=self)
        self.button.move(400,540)

class Page_2(Page):
    def __init__(self,parent=None):
        Page.__init__(self,parent)
        self.switch = Switch(QColor(50, 50, 255), 30, self)
        self.switch.move(self.window().width()-self.switch.width()-25, 25)
        self.autorefresh=Text("Auto-refresh messages (may use a lot of data)",parent=self)
        self.autorefresh.move(25,25)
        self.about=Text("Read the about for more",parent=self)
        self.about.move(25,75)
        self.button2 = RaisedButton("About",'#29b6f6', parent=self)
        self.button2.move(250, 75)
        self.q=Text("Would you like to agree to this question?",parent=self)
        self.q.move(25,125)
        self.check = CheckBox(self)
        self.check.move(350, 125)
        self.prompt=Text("Please enter your age",parent=self)
        self.prompt.move(25,190)
        self.line=LineEdit(self)
        self.line.move(275,175)
        self.line.resize(150,50)
        self.instructions=Text("This button makes the above wrong, useful for data evaluation",parent=self)
        self.instructions.move(25,275)
        self.button3 = FlatButton("Wrong", parent=self)
        self.button3.move(300, 300)
        QObject.connect(self.button3,SIGNAL('clicked()'),self.flat_click)
    def flat_click(self):
        self.line.wrong()






class Page_3(Page):
    def __init__(self,parent=None):
        Page.__init__(self,parent)


class Example_App(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        #Initialize the main window, which is the background
        self.resize(480,720)
        self.move(0,0)
        self.setStyleSheet("background-color: #ffffff")
        self.setWindowTitle("Material Design Example")
        self.topbar = TopBar("#ff33bb", 120, self)
        self.hamburger=Hamburger(self.topbar)
        self.hamburger.move(0,0)
        self.hamburger.setMinimumSize(64,64)
        self.tab = TabBar(self.topbar)

        self.tab.addTab("Messages")
        self.tab.addTab("Settings")
        self.tab.addTab("About this app")
        self.tabspace = QTabWidget(self.topbar)
        self.tabspace.resize(self.tabspace.window().width(), self.tab.tabSizeHint(0).height())
        self.tabspace.setTabBar(self.tab)
        self.tabspace.setStyleSheet("background-color: "+self.topbar.color)
        self.tabspace.move(4,self.topbar._height-(self.tabspace.height()-1))

        #set up the first page
        self.page_1=Page_1(self)
        self.page_1.resize(480,720)
        self.page_1.move(0,100)
        self.current_page=self.page_1

        #set up second page
        self.page_2=Page_2(self)
        self.page_2.resize(480,720)
        self.page_2.move(0,100)

        self.page_2.hide() #need to keep hidden

        #set up second page
        self.page_3=Page_3(self)
        self.page_3.resize(480,720)
        self.page_3.move(0,100)

        self.page_3.hide() #need to keep hidden

        self.page_queue=[self.page_1,self.page_2,self.page_3]
        self.tabspace.currentChanged.connect(self.change_page)

    def change_page(self, num):
        self.next_page=self.page_queue[num]
        self.current_page.hide()
        self.current_page.destroy()
        del self.current_page
        self.current_page=self.next_page
        self.current_page.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Example_App()
    win.show()
    sys.exit(app.exec_())