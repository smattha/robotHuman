#!/usr/bin/env python3

import argparse
import os
import queue
import sounddevice as sd
import vosk
import sys
import json 


NAME = 'add_two_ints_server'


from audio_service.srv import *
import rospy 




class ControllerExersice5(object):

    def __init__(self,args,parser):
        self.args=args
        if args.list_devices:
            print(sd.query_devices())
            parser.exit(0)
        parser = argparse.ArgumentParser(
            description=__doc__,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            parents=[parser])
        parser.add_argument(
            '-f', '--filename', type=str, metavar='FILENAME',
            help='audio file to store recording to')
        parser.add_argument(
            '-m', '--model', type=str, metavar='MODEL_PATH',
            help='Path to the model')
        parser.add_argument(
            '-d', '--device', type=self.int_or_str,
            help='input device (numeric ID or substring)')
        parser.add_argument(
            '-r', '--samplerate', type=int, help='sampling rate')
        self.args = parser.parse_args(remaining)

        self.args.model = "model"
        
        if not os.path.exists(self.args.model):
            print ("Please download a model for your language from https://alphacephei.com/vosk/models")
            print ("and unpack as 'model' in the current folder.")
            parser.exit(0)
        if self.args.samplerate is None:
            device_info = sd.query_devices(self.args.device, 'input')
            # soundfile expects an int, sounddevice provides a float:
            self.args.samplerate = int(device_info['default_samplerate'])

        self.model = vosk.Model(self.args.model)

        if self.args.filename:
            dump_fn = open(args.filename, "wb")
        else:
            dump_fn = None

        self.q = queue.Queue()

        rospy.init_node(NAME)
        s = rospy.Service('add_two_ints', GetAudio, self.add_two_ints)






    def getText(self): 



        self.rec = vosk.KaldiRecognizer(self.model, self.args.samplerate)
        with sd.RawInputStream(samplerate=self.args.samplerate, blocksize = 8000, device=self.args.device, dtype='int16',
                            channels=1, callback=self.callback):
            while True:
                data = self.q.get()
                if self.rec.AcceptWaveform(data):
                    print(self.rec.Result())
                else:
                    self.dataResults = json.loads(self.rec.PartialResult())
                    print(self.rec.PartialResult())
                    if self.dataResults['partial']=='':
                        print('..........................................................................................................')
                    else:
                        break

            
            print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
            return self.dataResults['partial']

    def add_two_ints(self,req):
        print("...................../\/")
        
        # initialize the recognizer

        text=self.getText()
        return GetAudioResponse(text)

    def callback(self,indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        self.q.put(bytes(indata))

    def int_or_str(text):
        """Helper function for argument parsing."""
        try:
            return int(text)
        except ValueError:
            return text

if __name__ == '__main__':
    try:

        parser = argparse.ArgumentParser(add_help=False)
        parser.add_argument(
        '-l', '--list-devices', action='store_true',
        help='show list of audio devices and exit')
        args, remaining = parser.parse_known_args()
        app = ControllerExersice5(args,parser)
        
        rospy.spin()

        print("-------------")
    except KeyboardInterrupt:
        exit(0)




