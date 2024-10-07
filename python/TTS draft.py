# -----------------------------------------------------------------------------------------------------------1 Import
from gtts import gTTS
import pyaudio
import wave
import soundfile
import tkinter as tk
# -----------------------------------------------------------------------------------------------------------2 greetings

# greetings!
audio = gTTS(text="welcome user we are humbled to serve you today", lang="en", slow=False)
audio.save('greet.wav')
greet_file_path = "greet.wav"

# Read and rewrite the file with soundfile
data, samplerate = soundfile.read(greet_file_path)
soundfile.write(greet_file_path, data, samplerate)

# Open the WAV file
with wave.open('greet.wav', 'rb') as audio_file:
    # Get the audio file parameters
    sample_rate = audio_file.getframerate()
    num_channels = audio_file.getnchannels()
    sample_width = audio_file.getsampwidth()

    # Initialize PyAudio
    audio_player = pyaudio.PyAudio()

    # Open the audio stream
    stream = audio_player.open(
        format=audio_player.get_format_from_width(sample_width),
        channels=num_channels,
        rate=sample_rate,
        output=True
    )

    # Read the audio data in chunks and play it
    chunk_size = 1024
    data = audio_file.readframes(chunk_size)
    while data:
        stream.write(data)
        data = audio_file.readframes(chunk_size)

    # Clean up
    stream.stop_stream()
    stream.close()
    audio_player.terminate()
# -------------------------------------------------------------------------------------------------3 Func using buttons

def save_text_to_audio():
    mytext = input("enter your text here ")
    audio = gTTS(text=mytext, lang="en", slow=False)
    audio.save('audio.wav')


def speak_text_in_realtime():
    # Create gTTS object
    user_input = entry_widget.get()
    audio = gTTS(text=user_input, lang="en", slow=False)
    audio.save('audio.wav')

    file_path = "audio.wav"

    # Read and rewrite the file with soundfile
    data, samplerate = soundfile.read(file_path)
    soundfile.write(file_path, data, samplerate)

    # Open the WAV file
    with wave.open('audio.wav', 'rb') as audio_file:
        # Get the audio file parameters
        sample_rate = audio_file.getframerate()
        num_channels = audio_file.getnchannels()
        sample_width = audio_file.getsampwidth()

        # Initialize PyAudio
        audio_player = pyaudio.PyAudio()

        # Open the audio stream
        stream = audio_player.open(
            format=audio_player.get_format_from_width(sample_width),
            channels=num_channels,
            rate=sample_rate,
            output=True
        )

        # Read the audio data in chunks and play it
        chunk_size = 1024
        data = audio_file.readframes(chunk_size)
        while data:
            stream.write(data)
            data = audio_file.readframes(chunk_size)

        # Clean up
        stream.stop_stream()
        stream.close()
        audio_player.terminate()

# ---------------------------------------------------------------------------------------4 user interference

window = tk.Tk()
window.title("Big mouth Version_0.1")
# Create input text widget
entry_widget = tk.Entry(window, width=50)
entry_widget.pack()

# Create save button
save_button = tk.Button(window, text="Save Audio", command=save_text_to_audio)
save_button.pack()

# Create speak button
speak_button = tk.Button(window, text="Speak Text", command=speak_text_in_realtime)
speak_button.pack()

# Create status label
status_label = tk.Label(window, text="Enter the text above!")
status_label.pack()

# Run the Tkinter event loop
window.mainloop()

