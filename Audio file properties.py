import wave
import scipy.io.wavfile as save
import numpy as np
import io
from pydub import AudioSegment 
import soundfile as sf

# Reading the wav file
start = wave.open("start.wav","rb")

end = wave.open("end.wav","rb")

# Converting to bytes
audio_sound_wave_start=start.readframes(-1)
audio_sound_wave_end=end.readframes(-1)

print('Frame Rate:',end.getframerate())

print('Sample Width:',end.getsampwidth())

print('Channels:',end.getnchannels())

# filename='end_test'
# s = io.BytesIO(audio_sound_wave_end)
# audio = AudioSegment.from_raw(s,frame_rate=12500,sample_width=2,channels=2)
# audio.export(filename, format='mp3')

sf.write('end_file.wav',np.array(audio_sound_wave_start),12500,'PCM_16')