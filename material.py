import sys, time
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtCore import Qt
from PyQt4.QtSvg import QSvgRenderer

class FloatingActionButton(QPushButton):
    def __init__(self,color=QColor(243,40,109,255), radius=50,icon="plus.png",parent=None,*args):
        super(FloatingActionButton, self).__init__(parent)
        if icon:
            self.pixmap=QPixmap(icon)
        self.setMouseTracking(True)
        self.effect=QGraphicsDropShadowEffect(self.parent())
        self.effect.setXOffset(4)
        self.effect.setBlurRadius(4)
        self.effect.setColor(QColor(0,0,0,40))
        self.setGraphicsEffect(self.effect)
        self.color=color
        self.radius=radius
        self.resize(self.radius+1,self.radius+1)
        self.setMaximumSize(self.size())
        self.setMinimumSize(self.size())
        self.effect_size=self.radius
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.setBrush(self.color)
        if self.effect_size==self.radius:
            painter.drawEllipse(1,1,self.radius-1,self.radius-1)
            painter.drawPixmap(QRect(14,14,self.radius/2,self.radius/2),self.pixmap)
        else:
            painter.drawEllipse(self.width()/2,self.height()/2,self.effect_size,self.effect_size)
        painter.end()
    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.animate()
    def animate(self):
        while self.effect_size>1:
            self.effect_size-=2
            self.repaint()
            time.sleep(0.008)

class RaisedButton(QPushButton):
    def __init__(self,text,size=QSize(80,30),color=QColor(66,165,245),parent=None):
        super(RaisedButton, self).__init__(parent)
        self.resize(size)
        self.isFlat=True
        self.color=color
        self.setText(text)
        self.effect=QGraphicsDropShadowEffect(self.parent())
        self.effect.setOffset(3)
        self.effect.setColor(QColor(0,0,0,40))
        self.setGraphicsEffect(self.effect)
        self.press=False
        with open("QPushButton-Raised.qss") as f:
            dat=f.read()
            color1=color.name()
            color2=color.lighter().name()
            dat=dat % (str(color1), str(color2))
            self.setStyleSheet(dat)
    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.effect.setEnabled(False)
            self.press=True
    def mouseReleaseEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.effect.setEnabled(True)
            self.press=False
class FlatButton(QPushButton):
    def __init__(self,text,size=QSize(80,30),color=QColor(66,165,245),parent=None):
        super(FlatButton, self).__init__(parent)
        self.resize(size)
        self.setObjectName("FlatButton")
        self.color=color
        self.setText(text)
        self.press=False
        with open("QPushButton-Flat.qss") as f:
            dat=f.read()
            color1=color.name()
            dat=dat % (str(color1))
            self.setStyleSheet(dat)

class Switch(QCheckBox):
    """Switch(tuple colors=(QColor(50,50,50),QColor(50,50,255)),int diameter,QWidget parent"""
    def __init__(self,colors=(QColor(50,50,50),QColor(50,50,200)), *args):
            QCheckBox.__init__(self, *args)
            try:
                if type(colors)!=type((1,1)):
                    diameter=colors
                    colors=(QColor(50,50,50),QColor(50,50,255))
                else:
                    diameter=args[1]
                self.color1=colors[0]
                self.color2=colors[1]
            except:
                raise RuntimeError("Incorrect args. See the docs.")
            self.resize(QSize(3*float(diameter),diameter))
            self.setStyleSheet("background-color: rgb(0, 0, 0);\n" +
                      "color: rgb(255, 255, 255);\n")
            self.setChecked(True)
            self.setEnabled(True)
            self._enable = True
    def mousePressEvent(self, event):
            if self.isChecked():
                self.setChecked(False)
            else:
                self.setChecked(True)
            return QCheckBox.mousePressEvent(self, event)
    def paintEvent(self,event):
            #Size attributes
            self.setMinimumHeight(40)
            self.setMinimumWidth(100)
            self.setMaximumHeight(50)
            self.setMaximumWidth(150)
            painter = QPainter()
            painter.begin(self)
            painter.setRenderHint(QPainter.HighQualityAntialiasing)
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setRenderHint(QPainter.SmoothPixmapTransform)
            #change the look for on/off
            if self.isChecked():
                #blue fill
                brush = QBrush(self.color2)
                painter.setBrush(brush)
                painter.drawRoundedRect(0,10,self.width()-2,self.height()-20, self.height()/2-10,self.height()/2)
                brush = QBrush(QColor(0,100,255))
                painter.setBrush(brush)
                painter.drawEllipse(self.width()-self.height(),0,self.height(),self.height())
            else:
                brush = QBrush(self.color1)
                painter.setBrush(brush)
                painter.drawRoundedRect(1,10,self.width()-3,self.height()-20, self.height()/2-10,self.height()/2)
                brush = QBrush(QColor(100,100,100))
                painter.setBrush(brush)
                painter.drawEllipse(0,0,self.height(),self.height())
            painter.end()
class TabBar(QTabBar):
    def __init__(self,parent=None,*args):
        super(TabBar,self).__init__(parent)
        if len(args)==1:
            color=args[0].name()
        else:
            color="#4caf50"
        with open("QTabBar.qss") as f:
            data=f.read()
            data=data % (color)
            self.setStyleSheet(data)
class Slider(QSlider):
    def __init__(self,parent=None):
        super(Slider,self).__init__(parent)
        with open("QSlider.qss") as f:
            self.setStyleSheet(f.read())
class CheckBox(QCheckBox):
    def __init__(self,*args):
        super(CheckBox,self).__init__(*args)
        self.setMouseTracking(True)
        if tuple() in [type(i) for i in args]:
            for arg in args:
                if type(arg)==tuple():
                    color=arg
        else:
            color=(QColor(0,150,136),QColor(255,255,255))
        self.color1=color[0]
        self.color2=color[1]
        self.svgrenderer=QSvgRenderer("icons\\check.svg")

        self.check=QImage(500, 200, QImage.Format_ARGB32)
        self.resize(30,30)
        paint=QPainter(self.check)
        self.svgrenderer.render(paint)
    def paintEvent(self, event):
        painter=QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)

        self.img=QPixmap()
        if self.isChecked():
            painter.setBrush(self.color1)
            painter.drawRect(QRect(0,0,30,30))
            painter.drawPixmap(QRect(0,-5,30,40),self.img.fromImage(self.check))
        else:
            pen=QPen()
            pen.setWidth(2)
            painter.setPen(pen)
            #hand draw rect
            painter.drawLine(QPoint(0,0),QPoint(30,0))
            painter.drawLine(QPoint(30,0),QPoint(30,30))
            painter.drawLine(QPoint(0,0),QPoint(0,30))
            painter.drawLine(QPoint(0,30),QPoint(30,30))
        painter.end()
    def mouseReleaseEvent(self, event):
        print event.button()
        if event.button()==Qt.LeftButton:
            if self.isChecked():

                self.setChecked(False)
            else:
                self.setChecked(True)
            self.repaint()
class ProgressBar(QProgressBar):
    def __init__(self,*args):
        QProgressBar.__init__(self,*args)
        colorful=False
        if type(args[0])==type(bool):
            coloful=True
        if not colorful:
            with open("QProgressBar.qss") as f:
                self.setStyleSheet(f.read())

#With thanks to Chris Wheatley and his Hamburger Concept
class Hamburger(QPushButton):
    def __init__(self,color,parent=None):
        QPushButton.__init__(self,parent)
        if not color:
            self.color=QColor(255,255,255)
        else:
            self.color=color
        self.press=False
        def paintEvent(self, event):
            painter=QPainter()
            painter.begin(self)
            painter.setRenderHint(QPainter.HighQualityAntialiasing)
            painter.setRenderHint(QPainter.SmoothPixmapTransform)
            if self.press:
                pass
            else:
                #TODO

class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setStyleSheet("background-color: #ffffff")
        self.backgroundwidget=QWidget(self)
        self.backgroundwidget.setStyleSheet("background-color:rgb(0255,255,0)")
        self.backgroundwidget.resize(200,200)
        self.button =FloatingActionButton(parent=self)
        self.button.move(100,100)
        self.switch=Switch(20,self)
        self.switch.move(100,200)
        self.button2=RaisedButton("Hi",parent=self)
        self.button2.move(100,275)
        self.button3=FlatButton("Hi",parent=self)
        self.button3.move(100,350)
        self.tab=TabBar(self)
        self.tabspace=QTabWidget(self)
        self.tabspace.setTabBar(self.tab)
        self.tab.addTab("Foo")
        self.tab.addTab("bar")
        self.tabspace.resize(self.tab.count()*self.tab.tabSizeHint(0).width(),self.tab.tabSizeHint(0).height())
        self.slide=Slider(self)
        self.slide.move(200,450)
        self.slide.resize(20,100)
        self.slide2=Slider(self)
        self.slide2.move(100,400)
        self.slide2.setOrientation(Qt.Horizontal)
        self.check=CheckBox(self)
        self.check.move(300,450)
        self.progbar=ProgressBar(self)
        self.progbar.move(300,500)
        self.progbar.resize(150,10)
        self.progbar.setValue(30)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win=Window()
    win.showMaximized()
    sys.exit(app.exec_())