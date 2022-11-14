import os
import openai
from TTS.utils.synthesizer import Synthesizer
from ctts import cTTS
import argparse

from argparse import RawTextHelpFormatter




# openai.api_key_path = "api_key.txt"
openai.api_key = ("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")

def get_completion(prompt):
    completion = openai.Completion.create(
    model="text-davinci-002",
    prompt=prompt,
    max_tokens=50,
    temperature=0.8
    )
    return completion["choices"][0]["text"]


prompt = str(input("Input: "))
# prompt = "hoe is het?"

completion = get_completion(prompt)
print('Done with gpt3')
print("GPT3 OUTPUT:", str(completion))

parser = argparse.ArgumentParser(
        formatter_class=RawTextHelpFormatter,
    )
parser.add_argument("--use_cuda", type=bool, help="Run model on CUDA.", default=True)
args = parser.parse_args()


model_path = None
config_path = None
speakers_file_path = None
language_ids_file_path = None
vocoder_path = None
vocoder_config_path = None
encoder_path = None
encoder_config_path = None
text = str(completion)
output_wav = '/Users/corlangerak/Documents/Work2022-2023/project_davy_ai_jeroen_willems/output.wav'

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


wav = synthesizer.tts(
        text,
        args.speaker_idx,
        args.language_idx,
        args.speaker_wav,
        reference_wav=args.reference_wav,
        style_wav=args.capacitron_style_wav,
        style_text=args.capacitron_style_text,
        reference_speaker_name=args.reference_speaker_idx,
    )

    # save the results
print(" > Saving output to {}".format(args.out_path))
synthesizer.save_wav(wav, output_wav)
# cTTS.synthesizeToFile("/Users/corlangerak/Documents/Work2022-2023/project_davy_ai_jeroen_willems/output.wav", str(completion))
print('Done with sythesizing')

print('playing sound using native player')

file = "/Users/corlangerak/Documents/Work2022-2023/project_davy_ai_jeroen_willems/output.wav"
os.system("afplay " + file)
