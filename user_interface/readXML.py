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

class results():

    def __init__(self):
        # super().__init__()
        self.listResults = []
        # self.listWithNames = ["1"]
        # result = resultOfPerson()
        #
        # self.listResults.append(result)
        # self.listResults.append(result)
        # self.listResults.append(resultOfPerson())

    def toJSON(self):
        return json.dumps(self.listResults, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)



fp= open('my_json.txt','w')
data=resultOfPerson()
json_data=data.__dict__,data.__dict__,
json.dump(json_data, fp)



fp= open('my_json.txt', 'r')
data = json.load(fp)
# x = json.loads(data, object_hook=lambda d: resultOfPerson(**d))



# data1= resultOfPerson(data)
# data1= resultOfPerson
resultTotal=results()
eject_name = namedtuple("ObjectName", data[0].keys())(*data[0].values())
a=resultOfPerson()
# resultTotal.listResutls.append(a)
resultTotal.listResults.append(eject_name)
resultTotal.listResults.append(a)

eject_name = namedtuple("ObjectName", data[1].keys())(*data[1].values())
resultTotal.listResults.append(eject_name)
print ('1111111'+resultTotal.listResults[1].surname)
print ('!!!!!!!!!!!!!!!!!!!!!')

# #     # data=resultOfPerson()
# #     json.dump(data.toJSON(), fp)

# tree = ET.parse('/home/stergios/Desktop/1.xml')
# root = tree.getroot()
# for child in root:
#      print(child.tag, child.attrib)