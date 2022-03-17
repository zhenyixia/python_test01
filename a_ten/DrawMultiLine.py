# -*- coding:utf-8 -*-
# @Author: lyp
# @Desc  : 画线
# @Time  : 22/03/18 6:56

import sys

from PySide2.QtCore import Qt
from PySide2.QtGui import QPen, QPainter
from PySide2.QtWidgets import QApplication, QWidget


class DrawMultiLine(QWidget):
    def __init__(self):
        super(DrawMultiLine, self).__init__()
        self.resize(300, 300)
        self.setWindowTitle('设置Pen的样式')

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        pen = QPen(Qt.red, 3, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(20, 40, 250, 40)
        size = self.size()

        pen = QPen(Qt.red, 3, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(20, 40, 250, 40)
        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        painter.drawLine(20, 80, 250, 80)
        pen.setStyle(Qt.DashDotDotLine)
        painter.setPen(pen)
        painter.drawLine(20, 120, 250, 120)
        pen.setStyle(Qt.DotLine)
        painter.setPen(pen)
        painter.drawLine(20, 160, 250, 160)

        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1, 4, 5, 4])
        painter.setPen(pen)
        painter.drawLine(20, 240, 250, 240)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawMultiLine()
    main.show()
    sys.exit(app.exec_())
