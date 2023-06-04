import cli

# cli.get_voices()
# cli.speak("Hello I am ready what do you want me to do", voice="mb-fr1-en", speed=140)

while True:
    i = input()
    if i=='q':break
    cli.balcon(i)