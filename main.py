import os
import sys

import spectrogram
import filehandler


def make_spectrograms(path=os.getcwd()+'\\assets\\'):
    # Creates 'images' directory if not already there
    if not os.path.isdir('images'):
        os.mkdir('images')

    # .wav file paths
    files = filehandler.get_wav_files(path)

    # Create spectrogram images of each .wav file
    # Limits 500 images per directory
    image_count = 0
    folder_num = 0
    for file in files:
        if image_count == 500:
            folder_num += 1
            image_count = 0
        spectrogram.make_spectrogram(file, 'images/' + str(folder_num) + '/')
        image_count += 1


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(sys.argv)
        make_spectrograms(path=sys.argv[1]+"\\")
    else:
        print(0)
        make_spectrograms()

    if len(os.listdir(os.getcwd())) != 0:
        filehandler.zip_files()
