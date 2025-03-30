from llama_cpp import Llama
from elevenlabs import stream
from elevenlabs.client import ElevenLabs
from elevenlabs import VoiceSettings
from RealtimeSTT import AudioToTextRecorder
import sys


client = ElevenLabs(
    api_key="sk_f5b478c94526eb3172ec638f9f10eabbca437b25b5980540",
)

# Configure Voice Settings
client.voices.edit_settings(
    voice_id="84Fal4DSXWfp7nJ8emqQ",
    request=VoiceSettings(
        stability=1,
        similarity_boost=1,
        style=0,
        speed=1.1,  # Increase speech speed by 10%
    )
)

# Load the Llama model
llm = Llama(model_path="/Users/nadaremah/Documents/llama-code/unsloth.Q8_0.gguf")


prompt1 = """You are a helpful AI assistant. Answer the following question clearly and concisely:

Question:""" # Hi, I'm a new student and I'm trying to finalize my acceptance. I was wondering, what happens if I fail to submit a certified final transcript?"""

####################config data^^^#####################
def start_recorder():
    # while True:  
    recorder = AudioToTextRecorder(
        wake_words="Hello_wolfy!",
        on_recording_stop=my_stop_callback
    )
    print('Say "Hello Wolfy!" to start recording.')
    recorder.text(process_text)

def fin_play():
	audio_stream = client.text_to_speech.convert_as_stream(
    	text=trimmed_text,
    	voice_id="84Fal4DSXWfp7nJ8emqQ",
    	model_id="eleven_multilingual_v2"
	)
	stream(audio_stream)
	start_recorder()

trimmed_text= ""

def get_repo(prompt):
    global trimmed_text
    response = llm(prompt, max_tokens=100)
    text_response = response["choices"][0]["text"]  # Extract text
    print(text_response)
	# Extract text after ("Answer:")
    trimmed_text = get_text_after_keyword(text_response, "Answer:")
    print(f"\nPlaying from: {trimmed_text}")  
    fin_play()
    



# Function to get text AFTER a specific word ("Answer:")
def get_text_after_keyword(textt, keyword):
    #Returns the text after the first occurrence of 'keyword'.
    index = textt.find(keyword)
    if index != -1:  # If the keyword is found
        return textt[index + len(keyword):].strip()  # Extract text after keyword
    return textt  # Return full text if keyword is not found


prompt = ""

def process_text(text):
    global prompt
    print("Recorded text:", text)
    
    # Concatenate the preamble and the recorded text
    prompt = prompt1 + " " + text
    print(prompt)
    get_repo(prompt)
    
    
def my_stop_callback():
    print("\n Recording stopped!")


if __name__ == "__main__":
    try:
        start_recorder()  # Start the recording process
        while True:  # Keeps the program alive
            pass  
    except KeyboardInterrupt:
        print("\nProgram terminated.")
        

#TIS WEIRD AND BUGGY AND IT FEELS LIKE ITS GONNA FALL APART BUT IT WORKS AND LOOPS AT LEAST.
#ILL TRYTA FIX IT