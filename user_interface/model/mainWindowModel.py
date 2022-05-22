import json
from turtle import position
from PyQt5.QtCore import QObject, pyqtSignal
from sqlalchemy import true
import json
from collections import namedtuple


class resultOfPerson(object):

    def __init__(self, my_dict):
        for key in my_dict:
            setattr(self, key, my_dict[key])

    def __init__(self):
        super().__init__()
        self.listWithNames = ["1"]

        self.name = ''
        self.age = ''
        self.surname = ''

        self.answerEx1 = ''
        self.answerEx2 = ''
        self.answerEx3 = ''
        self.answerEx4 = ''
        self.answerEx5A = ''
        self.answerEx5B = ''
        self.answerEx6A = ''
        self.answerEx6B = ''

        self.answerEx7 = ''
        self.answerEx8 = ''
        self.answerEx9 = ''
        self.answerEx10 = ''
        self.answerEx11A = ''
        self.answerEx11B = ''
        self.answerEx12A = ''
        self.answerEx12B = ''
        # self.name = 'Ονομα'
        # self.surname = 'Ματθαιάκης'

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)



class results():

    def __init__(self):
        # super().__init__()
        self.listResults = []
        self.listWithNames = ["1"]
        # result = resultOfPerson()
        # #
        # self.listResults.append(result)
        # self.listResults.append(result)
        # self.listResults.append(resultOfPerson())

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)

class StoreJSONFile():

    def __int__(self,str):
        self.file=str


    def __int__(self,):
        self.file=''

    def storeResults(self,results):
        jsonFileHandler= open(self.file,'w')
        # data=resultOfPerson()
        # json_data=data.__dict__,data.__dict__,

        # json.dump(data.listResults, fp)
        json.dump(results.toJSON(), jsonFileHandler)


    def readFromFile(self):

            fp= open(self.file, 'r')
            data = json.load(fp)

            jsonDataStr=json.loads(data)
            data=jsonDataStr['listResults']


            resultsStored= results()

            for d in  data:
                newResult = namedtuple("result", d.keys())(*d.values())
                resultsStored.listResults.append(newResult)
            return resultsStored


class MainWindowModel(QObject):


    listAvailableExersice= ["Το λιοντάρι και τα παπάκια", "Ασκηση προσοχής", "Ο Γιωργάκης και η σοκολάτα",
                            "Η Μαρία και η μαμά της", "Ένα παιγνίδι με γρίφους", "Τι δείχνουν οι εικόνες",
                            "Η μαμά καγκούρο", "Ο Μάξιμος", "Ο κοκκινός στρατός",
                            "Η Σοφία στο σχολείο", "Ένα παιγνίδι με γρίφους 2", "Τι δείχνουν οι εικόνες 2"]

    exersisesDescription = {
    "1": "Περιγραφή Δραστηριότητα 1",
    "2": "Περιγραφή Δραστηριότητα 2",
    "3": "Περιγραφή Δραστηριότητα 3",
    "4": "Περιγραφή Δραστηριότητα 4",
    "5": "Περιγραφή Δραστηριότητα 5",
    "6": "Περιγραφή Δραστηριότητα 6",
    "7": "Περιγραφή Δραστηριότητα 7",
    "8": "Περιγραφή Δραστηριότητα 8",
    "9": "Περιγραφή Δραστηριότητα 9",
    "10": "Περιγραφή Δραστηριότητα 10",
    "11": "Περιγραφή Δραστηριότητα 11",
    "12": "Περιγραφή Δραστηριότητα 12",
}
    poseX=400
    poseY=100
    sizeX=1000
    sizeY=800
    i=2
    sleepForAnswer=1 ;
    #Constants
    resourcesImage1="./resources/images/ex1/mainImage.png"
    resourcesImage2="./resources/images/ex2/mainImage.png"
    resourcesImage3="./resources/images/ex3/1.png"
    resourcesImage3B="./resources/images/ex3/2.png"
    
    exersice3A="./resources/images/ex3/3.png"
    exersice3B="./resources/images/ex3/4.png"
    
    exersice4A="./resources/images/ex4/1.png"
    exersice4B="./resources/images/ex4/6.png"
    exersice4C="./resources/images/ex4/7.png"
    exersice4D="./resources/images/ex4/8.png"

    exersice5A="./resources/images/ex5/image.png"
    exersice6A="./resources/images/ex6/1.png"

    easyFeedbackImg="./resources/images/3.png"
    normalFeedback="./resources/images/2.jpg"
    difficultFeedback="./resources/images/1.jpg"  


    #create signal
    changeDscrSingal = pyqtSignal(str, name='valChanged')
    resetFieldSingal = pyqtSignal(str, name='resetFieldChanged')
    setPageSignal = pyqtSignal(int, name='setPageChanged')
    nextImgSingal= pyqtSignal(str,name='nextImg')

    #Exercise 5
    nextPageSignalEx5 = pyqtSignal(str, name='nextPageSignal')

    #Exercise 4
    nextPageSignalEx4 = pyqtSignal(str, name='nextPageSignal4')
    
    #Exercise 6
    nextPageSignalEx6 = pyqtSignal(str, name='nextPageSignal6')


    #Exercise 6
    feedbackShowButton = pyqtSignal(str, name='feedbackShowButton')

    @property
    def currentExerciseID(self):
        return self._currentExerciseID    

    @currentExerciseID.setter
    def currentExerciseID(self, value):
        self._currentExerciseID = value

    @currentExerciseID.getter
    def getCurrentExerciseID(self):
        return self._currentExerciseID

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
    def nextImage(self):
        return self.nextImage

    @nextImage.setter
    def nextImage(self, value):
        self.nextImgSingal.emit(value)

    @nextImage.getter
    def getNextImage(self):
        return self.nextImage


    @property
    def selectedExercise(self):
        return self._name

    @selectedExercise.setter
    def selectedExercise(self, value):
        self._description=self.exersisesDescription[str(value+1)]
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


    @property
    def showButtonFeedback(self):
        return self._description

    @showButtonFeedback.setter
    def showButtonFeedback(self, value):
        self._showButtonFeedback= value
        self.feedbackShowButton.emit(value)

    @showButtonFeedback.getter
    def getshowButtonFeedback(self):
        return self._showButtonFeedback


    def resetFields(self):
        print('reset data')
        self.resetFieldSingal.emit('')

    def trigger(self,page):
        self.setPageSignal.emit(page)


    def nextPageEx6(self,value):
        if self.stepImage6==0:
            print(' next page image 6', value)
            self.nextPageSignalEx6.emit("./resources/images/ex6/2.png") 
            self.stepImage6=self.stepImage6+1       
        else :
            self.setPageSignal.emit(8)     

    def reset(self):
        self._name = ''
        self._surname = ''
        self._age = ''
        self._selectedExercise=''
        self.stepImage3=0
        self.stepImage4=0
        self.stepImage6=0
        self._currentExerciseID=0
        self.feedback=''
        self._showButtonFeedback=''
        self.nextImage=''


    def createNewResult(self, newResult):

        self.result.listResults.append(newResult)

        storeJSONFile1 = StoreJSONFile()
        storeJSONFile1.file = 'test.json'
        self.result = storeJSONFile1.readFromFile()
        self.result.listResults.append(newResult)
        storeJSONFile1.storeResults(self.result)

    def createNewResultObject(self):
        return resultOfPerson()

    def __init__(self):
        super().__init__()
        self.result=results()
        self.reset()


