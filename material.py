import time
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtCore import Qt
from PySide.QtSvg import QSvgRenderer


class FloatingActionButton(QPushButton):
    def __init__(self, color=QColor(243, 40, 109, 255), radius=50, icon="plus.png", parent=None, *args):
        super(FloatingActionButton, self).__init__(parent)
        if icon:
            self.pixmap = QPixmap(icon)
        self.setMouseTracking(True)
        self.effect = QGraphicsDropShadowEffect(self.parent())
        self.effect.setXOffset(4)
        self.effect.setBlurRadius(4)
        self.effect.setColor(QColor(0, 0, 0, 40))
        self.setGraphicsEffect(self.effect)
        self.color = color
        self.radius = radius
        self.resize(self.radius + 1, self.radius + 1)
        self.setMaximumSize(self.size())
        self.setMinimumSize(self.size())
        self.effect_size = self.radius

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.setBrush(self.color)
        if self.effect_size == self.radius:
            painter.drawEllipse(1, 1, self.radius - 1, self.radius - 1)
            painter.drawPixmap(QRect(14, 14, self.radius / 2, self.radius / 2), self.pixmap)
        else:
            painter.drawEllipse(self.width() / 2, self.height() / 2, self.effect_size, self.effect_size)
        painter.end()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.animate()

    def animate(self):
        while self.effect_size > 1:
            self.effect_size -= 2
            self.repaint()
            time.sleep(0.008)


class RaisedButton(QPushButton):
    """RaisedButton(str text, color, QSize size, QWidget parent=None"""
    def __init__(self, text, color,size=QSize(80, 30), parent=None):
        super(RaisedButton, self).__init__(parent)
        self.resize(size)
        if color==None:
            color=QColor(66, 165, 245)
        else:
            color=QColor(color)
        self.isFlat = True
        self.color = color
        self.setText(text)
        self.effect = QGraphicsDropShadowEffect(self.parent())
        self.effect.setOffset(3)
        self.effect.setColor(QColor(0, 0, 0, 40))
        self.setGraphicsEffect(self.effect)
        self.press = False
        with open("QPushButton-Raised.qss") as f:
            dat = f.read()
            color1 = color.name()
            color2 = color.lighter().name()
            dat = dat % (str(color1), str(color2))
            self.setStyleSheet(dat)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.effect.setEnabled(False)
            self.press = True

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.effect.setEnabled(True)
            self.press = False


class FlatButton(QPushButton):
    def __init__(self, text, size=QSize(80, 30), color=QColor(66, 165, 245), parent=None):
        super(FlatButton, self).__init__(parent)
        self.resize(size)
        self.setObjectName("FlatButton")
        self.color = color
        self.setText(text)
        self.press = False
        with open("QPushButton-Flat.qss") as f:
            dat = f.read()
            color1 = color.name()
            dat = dat % (str(color1))
            self.setStyleSheet(dat)


class Switch(QCheckBox):
    """Switch(color,diameter,QWidget parent"""
    def __init__(self, color, diameter, parent=None):
        QCheckBox.__init__(self, parent)
        self.color1 = QColor(color)
        self.color2 = QColor(50, 50, 50)
        self.resize(QSize(2 * float(diameter), diameter))
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

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        # change the look for on/off
        if self.isChecked():
            # blue fill
            brush = QBrush(self.color1)
            painter.setBrush(brush)
            painter.drawRoundedRect(0, 7, self.width() - 2, self.height() - 15, self.height() / 2 - 10,
                                    self.height() / 2)
            brush = QBrush(self.lighter(self.color1))
            painter.setBrush(brush)
            painter.drawEllipse(self.width() - self.height(), 0, self.height(), self.height())
        else:
            #gray fill
            brush = QBrush(self.color2)
            painter.setBrush(brush)
            painter.drawRoundedRect(1, 7, self.width() - 3, self.height() - 15, self.height() / 2 - 10,
                                    self.height() / 2)
            brush = QBrush(QColor(100, 100, 100))
            painter.setBrush(brush)
            painter.drawEllipse(0, 0, self.height(), self.height())
        painter.end()

    def lighter(self, color):
        hexx=color.name()
        hexx = hexx.strip("#")
        r = int(hexx[:2], 16)
        g = int(hexx[2:4], 16)
        b = int(hexx[4:6], 16)
        r2 = hex(min(r + 20,255)).replace("0x", "")
        g2 = hex(min(g + 20,255)).replace("0x", "")
        b2 = hex(min(b + 20,255)).replace("0x", "")
        return QColor("#" + r2 + g2 + b2)

class TopBar(QWidget):
    def __init__(self, color, height, parent=None):
        QWidget.__init__(self, parent)
        if not parent:
            raise (Exception("You must specify a parent of this widget"))
        self.setObjectName("TopBar")
        self.setStyleSheet("background-color: #305135")
        self.height_resize(height)
        self.color = color

    def height_resize(self, height):
        self.resize(self.parent().width(), height)


class TabBar(QTabBar):
    def __init__(self, parent=None, *args):
        super(TabBar, self).__init__(parent)
        # self.setTabButton()
        if len(args) == 1:
            color2 = args[0].name()
        else:
            color2 = "#4ca050"
        if isinstance(parent, TopBar):
            color2 = self.lighter(self.lighter(parent.color))
        if 125<QColor(color2).red() and 125<QColor(color2).green() and 125<QColor(color2).blue():
            text="black"
        else:
            text="white"
        with open("QTabBar.qss") as f:
            data = f.read()
            while "[background]" in data:
                ind = data.find("[background]")
                data = data[:ind] + color2 + str(data[ind + 12:])
            while "[bottom]" in data:
                ind = data.find("[bottom]")
                if color2=="#"+color2[1:3]*3:
                    if text=="black":
                        color="#3F51B5"
                    else:
                        color="#29b6f6"
                else:
                    print color2
                    color=self.lighter(self.lighter(self.lighter(color2)))
                data = data[:ind] + color + str(data[ind + 8:])
            while "[hover]" in data:
                ind = data.find("[hover]")
                data = data[:ind] + self.lighter(color2) + str(data[ind + 7:])
            while "[color]" in data:
                ind = data.find("[color]")
                data = data[:ind] + text + str(data[ind + 7:])
            while "[background-pressed]" in data:
                ind = data.find("[background-pressed]")
                data = data[:ind] + str(self.darker(color2)) + str(data[ind + 20:])
            self.setStyleSheet(data)

    def darker(self, hexx):
        hexx = hexx.strip("#")
        r = int(hexx[:2], 16)
        g = int(hexx[2:4], 16)
        b = int(hexx[4:6], 16)
        r2 = hex(max(r - 20,0)).replace("0x", "")
        g2 = hex(max(g - 20,0)).replace("0x", "")
        b2 = hex(max(b - 20,0)).replace("0x", "")
        if len(r2)==1:
            r2="0"+r2
        if len(g2)==1:
            g2="0"+g2
        if len(b2)==1:
            b2="0"+b2
        return "#" + r2 + g2 + b2

    def lighter(self, hexx):
        hexx = hexx.strip("#")
        r = int(hexx[:2], 16)
        g = int(hexx[2:4], 16)
        b = int(hexx[4:6], 16)
        r2 = hex(min(r + 20,255)).replace("0x", "")
        g2 = hex(min(g + 20,255)).replace("0x", "")
        b2 = hex(min(b + 20,255)).replace("0x", "")
        return "#" + r2 + g2 + b2


class Slider(QSlider):
    def __init__(self, parent=None):
        super(Slider, self).__init__(parent)
        with open("QSlider.qss") as f:
            self.setStyleSheet(f.read())


class CheckBox(QCheckBox):
    def __init__(self, *args):
        super(CheckBox, self).__init__(*args)
        self.setMouseTracking(True)
        if tuple() in [type(i) for i in args]:
            for arg in args:
                if type(arg) == tuple():
                    color = arg
        else:
            color = (QColor(0, 150, 136), QColor(255, 255, 255))
        self.color1 = color[0]
        self.color2 = color[1]
        self.svgrenderer = QSvgRenderer("icons\\check.svg")

        self.check = QImage(500, 200, QImage.Format_ARGB32)
        self.resize(30, 30)
        paint = QPainter(self.check)
        self.svgrenderer.render(paint)
        paint.end()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)

        self.img = QPixmap()
        if self.isChecked():
            painter.setBrush(self.color1)
            painter.drawRect(QRect(-1, -1, 31, 31))
            painter.drawPixmap(QRect(-2, -5, 35, 40), self.img.fromImage(self.check))
        else:
            pen = QPen()
            pen.setWidth(2)
            painter.setPen(pen)
            # hand draw rect
            painter.drawLine(QPoint(0, 0), QPoint(30, 0))
            painter.drawLine(QPoint(30, 0), QPoint(30, 30))
            painter.drawLine(QPoint(0, 0), QPoint(0, 30))
            painter.drawLine(QPoint(0, 30), QPoint(30, 30))
        painter.end()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.isChecked():

                self.setChecked(False)
            else:
                self.setChecked(True)
            self.repaint()


class ProgressBar(QProgressBar):
    def __init__(self, *args):
        QProgressBar.__init__(self, *args)
        with open("QProgressBar.qss") as f:
            self.setStyleSheet(f.read())


class Hamburger(QPushButton):
    def __init__(self, parent=None):
        QPushButton.__init__(self, parent)
        self.svgrenderer=QSvgRenderer("icons/hamburger.svg")
        paint = QPainter(self.check)
        self.svgrenderer.render(paint)
        paint.end()

class LineEdit(QLineEdit):
    def __init__(self,parent=None):
        QLineEdit.__init__(self,parent)
        with open("QLineEdit.qss") as f:
            self.setStyleSheet(f.read())

    def wrong(self):
        self.setStyleSheet("QLineEdit{border: none;padding-bottom: 2px;border-bottom: 2px solid #ff1744;color: #111111;font-size: 20px;}")
class Page(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.setStyleSheet("background-color:#efefef")

