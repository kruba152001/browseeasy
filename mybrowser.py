import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

#pQt5 is case sensitive

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com")) 
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #create navigation bar
        navigbar = QToolBar()
        self.addToolBar(navigbar)

        #create backbutton
        bckbutton = QAction("Back" , self)
        bckbutton.triggered.connect(self.browser.back)
        navigbar.addAction(bckbutton)

        #create forward button
        forbutton = QAction("Forward", self)
        forbutton.triggered.connect(self.browser.forward)
        navigbar.addAction(forbutton)

        #reload button
        rebutton = QAction("Reload",self)
        rebutton.triggered.connect(self.browser.reload)
        navigbar.addAction(rebutton)

        #create homebutton
        hombutton= QAction("Home",self)
        hombutton.triggered.connect(self.navigate_home)
        navigbar.addAction(hombutton)

        #create search bar
        self.url_bar=QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navigbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)
    def navigate_home(self):
        self.browser.setUrl(QUrl("http://google.com"))
    
    def navigate_to_url(self):
        url =self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self,q):
        self.url_bar.setText(q.toString())


#create application
app=QApplication(sys.argv)
QApplication.setApplicationName("My Browser")
window=MainWindow()
app.exec_()