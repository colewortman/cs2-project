from project_logic import *

def main() -> None:
    '''
    Function to call and generate the gui.
    '''
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()

if __name__ == "__main__":
    main()