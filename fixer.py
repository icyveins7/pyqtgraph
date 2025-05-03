import pyqtgraph as pg
import numpy as np
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication
QApplication.closeAllWindows()

mat = np.eye(3)
mat[2,0] = 1
mat[0,2] = 1

win = pg.GraphicsLayoutWidget()
plt0 = win.addPlot(row=0, col=0)
plt0.addItem(pg.ImageItem(mat))
plt1 = win.addPlot(row=0, col=1)
plt1.addItem(pg.ImageItem(mat))
plt2 = win.addPlot(row=0, col=2)
plt2.addItem(pg.ImageItem(mat))
plt0.setTitle('a')
plt1.setTitle('very very very very long title that should not affect the layout')
plt2.setTitle('b')

# plt0.setMinimumSize(0,0)
# plt1.setMinimumSize(0,0)
# plt2.setMinimumSize(0,0)
#
# plt0.setPreferredSize(0,0)
# plt1.setPreferredSize(0,0)
# plt2.setPreferredSize(0,0)

title0 = plt0.layout.itemAt(5)
title1 = plt1.layout.itemAt(5)
title2 = plt2.layout.itemAt(5)

print("Title size hints")
minSize = title0.effectiveSizeHint(Qt.SizeHint.MinimumSize)
prefSize = title0.effectiveSizeHint(Qt.SizeHint.PreferredSize)
maxSize = title0.effectiveSizeHint(Qt.SizeHint.MaximumSize)
print(minSize, prefSize, maxSize)
horzPolicy = title0.sizePolicy().horizontalPolicy()
print(horzPolicy)

minSize = title1.effectiveSizeHint(Qt.SizeHint.MinimumSize)
prefSize = title1.effectiveSizeHint(Qt.SizeHint.PreferredSize)
maxSize = title1.effectiveSizeHint(Qt.SizeHint.MaximumSize)
print(minSize, prefSize, maxSize)
horzPolicy = title1.sizePolicy().horizontalPolicy()
print(horzPolicy)

minSize = title2.effectiveSizeHint(Qt.SizeHint.MinimumSize)
prefSize = title2.effectiveSizeHint(Qt.SizeHint.PreferredSize)
maxSize = title2.effectiveSizeHint(Qt.SizeHint.MaximumSize)
print(minSize, prefSize, maxSize)
horzPolicy = title2.sizePolicy().horizontalPolicy()
print(horzPolicy)

print("=================")


gLayout = win.ci
gGridLayout = gLayout.layout

minSize = plt0.effectiveSizeHint(Qt.SizeHint.MinimumSize)
prefSize = plt0.effectiveSizeHint(Qt.SizeHint.PreferredSize)
maxSize = plt0.effectiveSizeHint(Qt.SizeHint.MaximumSize)
print(minSize, prefSize, maxSize)
horzPolicy = plt0.sizePolicy().horizontalPolicy()
print(horzPolicy)

minSize = plt1.effectiveSizeHint(Qt.SizeHint.MinimumSize)
prefSize = plt1.effectiveSizeHint(Qt.SizeHint.PreferredSize)
maxSize = plt1.effectiveSizeHint(Qt.SizeHint.MaximumSize)
print(minSize, prefSize, maxSize)
horzPolicy = plt1.sizePolicy().horizontalPolicy()
print(horzPolicy)

minSize = plt2.effectiveSizeHint(Qt.SizeHint.MinimumSize)
prefSize = plt2.effectiveSizeHint(Qt.SizeHint.PreferredSize)
maxSize = plt2.effectiveSizeHint(Qt.SizeHint.MaximumSize)
print(minSize, prefSize, maxSize)
horzPolicy = plt2.sizePolicy().horizontalPolicy()
print(horzPolicy)

win.show()

