# Spectrogram Creator

The script takes a set of .wav files and creates spectrogram images of
each of them, then zips the images in files under 100mb

## Requirements
* matplotlib
* scipy.io

## Usage
```commandline
python main.py [path to file tree containing .wav files]
```
Alternatively, the script defaults to looking for an
"assets" folder in the same directory as the script
containing .wav files

## Work to be had
- finish clean_up() in filehandler.py
- Spectrograms of audio files less than 10 seconds should go flat after their duration show some unexpected artifacts
- Take 10 second clip of files greater than 10 seconds instead of first 10 seconds to give better context of the sound 
being classified
- add command line options to:
  - Change clip length
  - do clean_up() after job
  - set destination of zip files
  - set verbosity of script 
- move sample audio files out of repo and populate a repo of non-copyrighted audio files