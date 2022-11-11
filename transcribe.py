import os
import whisper
import pathlib
# from shutil import copyfile
# from genericpath import exists
import natsort
import glob
# assign directory
# directory = '/Users/corlangerak/Documents/Work2022 2023/Project Davy van Gerven AI jeroen willems/trim-recordings-Jeroen/'
# directory = '/Users/corlangerak/Documents/Work2022 2023/Project Davy van Gerven AI jeroen willems/test'
directory = "C:/Users/Gebruiker/Documents/litanie/litanie_code/wavs_split_final"

model = whisper.load_model('large')
language_whisper = "dutch"

options = dict(language=language_whisper)
transcribe_options = dict(task="transcribe", **options)

metadata = open(os.path.join("C:/Users/Gebruiker/Documents/litanie/dataset/metadata.csv"), mode="w", encoding="utf8")

# iterate over files in
# that directory
# wav_files = glob.glob('C:/Users/Gebruiker/Documents/litanie/litanie_code/wavs_split_final/*.wav')



audios = []


for filename in os.listdir(directory):
    source_file = os.path.join(directory,filename)
    audios.append(source_file)

sortedwav_files = natsort.natsorted(audios)

for audio in sortedwav_files:
    result = model.transcribe(audio, **transcribe_options)
    filename = pathlib.Path(audio).stem
    transcription = (f'{filename}|{result["text"]}\n')
    metadata.write(transcription)
    print(f'DONE with {filename}')


metadata.close


                            
