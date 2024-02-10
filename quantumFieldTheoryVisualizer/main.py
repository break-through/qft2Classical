from PyQt5.QtWidgets import QApplication
from visualizer import Visualizer

def main():
    app = QApplication([])
    visualizer = Visualizer()
    visualizer.show()
    app.exec_()

if __name__ == "__main__":
    main()