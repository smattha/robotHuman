#!/usr/bin/env python3
import xml.etree.ElementTree as ET
	
tree = ET.parse('/home/smatt/Documents/git/src/audio_service/resources/data.xml')
root = tree.getroot()

# all items data
print('Expertise Data:')

for elem in root:
   for subelem in elem:
      print(subelem.text)




