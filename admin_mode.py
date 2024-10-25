import sys

from PyQt5.QtWidgets import *

from View.AdminLandingPage import AdminLandingPage

if __name__ == "__main__":
    admin = AdminLandingPage()
    app = QApplication(sys.argv)
    admin = QDialog()
    ui = AdminLandingPage()
    ui.setupUi(admin)
    admin.show()

    sys.exit(app.exec_())