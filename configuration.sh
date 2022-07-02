#!/bin/sh

echo "Creating environment 🏕️"
python -m venv venv --prompt="mason-speaker"
echo "✔️ (mason-speaker) environment created 🔥"
. venv/bin/activate

echo ""
echo "Installing packages 📦 in env (mason-speaker)"
# sudo pip install -r requirements.txt >/dev/null
pip install gTTS==2.2.4 >/dev/null
echo "✔️ gTTS"
pip install SpeechRecognition==3.8.1 >/dev/null
echo "✔️ SpeechRecognition"

echo ""