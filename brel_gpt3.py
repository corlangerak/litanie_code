import os
import openai
import TTS
from ctts import cTTS



openai.api_key_path = "api_key.txt"

openai.api_key = os.getenv("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")

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




cTTS.synthesizeToFile("/Users/corlangerak/Documents/Work2022-2023/project_davy_ai_jeroen_willems/output.wav", str(completion))
print('Done with sythesizing')

print('playing sound using native player')

file = "/Users/corlangerak/Documents/Work2022-2023/project_davy_ai_jeroen_willems/output.wav"
os.system("afplay " + file)
