import backend
import frontend

class Application:
    def __init__(self):
        self.__backend = backend.BackEndManager("data.csv")
        self.__frontend = frontend.FrontEndUI(self.__backend)

app = Application()
