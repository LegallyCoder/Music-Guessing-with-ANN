import numpy as np
from scipy.io.wavfile import write
from sklearn.neural_network import MLPRegressor

note_duration = 0.5
samples = []
X = []
y = []
do= [16.35, 32.7, 65.4, 130.8, 261.6, 523.2, 1046.4, 2093.0]
dod = [17.32, 34.64, 69.28, 138.56, 277.12, 554.24, 1108.5, 2217.46]
re = [18.35, 36.7, 73.4, 146.8, 293.6, 587.2, 1174.4, 2349.32]
red= [19.45, 38.9, 77.8, 155.6, 311.2, 622.4, 1244.8, 2489.02]
mi  = [20.6, 41.2, 82.4, 164.8, 329.6, 659.2, 1318.5, 2637.02]
fa  = [21.83, 43.66, 87.31, 174.61, 349.23, 698.46, 1397.91, 2793.83]
fad= [23.12, 46.24, 92.49, 184.97, 369.99, 739.99, 1479.98, 2959.96]
sol  = [24.5, 49.0, 98.0, 196.0, 392.0, 784.0, 1568.0, 3135.96]
sold = [25.96, 51.91, 103.83, 207.65, 415.3, 830.61, 1661.22, 3322.44]
la  = [27.5, 55.0, 110.0, 220.0, 440.0, 880.0, 1760.0, 3520.0]
lad = [29.14, 58.27, 116.54, 233.08, 466.16, 932.33, 1865.66, 3729.31]
si = [30.87, 61.74, 123.47, 246.94, 493.88, 987.77, 1975.53, 3951.07]
melodi=[]#Write the Melody Notes with list type
for z in range(1,10):
    
    for i in range(0, len(melodi)-3):
        b=melodi[i:i+2]
        b.append(i+2)
        c=[]
        c.append(melodi[i+2])
        X.append(b)
        y.append(c)

    X = np.array(X)
    y = np.array(y)


    mlp = MLPRegressor(hidden_layer_sizes=(10), max_iter=1000)
    mlp.fit(X, y)
    d = [melodi[len(melodi)-2],melodi[len(melodi)-1],len(melodi)] 
    tahmin = mlp.predict(np.array([d]))
    melodi.append(tahmin)

for i in melodi:
    samples += np.array(i*np.sin(2*np.pi*np.arange(44100*note_duration)*i/44100), dtype=np.float32)


#Write the samples to a WAV file
write("bethowen.wav", 44100, samples)
