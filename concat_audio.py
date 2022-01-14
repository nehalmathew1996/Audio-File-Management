import os
import wave

in_files = ["start.wav","name.wav","end.wav"]
out_file = "output_combined.wav"

data= []
for in_file in in_files:
    w = wave.open(in_file, 'rb')
    data.append( [w.getparams(), w.readframes(w.getnframes())] )
    w.close()
    
output_v1 = wave.open(out_file, 'wb')
output_v1.setparams(data[0][0])
for i in range(len(data)):
    output_v1.writeframes(data[i][1])
output_v1.close()

os.system("output_combined.wav")