import subprocess as cmdLine
import playsound

def espeak(text,voice='default',pitch=50, speed=175, vol=100, gap=0 ):
    command = f'espeak -v {voice} -p {pitch} -s {speed} -a {vol} -g {gap} "{text}"'
    print(command)
    cmdLine.run(command, shell=True)

def espeak_get_voices():
    cmdLine.run('espeak --voices', shell=True)
    cmdLine.run('espeak --voices=mb', shell=True)

def espeak_help():
    cmdLine.run('espeak -h', shell=True)

# festival
def festival(text):
    f = open('script.txt','w')
    f.write(text)
    f.close()
    command = f'festival --tts script.txt'
    cmdLine.run(command, shell=True)

# balcon
def balcon(text, name='ZiraPro', pitch=0):
    command = f'WINEPREFIX="$HOME/prefix32" wine "$HOME/prefix32/drive_c/Program Files/balcon.exe" balcon -n {name} -t "{text} -p {pitch}"'
    cmdLine.run(command, shell=True)

def balcon_list():
    cmdLine.run('WINEPREFIX="$HOME/prefix32" wine "$HOME/prefix32/drive_c/Program Files/balcon.exe" balcon -l', shell=True)

#?---------------------------------------------------------
def mimic(text, voice='en_US/cmu-arctic_low'):
    cmdLine.run(f'mimic3 -v {voice} "{text}"',shell='True')
#?---------------------------------------------------------

