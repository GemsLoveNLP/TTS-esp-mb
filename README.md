# TTS-esp-mb
Definition:
- This file is just a way for python to be able to access the espeak installed on your machine 
- The things this file can do can be acheived through the command line

Prereq:
- install espeak
- install mbrola
- for installation guide check out <https://youtu.be/stMPWkRvTSA>


Function explanation:

1. speak(text, voice, pitch, speed):
  - Speak the text given to it
  - text: the text to be translated to speech
  - voice: the name of the voice which will read out the text
    (the default is en-fr1 you can check out get_voices() for more info)
  - pitch: the pitch of the voice in integer range of 0 to 99 (default is 50)
  - speed: the speed in words per minute of the speech in integer range of 80 to 450 (default is 175)

2. get_voices():
  - print the name of the voices to the terminal
  - there are two batches 
  - the first is the espeak voices
  - the second is the mbrola voices (prefered compared to the espeak)

3. help():
  - list all commands which could be run in the terminal with espeak
  - equivalent to running "espeak -h" in the terminal