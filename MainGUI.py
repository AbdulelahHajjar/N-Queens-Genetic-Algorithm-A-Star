# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import AStarAlgorithmGUI
import GeneticAlgorithmGUI


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(640, 431)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.greetingsLabel = QtWidgets.QLabel(self.centralwidget)
        self.greetingsLabel.setGeometry(QtCore.QRect(200, 40, 241, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.greetingsLabel.setFont(font)
        self.greetingsLabel.setObjectName("greetingsLabel")
        self.createdByLabel = QtWidgets.QLabel(self.centralwidget)
        self.createdByLabel.setGeometry(QtCore.QRect(190, 70, 261, 16))
        self.createdByLabel.setObjectName("createdByLabel")
        self.chooseAlgorithm = QtWidgets.QLabel(self.centralwidget)
        self.chooseAlgorithm.setGeometry(QtCore.QRect(10, 160, 371, 16))
        self.chooseAlgorithm.setObjectName("chooseAlgorithm")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 190, 641, 221))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.numQueensGATF = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.numQueensGATF.setObjectName("numQueensGATF")
        self.verticalLayout.addWidget(self.numQueensGATF)
        self.populationSizeTF = QtWidgets.QLineEdit(
            self.horizontalLayoutWidget)
        self.populationSizeTF.setObjectName("populationSizeTF")
        self.verticalLayout.addWidget(self.populationSizeTF)
        self.maxGenerationsTF = QtWidgets.QLineEdit(
            self.horizontalLayoutWidget)
        self.maxGenerationsTF.setObjectName("maxGenerationsTF")
        self.verticalLayout.addWidget(self.maxGenerationsTF)
        self.mutationRateTF = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.mutationRateTF.setObjectName("mutationRateTF")
        self.verticalLayout.addWidget(self.mutationRateTF)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.geneticsBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.geneticsBtn.clicked.connect(lambda: self.gaBtnClicked(self.numQueensGATF.text(
        ), self.populationSizeTF.text(), self.maxGenerationsTF.text(), self.mutationRateTF.text()))
        self.geneticsBtn.setObjectName("geneticsBtn")
        self.verticalLayout.addWidget(self.geneticsBtn)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.numQueensASTF = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.numQueensASTF.setObjectName("numQueensASTF")
        self.verticalLayout_2.addWidget(self.numQueensASTF)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.aStarBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.aStarBtn.clicked.connect(
            lambda: self.aStarBtnClicked(self.numQueensASTF.text()))
        self.aStarBtn.setObjectName("aStarBtn")
        self.verticalLayout_2.addWidget(self.aStarBtn)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.greetingsLabel.setText(_translate(
            "mainWindow", "Welcome to N-Queens Solver!"))
        self.createdByLabel.setText(_translate(
            "mainWindow", "Created by: Abdulelah Hajjar | s201727090"))
        self.chooseAlgorithm.setText(_translate(
            "mainWindow", "Choose how you would like to solve the N-Queens Problem:"))
        self.label.setText(_translate("mainWindow", "Genetics Algorithm"))
        self.numQueensGATF.setPlaceholderText(
            _translate("mainWindow", "Number of Queens"))
        self.populationSizeTF.setPlaceholderText(
            _translate("mainWindow", "Population Size"))
        self.maxGenerationsTF.setPlaceholderText(
            _translate("mainWindow", "Maximum Number of Generations"))
        self.mutationRateTF.setPlaceholderText(
            _translate("mainWindow", "Mutation Rate (0-1)"))
        self.geneticsBtn.setText(_translate(
            "mainWindow", "Solve with Genetics Algorithm"))
        self.label_2.setText(_translate("mainWindow", "A* Algorithm"))
        self.numQueensASTF.setPlaceholderText(
            _translate("mainWindow", "Number of Queens"))
        self.aStarBtn.setText(_translate(
            "mainWindow", "Solve with A* Algorithm"))

    def gaBtnClicked(self, numQueens, populationCount, maxGens, mutationRate):
        GeneticAlgorithmGUI.start(
            numQueens, populationCount, maxGens, mutationRate)

    def aStarBtnClicked(self, numQueens):
        AStarAlgorithmGUI.start(int(numQueens))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
