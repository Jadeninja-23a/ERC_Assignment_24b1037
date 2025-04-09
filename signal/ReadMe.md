
I used Python along with the `scipy`, `numpy`, and `matplotlib` libraries to implement this.

The amplitude modulated wave is of the form:

\[
(1 + m(t)) \cdot \cos(2\pi f_c t)
\]

To demodulate it, I multiply the signal again by \( \cos(2\pi f_c t) \), which gives:

\[
(1 + m(t)) \cdot \cos^2(2\pi f_c t)
\]

Using the identity \( \cos^2(\theta) = \frac{1 + \cos(2\theta)}{2} \), this expands to two components: one low-frequency part and one high-frequency component around \( 2f_c \). Since we only care about extracting \( m(t) \), I apply a low-pass filter to remove the higher-frequency part, leaving just the component that contains \( m(t) \).

At this point, the output is \( \frac{1 + m(t)}{2} \), so to recover \( m(t) \), I multiply the signal by 2 and subtract 1.

For implementation, I first used `scipy.io.wavfile` to load the audio file and get the signal as a long array of amplitude values. Then I plotted the waveform using `matplotlib`.

To analyze it in the frequency domain, I used `numpy.fft.fft()` and plotted the frequency spectrum. The frequency with the highest magnitude came out to be around **10,582 Hz**, which I took as the carrier frequency \( f_c \).

From there, I created two separate plots:
- One for the noisy demodulated signal (before filtering)
- One for the clean, filtered version

For the filtering part, I used a **bandpass filter** to isolate the frequency range of interest. `scipy.signal` and `numpy` have a lot of helpful functions that make this easy.

Finally, I demodulated the signal using the method described above and plotted everything using `matplotlib`.

---
