import winsound
from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer
import detection_camera
import time
import multiprocessing as mp
import sys
import threading
import os


def speech(text, model):
    ###################
    #text to dpeech section
    model_path = model
    config_path = 'C:/Users/Gebruiker/Documents/litanie/models_voice/config.json'
    speakers_file_path = None
    language_ids_file_path = None
    vocoder_path = None
    vocoder_config_path = None
    encoder_path = None
    encoder_config_path = None
    # text = str(completion)
    use_cuda = True
    output_wav = "C:/Users/Gebruiker/Documents/litanie/voice_output/output.wav"

    synthesizer = Synthesizer(
            model_path,
            config_path,
            speakers_file_path,
            language_ids_file_path,
            vocoder_path,
            vocoder_config_path,
            encoder_path,
            encoder_config_path,
            use_cuda,
        )
    

    wav = synthesizer.tts(text)
    synthesizer.save_wav(wav, output_wav)
    print('Done with sythesizing')
    file = "C:/Users/Gebruiker/Documents/litanie/voice_output/output.wav"
    # os.system("afplay " + file)
    winsound.PlaySound(file, winsound.SND_FILENAME)


def speak_at_random(camera):

    models = []
    rootdir = 'C:/Users/Gebruiker/Documents/litanie/litanie_code/models/'
    for subdir, _, files in os.walk(rootdir):
        for file in files:

            if file[-4:] == '.pth':
                models.append(os.path.join(subdir, file))
    print(models)
    # models = sorted(models)


    for model in models:
        time.sleep(3)
      
      

        test = "er zijn  nu {} mensen".format(camera.number_faces)
        # print("")
        speech(test, model)




if __name__ == "__main__":

    # Create camera object
    camera = detection_camera.myCamera()

    # p1 = threading.Thread(target=speak_at_random(camera) )
    # p2 = threading.Thread(target=camera.run_in_loop())
    # p1.start();p2.start()

    # start thread 1
    # Start in loop
    # camera.run_in_loop()
    p2 = threading.Thread(target= camera.run_in_loop) 
    p2.start()

    # while True:
    #     time.sleep(2)
    #     print(camera.number_faces)
        

    # Start thread 2
    # speak_at_random(camera)
    p1 = threading.Thread(target= speak_at_random, args=[camera] )
    p1.start()
    


    


    

