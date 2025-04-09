# AM Demodulation using Python

I demodulated this amplitude-modulated (AM) audio signal using Python with the help of scipy, numpy, and matplotlib.

The amplitude modulated wave has the form:
(1 + m(t)) * sin(2πf_c t)

To demodulate this, we multiply the signal again by sin(2πf_c t), which gives:
(1 + m(t)) * sin²(2πf_c t)

Using the identity:
sin²(θ) = (1 - cos(2θ)) / 2

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

the Code implementation

![image](https://github.com/user-attachments/assets/511ec21d-f000-43aa-ae21-10e4014b43df)


The Audio 

![image](https://github.com/user-attachments/assets/b923f232-d45c-45cc-be22-259e37e3207f)



2. **FFT Analysis**
Used numpy.fft.fft() to analyze the signal in the frequency domain and find the carrier frequency. .

![image](https://github.com/user-attachments/assets/d9537ed5-a3f3-4dac-b019-397825229d0a)\\


This is the graph in the frequency domain

![image](https://github.com/user-attachments/assets/88a78317-c1c2-40b0-9f4f-1b5efd950e49)\\

The code to fetch the carrier frequency

![image](https://github.com/user-attachments/assets/a8253796-fd4f-4b4a-947c-da2c820c7feb)

The frequency with the highest magnitude came out to be around 10,582 Hz, so that was taken as the carrier frequency f_c

3. **Demodulation**
   Designing a bandpass filter based on the carrier frequency
   
   ![image](https://github.com/user-attachments/assets/767561ff-0f62-4344-9ca0-cde93c720e6d)\\

Multiplied the modulated signal by sin(2πf_c t) and applied a low-pass filter using scipy.signal.butter() and filtfilt() to remove the high-frequency component.  
Here I am applying it on data with a bandpass filter and without to compare graphs with and without noise 

![image](https://github.com/user-attachments/assets/6a172ab2-5d85-4418-9d6f-67a069d9b129)\\



 Then scaled the result using:
    recovered = 1- 2 * filtered 

here are my lowpass, highpass and bandpass functions


![image](https://github.com/user-attachments/assets/f5f2599b-5be4-4dd6-a439-8aa30d134ccf)\\




4. **Frequency Shifting**
Shifted frequency to make the audio more clearer

![image](https://github.com/user-attachments/assets/217e8fe7-e7e5-4266-9934-6cc46feb7c74)

5. **Plotting**  
Plotted everything
The code for plotting the bandpass filtered original audio and the demodulated audio

![image](https://github.com/user-attachments/assets/e463a6ef-38fc-463e-960a-86baa2c3c470)


This is the plot 

![image](https://github.com/user-attachments/assets/7510390b-d8c2-44e7-9728-f754614c5f60)


The code for plotting bandpass filtered demodulated vs just demodulated without bandpass filtering

![image](https://github.com/user-attachments/assets/ba4573eb-057b-418f-be19-191c24df1fa3)

This is the plot 

![image](https://github.com/user-attachments/assets/c1fde9a1-ebaa-449e-9233-0e25ab88be77)

6. **Audio Recovery**
Recovering the audio from the demodulated data 

![image](https://github.com/user-attachments/assets/49f95936-13cd-41fb-a716-df0286192074)


##  Libraries Used

- numpy  
- scipy  
- matplotlib

## Files

- modulated_noisy_audio.wav – input AM signal  
- plotfft.py – main script  
- filtered_output.wav – demodulated output  
- .png plots – visualizations of time and frequency domain signals


