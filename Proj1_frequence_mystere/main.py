import numpy as np
import librosa
import matplotlib.pyplot as plt

x, sr = librosa.load('/Users/lixiquan/Documents/Telecom-Paris/Y1_2/SI101/Proj1_frequence_mystere/data/symboleU2.wav', sr=8000)
X = np.fft.fft(x)
X.argmax()

plt.figure()
plt.plot(x)
plt.show()

plt.figure()
plt.plot(X)
plt.show()

print(x)


