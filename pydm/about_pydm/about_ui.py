# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from qtpy import QtCore, QtWidgets, QtGui


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(474, 288)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setMinimumSize(QtCore.QSize(450, 0))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.versionTab = QtWidgets.QWidget()
        self.versionTab.setObjectName("versionTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.versionTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.pydmLabel = QtWidgets.QLabel(self.versionTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pydmLabel.sizePolicy().hasHeightForWidth())
        self.pydmLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(QtGui.QFont.Weight.Bold)
        self.pydmLabel.setFont(font)
        self.pydmLabel.setTextFormat(QtCore.Qt.PlainText)
        self.pydmLabel.setScaledContents(False)
        self.pydmLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pydmLabel.setObjectName("pydmLabel")
        self.verticalLayout_2.addWidget(self.pydmLabel)
        self.pydmVersionLabel = QtWidgets.QLabel(self.versionTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pydmVersionLabel.sizePolicy().hasHeightForWidth())
        self.pydmVersionLabel.setSizePolicy(sizePolicy)
        self.pydmVersionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pydmVersionLabel.setObjectName("pydmVersionLabel")
        self.verticalLayout_2.addWidget(self.pydmVersionLabel)
        self.modulesVersionLabel = QtWidgets.QLabel(self.versionTab)
        self.modulesVersionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.modulesVersionLabel.setWordWrap(True)
        self.modulesVersionLabel.setObjectName("modulesVersionLabel")
        self.verticalLayout_2.addWidget(self.modulesVersionLabel)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.tabWidget.addTab(self.versionTab, "")
        self.externalToolsTab = QtWidgets.QWidget()
        self.externalToolsTab.setObjectName("externalToolsTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.externalToolsTab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.externalToolsTableWidget = QtWidgets.QTableWidget(self.externalToolsTab)
        self.externalToolsTableWidget.setObjectName("externalToolsTableWidget")
        self.externalToolsTableWidget.setColumnCount(0)
        self.externalToolsTableWidget.setRowCount(0)
        self.verticalLayout_3.addWidget(self.externalToolsTableWidget)
        self.tabWidget.addTab(self.externalToolsTab, "")
        self.dataPluginsTab = QtWidgets.QWidget()
        self.dataPluginsTab.setObjectName("dataPluginsTab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.dataPluginsTab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.dataPluginsTableWidget = QtWidgets.QTableWidget(self.dataPluginsTab)
        self.dataPluginsTableWidget.setObjectName("dataPluginsTableWidget")
        self.dataPluginsTableWidget.setColumnCount(0)
        self.dataPluginsTableWidget.setRowCount(0)
        self.verticalLayout_4.addWidget(self.dataPluginsTableWidget)
        self.tabWidget.addTab(self.dataPluginsTab, "")
        self.contributorsTab = QtWidgets.QWidget()
        self.contributorsTab.setObjectName("contributorsTab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.contributorsTab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.contributorsListWidget = QtWidgets.QListWidget(self.contributorsTab)
        self.contributorsListWidget.setObjectName("contributorsListWidget")
        self.verticalLayout_5.addWidget(self.contributorsListWidget)
        self.tabWidget.addTab(self.contributorsTab, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "About PyDM"))
        self.pydmLabel.setText(_translate("Form", "PyDM"))
        self.pydmVersionLabel.setText(_translate("Form", "Version {version}"))
        self.modulesVersionLabel.setText(
            _translate(
                "Form",
                """Using Python v{pyver}, {python_binding} v{python_binding_ver}, Qt v{qtver}, Numpy v{numpyver}, and PyQtGraph v{pyqtgraphver}.""",
            )
        )
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.versionTab), _translate("Form", "Version"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.externalToolsTab), _translate("Form", "External Tools"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dataPluginsTab), _translate("Form", "Data Plugins"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.contributorsTab), _translate("Form", "Contributors"))
