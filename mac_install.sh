echo "Installing dependencies 🌱"
brew install portaudio &>/dev/null
echo "✔️ portaudio 🎤"
brew install flac &>/dev/null
echo "✔️ flac 🎤"

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
pip install SpeechRecognition==3.8.1 &>/dev/null
echo "✔️ SpeechRecognition"

brew install ffmpeg &>/dev/null
echo "✔️ ffmpeg"

mkdir -p util/audio
echo ""
echo "Installed a Mason Speaker! 🧱🎤"
