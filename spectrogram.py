# for file utilities
import os.path
# for visualizing the data
import matplotlib.pyplot as plt
# for .wav file handling
import scipy.io.wavfile as wavfile


def make_spectrogram(file_path, destination_folder):
    # Extract file name from path
    file_name = os.path.basename(file_path)

    # Read given .wav file data
    print('Reading: ' + file_name)
    fs, aud = wavfile.read(file_path)
    print(aud.shape)

    # Select left channel only
    if len(aud.shape) > 1:
        aud = aud[:, 0]

    # Trim the first 10 seconds
    if aud.shape[0] > int(fs*5):
        first = aud[:int(fs*5)]
    else:
        first = aud

    # Create spectrogram plot
    power_spectrum, frequencies_sound, time, image_axis = plt.specgram(first, Fs=fs)
    plt.axis('off')

    # Check for destination folder
    # Create destination folder if none exists
    if not os.path.isdir(destination_folder):
        os.mkdir(destination_folder)

    # Save spectrogram image
    image_name = file_name[:-4] + '.png'
    print('Writing ' + image_name + ' to ' + destination_folder)
    plt.savefig(destination_folder + image_name, bbox_inches='tight', pad_inches=0)


if __name__ == '__main__':
    make_spectrogram('Boredom.wav', 'images/')
