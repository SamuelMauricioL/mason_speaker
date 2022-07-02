# Mason Speaker

Mason Speaker is a task automation wizard

You can interact with it to create code templates for your preferred language, automate your daily tasks and all just by asking the assistant.

<br>

## Installation

If you are using any Linux distribution, you may need to follow the steps below to install all dependencies.

<br>

### Step 1) Install pyaudio

**speech_recognition** library needs **pyaudio** plugin...

And to install pyaudio first we need to install portaudio modules:

```bash
sudo apt-get install libasound-dev
```

Download the portaudio archive from:

```bash
http://files.portaudio.com/download.html
```

Unzip the archive:

```bash
tar -zxvf [portaudio.tgz]
```

Enter the directory, then run:

```bash
./configure && make
```

Install:

```bash
sudo make install
```

And finally:

```bash
sudo pip install pyaudio
```

Check the version of pyaudio, it should be 0.2.9

<br>

### Step 2) Install others packages

```bash
sudo pip install gTTS
```

<br>

### Step 3) Play with Mason Speaker :)

Run the next command to use and config your personal Mason Speaker

```bash
python main.py
```

## Others Configurations

If you want to change the assistant voice you can follow the following guide

```bash
https://pythonprogramminglanguage.com/text-to-speech/
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
