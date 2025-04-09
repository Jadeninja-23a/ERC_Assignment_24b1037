import numpy as np, matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import butter, filtfilt
def lowpass_filter(signal, cutoff, fs, order=5):
    b, a = butter(order, cutoff / (0.5 * fs), btype='low')
    return filtfilt(b, a, signal)

def bandpass_filter(signal, lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return filtfilt(b, a, signal)

def highpass_filter(signal, cutoff, fs, order=4):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='high')
    return filtfilt(b, a, signal)

sample_rate, data = wavfile.read("modulated_noisy_audio.wav")

print(data.ndim)
print(sample_rate)
duration = len(data)/sample_rate
time = np.linspace(0, duration, len(data))
# formatting the data in terms of time 
duration_to_plot = 0.1  # in seconds
samples_to_plot = int(sample_rate * duration_to_plot)

# Slice data and time
time_slice = time[:samples_to_plot]
data_slice = data[:samples_to_plot]
plt.subplot(1,2,1)
plt.plot(time_slice, data_slice)
plt.title("Amplitude vs Time")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
# plotting original audio

N = len(data)
fft_result = np.fft.fft(data)
freqs = np.fft.fftfreq(N, 1/sample_rate)
fft_magnitude = np.abs(fft_result/N)
plt.subplot(1,2,2)
plt.plot(freqs, fft_magnitude)
plt.title("Amplitude vs Frequency")
plt.xlabel("f")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()
mask = freqs>=0
Fc = freqs[mask][np.argmax(fft_magnitude[mask])]
print(freqs[mask][np.argmax(fft_magnitude[mask])])
threshold = 0.4 * np.max(fft_magnitude)

strong_indices = np.where(fft_magnitude[mask] > threshold)[0]
lowcut = freqs[strong_indices[0]]
highcut = freqs[strong_indices[-1]]

data = bandpass_filter(data, lowcut=lowcut,highcut=highcut,fs=sample_rate)
demodulated = data*np.cos(2*np.pi*Fc*time)
filtered = lowpass_filter(demodulated,cutoff=5000, fs=sample_rate)
filtered = highpass_filter(filtered, cutoff=200, fs=sample_rate)
plt.figure(figsize=(10,4))
plt.plot(time[:1000], data[:1000], label="AM Signal")
plt.plot(time[:1000], filtered[:1000], label="Recovered Audio", alpha=1)
plt.legend()
plt.title("AM Demodulation")
plt.grid(True)
plt.tight_layout()
plt.show()

filtered_normalized = filtered / np.max(np.abs(filtered))

# Scale to int16 range
filtered_int16 = np.int16(filtered_normalized * 32767)

# Write to WAV file
wavfile.write("filtered_output.wav", sample_rate, filtered_int16)
