# TTS-esp-mb
Definition:
- This file is just a way for python to be able to access the espeak installed on your machine 
- The things this file can do can be acheived through the command line

# Prereq:

for espeak+mbrola:
- install espeak
- install mbrola
- for installation guide check out <https://youtu.be/stMPWkRvTSA>

for balcon (prefered):
- run the "install.sh" file


# Function explanation:

1. speak(text, voice, pitch, speed):
  - Speak the text given to it
  - text: the text to be translated to speech
  - voice: the name of the voice which will read out the text
    (the default is mb-en1 you can check out get_voices() for more info)
  - pitch: the pitch of the voice in integer range of 0 to 99 (default is 50)
  - speed: the speed in words per minute of the speech in integer range of 80 to 450 (default is 175)
  - vol: the volume in integer range from 0 to 200 (default is 100)
  - gap: the pause between words in the unit of centisecond (default is 0)

2. get_voices():
  - print the name of the voices to the terminal
  - there are two batches 
  - the first is the espeak voices
  - the second is the mbrola voices (prefered compared to the espeak)

3. help():
  - list all commands which could be run in the terminal with espeak
  - equivalent to running "espeak -h" in the terminal

4. festival(text):
  - speak the text using the festival model

6. balcon(text):
  - speak the text using a micorsoft model
  - the commands are sketchy as it is created by me and I have no idea what kind of things gonna happen
  - Pro: extremely good sounding
  - Con: I have no idea how the command works

7. balcon_list():
  - list all available SAPI voices
