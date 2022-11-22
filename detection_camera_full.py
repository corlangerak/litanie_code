import winsound
from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer
import detection_camera
import time
import multiprocessing as mp
import sys
import threading
import os
import random


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
    print("[speak_at_random]")
    time.sleep(3)
    models = []
    rootdir = 'C:/Users/Gebruiker/Documents/litanie/models_voice/'
    for subdir, _, files in os.walk(rootdir):
        for file in files:
            print("file: ", file)

            if file[-4:] == '.pth':
                models.append(os.path.join(subdir, file))
    print(models)
    # models = sorted(models)


    random_model = random.choice(models)
    
    for i in range(10):

        random_seconds = random.randint(2,9)
        time.sleep(random_seconds)
        random_zin = get_random_sentence(camera)
        print("Random zin: ", random_seconds, random_zin)
        speech(random_zin, random_model)


        # break



def get_random_sentence(camera):
    # print("this is it: , ", camera.number_faces)

    number_faces = int(camera.number_faces)

    stats = camera.stats
    
    mannen = 0
    vrouwen = 0
    leeftijden = []
    all_sents = []
    # print(camera.stats)
    # time.sleep(5)
    for person, statistics in camera.stats.items():
        print(statistics)

        if statistics['gender'] == "man":
            mannen += 1
        else:
            vrouwen += 1
        leeftijden.append(statistics['age'])

    if number_faces ==0:
        p_sents = ["Er zijn <num> mensen om een sigaret mee te roken", 
        "er zijn <num> mensen in de ruimte",
        "Er zijn <num> mensen om opnieuw een liedje voor te zingen"]

        all_sents.extend(p_sents)
        random_sent = random.choice(all_sents)
        random_sent = random_sent.replace("<num>", "geen")

        return random_sent

    elif number_faces > 0:

        if number_faces > 1:
            p_sents = ["ik wil dat <num> mensen hun best doen om gedurende de installatie niet te hoesten",
            "Er zijn <num> mensen die ik wil vertellen, dat mijn depressieve aard samen hangt met het voortijdige overlijden van mijn vader",
            "<num> zullen mij niet meer herinneren"]
            all_sents.extend(p_sents)

        if mannen == 1:
            print("een man anwezig")
            p_sents = ["<num> man zal mij vanavond opnieuw horen zingen",
                "<mannen> jonge man zal mij nog nooit hebben zien spelen",
                "<mannen> man zal mij vanavond opnieuw horen zingen",
                ]
            all_sents.extend(p_sents)

        elif mannen > 1:
            p_sents = ["<mannen> jonge mannen zullen mij nog nooit hebben zien spelen",
            "er zijn <mannen> mannen die ik wil vertellen dat mijn depressieve aard samen hangt met het voortijdige overlijden van mijn vader",
            "<mannen> jonge mannen zal ik bewijzen dat ik ook zonde rlichaam verder zal leven",
            "Er zijn <num> mensen in de zaal, waarvan er <mannen> man zijn"]
            all_sents.extend(p_sents)


        if vrouwen > 0:
            p_sents =  [" ik wil voor <vrouwen> vrouwen een liedje zingen",
            "Ik ga <vrouwen> vrouwen vertellen hoe mooi het is dat ze dit gaan meemaken"]

            all_sents.extend(p_sents)

        

        all_sents = [
            "Ik kijk rond. Ik zie <num> mensen. Ik zou deze <num> mensen bij mij in de zaal kunnen hebben. <mannen> mannen, in het publiek. En dan ook <vrouwen> vrouwen. Ik zie iemand van 25 jaar. Misschien moet ik iets voordragen. Of ik zing een lied.",
            "Ik loop door een fabriek in Eindhoven. Ik kom in een ruimte en zie <num> mensen staan. Daarvan zijn er <mannen> mannen, en <vrouwen> vrouwen. Ik besluit door te lopen naar de volgende ruimte.",
            "Ik zie <mannen> mannen.",
            "ik zie <vrouwen> vrouwen.",
            "ik zie nu <num> mensenn. Deze mensen zouden bij mij in het publiek kunnen zitten.",
            "Ik ben in een fabriek in Eindhoven. In een ruimte van 5 bij 4 meter. Ik ben hier met <num> mensen",
            "Ik ben zenuwachtig voor mijn opkomst. Ik ben in een ruimte met <num> mensen.",
            " In de installatie zijn 4 tafels, 8 microfoons. Er zijn vier plafondluidsprekers. Er is de fabriekshal, en de kelder.",
            "Ik zie iemand van 25 jaar oud.",
            "Mijn Curriculum Vitae ziet er zo uit: ik ben geboren in 1962, en ik heet Jeroen. Ik heb in 21 toneelstukken gespeeld volgens mijn Wikipedia pagina. Mijn favoriete rol was mijn hoofdrol in de decamarone. Mijn favoriete schrijver is Frank Wright."]

        random_sent = random.choice(all_sents)
        if number_faces == 1:
            random_sent = random_sent.replace("<num>", "één")
        else:
            random_sent = random_sent.replace("<num>", str(camera.number_faces))

        if mannen == 1:
            random_sent = random_sent.replace("<mannen>", "geen")
        elif mannen == 1:
            random_sent = random_sent.replace("<mannen>", "één")
        else:
            random_sent = random_sent.replace("<mannen>", str(mannen))

        if vrouwen == 1:
            random_sent = random_sent.replace("<vrouwen>", "geen")
        elif vrouwen == 1:
            random_sent = random_sent.replace("<vrouwen>", "één")
        else:
            random_sent = random_sent.replace("<vrouwen>", str(vrouwen))
        # random_sent = random_sent.replace("<vrouwen>", str(vrouwen))
        return random_sent
        
        
        

    


if __name__ == "__main__":



    # Create camera object
    camera = detection_camera.myCamera()

    # start thread 1
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
    


    


    

