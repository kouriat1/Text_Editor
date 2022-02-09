import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc



class MainWindow(qtw.QMainWindow):

    def __init__(self):
        """MainWindow constructor."""
        super().__init__()
        # Main UI code goes here
        self.textedit = qtw.QTextEdit()
        self.setCentralWidget(self.textedit)

        # Menubar

        menubar = self.menuBar()  # QMenuBar
        file_menu = menubar.addMenu('File')  # QMenu
        file_menu.addAction('Open', self.open_file)
        save_action = file_menu.addAction('Save')  # QAction
        file_menu.addSeparator()
        file_menu.addAction('Quit', self.close)

        save_action.triggered.connect(self.save_file)

        # statusbar
        self.statusBar().showMessage('Welcome to my editor', 2000)

        edit_toolbar = self.addToolBar('Edit')  # QToolBar
        edit_toolbar.addAction('Copy', self.textedit.copy)
        edit_toolbar.addAction('Cut', self.textedit.cut)
        edit_toolbar.addAction('Paste', self.textedit.paste)
        
        # Dockwidget
        

        # End main UI code
        self.show()

    def save_file(self):

        text = self.textedit.toPlainText()
        filename, _ = qtw.QFileDialog.getSaveFileName()
        if filename:
            with open(filename, 'w') as handle:
                handle.write(text)
                self.statusBar().showMessage(f'Saved to {filename}')

    def open_file(self):
        filename, _ = qtw.QFileDialog.getOpenFileName()
        if filename:
            with open(filename, 'r') as handle:
                text = handle.read()
            self.textedit.clear()
            self.textedit.insertPlainText(text)
            self.textedit.moveCursor(qtg.QTextCursor.Start)
            self.statusBar().showMessage(f'Editing {filename}')
            ##closeEvent
    def closeEvent(self,event):
        result = QtGui.QMessageBox.question(self,
                      "Close Window",
                      "Are you sure you want to exit ?",
                      QtGui.QMessageBox.Yes| QtGui.QMessageBox.No)
        event.ignore()

        if result == QtGui.QMessageBox.Yes:
         event.accept()

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())