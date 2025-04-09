# AM Demodulation using Python

I demodulated this amplitude-modulated (AM) audio signal using Python with the help of scipy, numpy, and matplotlib.

The amplitude modulated wave has the form:
(1 + m(t)) * cos(2πf_c t)

To demodulate this, we multiply the signal again by cos(2πf_c t), which gives:
(1 + m(t)) * cos²(2πf_c t)

Using the identity:
cos²(θ) = (1 + cos(2θ)) / 2

This breaks into two components:
- A low-frequency part containing m(t)
- A high-frequency component around 2f_c

We apply a low-pass filter to remove the high-frequency part and isolate the baseband signal.

After filtering, the result is:
(1 + m(t)) / 2

To get back m(t), we multiply the result by 2 and subtract 1.

## Implementation Steps

1. **Load and Visualize Audio**  
Used scipy.io.wavfile to read the .wav file and extract the audio signal as a long array of samples. Visualized the waveform using matplotlib.

2. **FFT Analysis**  
Used numpy.fft.fft() to analyze the signal in the frequency domain and find the carrier frequency. The frequency with the highest magnitude came out to be around 10,582 Hz, so that was taken as the carrier frequency f_c.

3. **Demodulation**  
Multiplied the modulated signal by cos(2πf_c t) and applied a low-pass filter using scipy.signal.butter() and filtfilt() to remove the high-frequency component.  
Then scaled the result using:
    recovered = 2 * filtered - 1

4. **Filtering**  
Applied a bandpass filter around the audio bandwidth to remove background noise and unwanted frequencies before or after demodulation.

5. **Plotting**  
Used matplotlib to generate the following plots:
- Original AM signal
- Noisy demodulated signal
- Clean filtered signal
- FFT plots of the audio

##  Libraries Used

- numpy  
- scipy  
- matplotlib

## Files

- modulated_noisy_audio.wav – input AM signal  
- plotfft.py – main script  
- filtered_output.wav – demodulated output  
- .png plots – visualizations of time and frequency domain signals


