echo "Creating environment 🏕️"
python -m venv env --prompt="mason-speaker" &>/dev/null
echo "✔️ (mason-speaker) environment created 🔥"
. env/bin/activate

echo ""
echo "Installing python packages 📦 in env (mason-speaker)"
pip install pyaudio==0.2.12 &>/dev/null
echo "✔️ pyaudio"
pip install gTTS==2.2.4 &>/dev/null
echo "✔️ gTTS"
pip install wavio==0.0.7 &>/dev/null
echo "✔️ wavio"
pip install sounddevice==0.4.5 &>/dev/null
echo "✔️ sounddevice"
pip install SpeechRecognition==3.8.1 &>/dev/null
echo "✔️ SpeechRecognition"
pip install git+https://github.com/openai/whisper.git &>/dev/null
echo "✔️ Whisper"
pip install tkintertable==1.3.3 &>/dev/null
echo "✔️ tkintertable"

mkdir -p util/audio
echo ""
echo "Installed a Mason Speaker! 🧱🎤"