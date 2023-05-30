import subprocess as cmdLine

def speak(text,voice='mb-us3',pitch=50, speed=175):
    command = f'espeak -v {voice} -p {pitch} -s {speed} "{text}"'
    print(command)
    cmdLine.run(command, shell=True)

def get_voices():
    cmdLine.run('espeak --voices', shell=True)
    cmdLine.run('espeak --voices=mb', shell=True)

def help():
    cmdLine.run('espeak -h', shell=True)

# get_voices()
help()