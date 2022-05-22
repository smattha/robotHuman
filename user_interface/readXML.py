#!/usr/bin/env python3
import xml.etree.ElementTree as ET
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
    def parser(self, dict):
        for key in dict:
            setattr(self, key,dict[key])

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
                # newResult = namedtuple("result", d.keys())(*d.values())
                newResult=resultOfPerson()
                newResult.parser(d)
                # newResult = namedtuple("result", d.keys())(*d.values())
                resultsStored.listResults.append(newResult)
            return resultsStored

##########################################
#Write data to file
##########################################
    # fp= open('my_json.txt','w')
    # # data=resultOfPerson()
    # # json_data=data.__dict__,data.__dict__,
    #
    # data=results()
    #
    #
    # # json.dump(data.listResults, fp)
    # json.dump(data.toJSON(), fp)

#################################################
###############Read from files###################
#################################################
# file='my_json.txt'
#
# fp= open(file, 'r')
# data = json.load(fp)
#
# jsonDataStr=json.loads(data)
# data=jsonDataStr['listResults']
#
#
# resultsStored= results()
#
# for d in  data:
#     newResult = namedtuple("result", d.keys())(*d.values())
#     resultsStored.listResults.append(newResult)


resultsA= results()

personA= resultOfPerson()

personA.name='Person 1'

resultsA.listResults.append(personA)


personB= resultOfPerson()

personB.name='Person 2'

resultsA.listResults.append(personB)

storeJSONFile1=StoreJSONFile()
storeJSONFile1.file='test.json'
storeJSONFile1.storeResults(resultsA)
resultsB=storeJSONFile1.readFromFile()


a=1