#!/bin/bash

sudo dpkg --add-architecture i386 
sudo mkdir -pm755 /etc/apt/keyrings
sudo wget -O /etc/apt/keyrings/winehq-archive.key https://dl.winehq.org/wine-builds/winehq.key
sudo wget -NP /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/ubuntu/dists/focal/winehq-focal.sources
sudo apt update
sudo apt install --install-recommends winehq-stable

WINEPREFIX="$HOME/prefix32" WINEARCH=win32 wine wineboot
cd "$HOME/prefix32/drive_c/Program Files/"
wget http://www.cross-plus-a.com/balcon.zip
unzip balcon.zip

wget https://download.microsoft.com/download/A/6/4/A64012D6-D56F-4E58-85E3-531E56ABC0E6/x86_SpeechPlatformRuntime/SpeechPlatformRuntime.msi
WINEPREFIX="$HOME/prefix32" wine msiexec /i SpeechPlatformRuntime.msi
wget https://download.microsoft.com/download/4/0/D/40D6347A-AFA5-417D-A9BB-173D937BEED4/MSSpeech_TTS_en-US_ZiraPro.msi
WINEPREFIX="$HOME/prefix32" wine msiexec /i MSSpeech_TTS_en-US_ZiraPro.msi

sudo apt install winetricks
WINEPREFIX="$HOME/prefix32" winetricks msxml6

WINEPREFIX="$HOME/prefix32" wine "$HOME/prefix32/drive_c/Program Files/balcon.exe" balcon -n ZiraPro -t "Successfully installed balcon and ZiraPro"
