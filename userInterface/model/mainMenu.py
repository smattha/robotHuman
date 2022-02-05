from PyQt5.QtCore import QObject, pyqtSignal


class MainModel(QObject):


    listAvailableExersice= ["1", "2", "3"]

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        print("name Setter")
        # self.name_change.emit(value)

    @name.getter
    def getName(self):
        return self.__name

    @property
    def selectedExercise(self):
        return self._name

    @selectedExercise.setter
    def selectedExercise(self, value):
        self._name = value
        print("selectedButton Setter")
        # self.name_change.emit(value)

    @selectedExercise.getter
    def getSelectedExercise(self):
        return self.__name

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value
        print("surname Setter")
        # self.name_change.emit(value)
    
    @surname.getter
    def getSurname(self):
        return self.__surname

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age= value
        print("age Setter")
        # self.name_change.emit(value)

    @age.getter
    def getAge(self):
        return self._age

    def __init__(self):
        super().__init__()

        self._name = ''
        self._surname = ''
        self._age = ''
        self._selectedExercise='1'
       

