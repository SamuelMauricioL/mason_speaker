#!/bin/sh

echo "Installing dependencies 🌱"
sudo apt-get install libasound-dev >/dev/null
echo "✔️ libasound-dev 🎤"

mkdir -p util
sudo curl http://files.portaudio.com/archives/pa_stable_v190700_20210406.tgz --silent --create-dirs -o ./util/portaudio.tgz
sudo tar -zxvf ./util/portaudio.tgz -C ./util >/dev/null
sudo rm -rf ./util/portaudio.tgz
cd util/portaudio/
sudo ./configure >/dev/null
sudo make &> /dev/null
sudo make -s install &> /dev/null
cd ./../../
echo "✔️ portaudio 🎤"


echo ""
echo "Creating environment 🏕️"
python -m venv venv --prompt="mason-speaker"
echo "✔️ (mason-speaker) environment created 🔥"
. venv/bin/activate

echo ""
echo "Installing python packages 📦 in env (mason-speaker)"
# sudo pip install -r requirements.txt >/dev/null
pip install pyaudio &> /dev/null
echo "✔️ pyaudio"
pip install gTTS==2.2.4 >/dev/null
echo "✔️ gTTS"
pip install SpeechRecognition==3.8.1 >/dev/null
echo "✔️ SpeechRecognition"

echo ""