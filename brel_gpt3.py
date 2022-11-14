import os
import openai
from TTS.utils.synthesizer import Synthesizer
from ctts import cTTS
import argparse
import winsound


from argparse import RawTextHelpFormatter




# openai.api_key_path = "api_key.txt"
openai.api_key = ("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")

# def get_completion(prompt):
#     completion = openai.Completion.create(
#     model="text-davinci-002",
#     prompt=prompt,
#     max_tokens=50,
#     temperature=0.8
#     )
#     return completion["choices"][0]["text"]


# prompt = str(input("Input: "))
# prompt = "hoe is het?"

# completion = get_completion(prompt)
# print('Done with gpt3')
# print("GPT3 OUTPUT:", str(completion))

parser = argparse.ArgumentParser(
        formatter_class=RawTextHelpFormatter,
    )

parser.add_argument("--use_cuda", type=bool, help="Run model on CUDA.", default=True)
args = parser.parse_args()


model_path = 'C:/Users/Gebruiker/Documents/litanie/models_voice/checkpoint_70000.pth'
config_path = 'C:/Users/Gebruiker/Documents/litanie/models_voice/config.json'
speakers_file_path = None
language_ids_file_path = None
vocoder_path = None
vocoder_config_path = None
encoder_path = None
encoder_config_path = None
# text = str(completion)
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
        args.use_cuda,
    )



def chat(question,chat_log = None) -> str:
    if(chat_log == None):
        chat_log = start_chat_log

    prompt = f"{chat_log}\n\nQ: {question}\nA:"
    response = completion.create(prompt = prompt, engine =  "davinci", temperature = 0.87, top_p=0.5, frequency_penalty=0.5, 
    presence_penalty=0.7, best_of=3, max_tokens=150, stop = "\n\nQ: ")
    return response.choices[0].text

def modify_start_message(chat_log,question,response) -> str:
    if chat_log == None:
        chat_log = start_chat_log
    chat_log += f"\n\nQ: {question}\nA: {response}\n"
    return chat_log



    
# prompt = "hoe is het?"

if __name__ == "__main__":

    start_chat_log = """Ik ben Jeroen Willems, acteur en zanger. Ik ben nu een chatbot die geïnterviewd wordt en antwoord geeft op alle vragen vanuit mijn kennis over Jeroen Willems, het theater en auteurschap. Ik was een bekende Nederlandse acteur uit Maastricht maar ben inmiddels overleden. Op mijn sterfdag kreeg ik een hartaanval vlak voor een première in Carre. Ik geef graag antwoord op de vragen in dit interview, maar zal soms ook iets vertellen dat niet gevraagd is.\n\nQ: Wil je gast zijn op het Nederlands filmfestival?\nA: Hoezo? Waarom in godsnaam?\n\nQ: Hoe interpreteer je Brel?\nA: Brel nadoen is onmogelijk, op zoek gaan naar diens compromisloze eerlijkheid, overgave, tederheid en poëzie; dat is een poging waard.\n\nQ: Is het extra moeilijk is om\nbestaande figuren te dramatiseren?\nA: Het moeilijkste is om van Brels expressie en klank vandaan te komen. Allicht heb ik de videobanden van Brels optredens gezien en gehoord, zoals ook die van Sonneveld en foto's van Troelstra: hoe stonden ze, hoe keken ze? Ze zitten de hele tijd op je schouder mee te kijken, en toch moet ik me op de een of andere manier onder hen uit worstelen. Ik zie wel wat voor 'acteursschakels' Brel maakt, maar ik kan die niet zomaar overnemen.\n\nQ: Het lijkt alsof je een soort aversie hebt tegenover Nederlandse film, klopt dat?\nA:Nee, ik heb niks tegen Nederlandse films. Ze worden beter. Wel heb ik vaak moeite met de scenario's. Zo één op één. Ik hou van jou wordt ik hou van jou. Als je naar Britse of Amerikaanse producties kijkt, zitten er meer lagen in. Acteurs praten langs elkaar heen en hebben het toch over hetzelfde. Dat is spannender. Vaak zit er ook een team van schrijvers op een project. Nederlandse filmmakers zijn bang voor veel tekst. Dat begrijp ik niet goed. In de serie In therapie zaten hele lappen. Er stond lang een camera op het gezicht van iemand die praat. Het werkte. Het kan dus wel.\n\nQ: Wat zijn de kenmerken van jouw personages?\nA: Geheimzinnige personages, met een haast dierlijke, ingehouden kracht; gevaarlijk, met een erotische uitstraling, dat is Willems.\n\nQ: Ben je op een andere manier aan het acteren als je voor de camera staat?\nA: Ik heb wel de neiging op camera te veel te doen met mijn ogen. Je denkt vaak: zal de kijker wel registreren wat ik denk? Zie je niet dat ik zwaar lijd? Het kan altijd minder.\n\nQ: Waar ben je onzeker over?\nA: Gaat het niet te veel over mijn twijfels en onzekerheden? Dat heeft vaak zo de overhand in interviews.\n\nQ: ",

    """
    # vraag = str(input("Q: "))
    completion = openai.Completion()

    question = ""
    while True:
        question = input("Question: ")
        if question == "stop":
            break

        print('send to gpt3')
        response = chat(question,start_chat_log)
        start_chat_log = modify_start_message(start_chat_log,question,response)


        print("GPT3 OUTPUT:", response)

        # save the results
        print(" > Saving output to {}".format(output_wav))
        wav = synthesizer.tts(response,
    #     args.speaker_idx,
    #     args.language_idx,
    #     args.speaker_wav,
    #     reference_wav=args.reference_wav,
    #     style_wav=args.capacitron_style_wav,
    #     style_text=args.capacitron_style_text,
    #     reference_speaker_name=args.reference_speaker_idx,
        )
        synthesizer.save_wav(wav, output_wav)
        print('Done with sythesizing')
        file = "C:/Users/Gebruiker/Documents/litanie/voice_output/output.wav"
        # os.system("afplay " + file)
        winsound.PlaySound(file, winsound.SND_FILENAME)


   
