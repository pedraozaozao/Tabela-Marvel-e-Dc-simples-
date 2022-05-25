from turtle import color, width
from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSortFilterProxyModel

from PyQt5.QtGui import QStandardItem, QStandardItemModel

Quadrinhos = ('doutor estranho','homem de ferro','homem aranha','thor','hulk','guardioes da galaxia','thanos','dormamo','pantera negra','galactus','feiticeira escarlate','justiceiro',
'cavaleiro da lua',)
modelo = QStandardItemModel(len(Quadrinhos),1)
modelo.setHorizontalHeaderLabels(['Quadrinhos Da Marvel'])

for linha, Quadrinho in enumerate(Quadrinhos):  #[(1, 'cavaleiro da moon'), (2,'homem-spider')]
    elemento = QStandardItem(Quadrinho)
    modelo.setItem(linha, 0, elemento)

filtro = QSortFilterProxyModel()
filtro.setSourceModel(modelo)
filtro.setFilterKeyColumn(0)
#filtro.setFilterCaseSensivity(Qt.CaseInsensitive)



Quadrinhos2 = ('batman','dark side','robin','jovens titans','flash','flash reverso','mulher maravilha','superman','lanterna verde','ares','lendas do amanha','lanterna vermelha','super girl',)
modelo2 = QStandardItemModel(len(Quadrinhos2),1)
modelo2.setHorizontalHeaderLabels(['Quadrinhos Da DC'])

for linha2, Quadrinho2 in enumerate(Quadrinhos2):  #[(1, 'batman'), (2,'robin')]
    elemento2 = QStandardItem(Quadrinho2)
    modelo2.setItem(linha2, 0, elemento2)

filtro2 = QSortFilterProxyModel()
filtro2.setSourceModel(modelo2)
filtro2.setFilterKeyColumn(0)
#filtro2.setFilterCaseSensivity(Qt.CaseInsensitive)




app=QtWidgets.QApplication([])
tela=uic.loadUi("layout.ui")
tela.tableView.setModel(filtro)
tela.tableView.horizontalHeader().setStyleSheet("font-size: 20px; color : rgb(50,50, 225);")
tela.lineEdit.textChanged.connect(filtro.setFilterRegExp)
tela.tableView_2.setModel(filtro2)
tela.tableView_2.horizontalHeader().setStyleSheet("font-size: 20px; color : rgb(50,50, 225);")
tela.lineEdit_2.textChanged.connect(filtro2.setFilterRegExp)


tela.show()
app.exec()