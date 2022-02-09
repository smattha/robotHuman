from PyQt5.QtCore import QObject, pyqtSignal
from sqlalchemy import true


class MainWindowModel(QObject):


    listAvailableExersice= ["Δραστηριότητα 1", "Δραστηριότητα 2", "Δραστηριότητα 3",
                            "Δραστηριότητα 4", "Δραστηριότητα 5", "Δραστηριότητα 6"]

    exersisesDescription = {
    "1": "Περιγραφή Δραστηριότητα 1",
    "2": "Περιγραφή Δραστηριότητα 2",
    "3": "Περιγραφή Δραστηριότητα 3",
    "4": "Περιγραφή Δραστηριότητα 4",
    "5": "Περιγραφή Δραστηριότητα 5",
    "6": "Περιγραφή Δραστηριότητα 6",
}

    #create signal
    changeDscrSingal = pyqtSignal(str, name='valChanged')
    resetFieldSingal = pyqtSignal(str, name='resetFieldChanged')
    setPageSignal = pyqtSignal(int, name='setPageChanged')

    

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
        print(value)
        # self._name = str(value+1)
        print("selectedButton Setter",str(value+1))
        self._description=self.exersisesDescription[str(value+1)]
        print("selectedButton Setter",self._description)
        self.changeDscrSingal.emit(self._description)

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

    @property
    def description(self):
        return self._description

    @description.setter
    def getDEscription(self, value):
        self._description= value
        print("description Setter")
        # self.name_change.emit(value)

    @description.getter
    def getDescription(self):
        return self._description


    def resetFields(self):
        print('reset data')
        self.resetFieldSingal.emit('')

    def trigger(self,page):
        self.setPageSignal.emit(page)


    def __init__(self):
        super().__init__()

        self._name = ''
        self._surname = ''
        self._age = ''
        self._selectedExercise=''
       

