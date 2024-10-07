from gtts import gTTS
import pyaudio
import wave
import soundfile
from playsound import playsound
mytext = input("enter your text here ")
audio = gTTS(text=mytext, lang="en", slow=False)
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


