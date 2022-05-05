import os.path
import glob
from os.path import basename
from zipfile import ZipFile


# Looks for .wav files in directory at path and returns a list of their absolute paths
def get_wav_files(path):
    names = glob.glob(path + '*.wav')
    names = names + glob.glob(path + '\\*\\*.wav')
    print([os.path.basename(x) for x in names])
    return names


# Archives image directory as .zip files and places them in 'zips' directory
def zip_files():
    # Check for `zips` directory
    # Create directory if none exists
    if not os.path.isdir('zips'):
        os.mkdir('zips')

    # Navigate through 'images' directory
    for root, folderNames, fileNames in os.walk('images', topdown=False):
        print('root: ' + str(root))
        print('folders: ' + str(folderNames))
        print('files:  ' + str(fileNames))

        # Condition to keep from zipping root 'images' directory
        if len(folderNames) == 0:

            # Create new archive in 'zips' directory for each subdirectory of 'images'
            print('Creating Archive: ' + root[-1:] + '.zip')
            with ZipFile('zips\\' + root[-1:] + '.zip', 'w') as zipObj:
                for file in fileNames:
                    print('Archiving: ' + str(file))
                    file_path = os.path.join(root, file)
                    zipObj.write(file_path, basename(file_path))
                zipObj.close()


# Removes 'images' and 'zips' directories
def clean_up():
    return None


if __name__ == '__main__':
    # get_wav_files(os.getcwd() + '\\assets\\')
    zip_files()
