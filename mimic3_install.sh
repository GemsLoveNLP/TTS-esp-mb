#!/bin/bash

pip install --upgrade pip
pip install mycroft-mimic3-tts[all]

mimic3 -v en_US/cmu-arctic_low "mimic3 is  downloaded successfully"