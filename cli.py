import subprocess as cmdLine

def speak(text,voice='default',pitch=50, speed=175, vol=100, gap=0 ):
    command = f'espeak -v {voice} -p {pitch} -s {speed} -a {vol} -g {gap} "{text}"'
    print(command)
    cmdLine.run(command, shell=True)

def get_voices():
    cmdLine.run('espeak --voices', shell=True)
    cmdLine.run('espeak --voices=mb', shell=True)

def help():
    cmdLine.run('espeak -h', shell=True)

# festival
def festival(text):
    f = open('script.txt','w')
    f.write(text)
    f.close()
    command = f'festival --tts script.txt'
    cmdLine.run(command, shell=True)

# balcon
def balcon(text, name='Hazel'):
    command = f'WINEPREFIX="$HOME/prefix32" wine "$HOME/prefix32/drive_c/Program Files/balcon/balcon.exe" balcon -n {name} -t "{text}"'
    cmdLine.run(command, shell=True)

def balcon_list():
    cmdLine.run('WINEPREFIX="$HOME/prefix32" wine "$HOME/prefix32/drive_c/Program Files/balcon/balcon.exe" balcon -l', shell=True)

# get_voices()
# help()
# balcon_list()