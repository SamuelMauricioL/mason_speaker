echo "Installing dependencies 🌱"
brew install portaudio &>/dev/null
echo "✔️ portaudio 🎤"
brew install flac &>/dev/null
echo "✔️ flac 🎤"
brew install ffmpeg &>/dev/null
echo "✔️ ffmpeg"

echo ""
echo "Creating environment 🏕️"
python3 -m venv env --prompt="mason-speaker" &>/dev/null
echo "✔️ (mason-speaker) environment created 🔥"
source env/bin/activate

echo ""
echo "Installing python packages 📦 in env (mason-speaker)"
CFLAGS="-I/opt/homebrew/include -L/opt/homebrew/lib" python3 -m pip install pyaudio &>/dev/null
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

mkdir -p util/audio
echo ""
echo "Installed a Mason Speaker! 🧱🎤"
