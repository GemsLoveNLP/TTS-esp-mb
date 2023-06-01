How to install balcon and use it through Python:

1. Install wine
2. Follow this tutorial https://askubuntu.com/questions/1189046/wine-how-to-use-sapi-5-voices-for-tts-application-balabolka
3. Go to http://www.cross-plus-a.com/bconsole.htm and download the file
4. The file should be in your download folder and is named "balcon.zip"
5. Move the downloaded file to /home/YOURNAME/prefix32/drive_c/Program Files
6. Click extract here on that zip file
7. A folder called "balcon" should appear and inside it their should be a .exe file named "balcon.exe"
8. Go to terminal and try running the following command

  WINEPREFIX="$HOME/prefix32" wine "$HOME/prefix32/drive_c/Program Files/balcon/balcon.exe" balcon -n Zira -t "Hello World"

9. If it works then yay congrats you can now use the balcon function in the python file. if it does not then I also have no idea how to fix it
