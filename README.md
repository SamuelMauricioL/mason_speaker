# Mason Speaker

We have plenty of general-purpose voice assistants, but are there any that are focused on developers 👨‍💻?

I want to introduce you to Mason Speaker 👩 a voice assistant for developers that I have been working on.

### Recipe:

- Whisper👂 : Voice recognition - OpenAI
- gTTS 🔉 : Text-to-Speech - Google
- Mason 🧱 : Generation of code templates - Felix Angelov

### Initial focus:

My goal was to create a voice interface to use Mason which is a great tool for generating boilerplate code templates through bricks and thus avoiding boring code.

### It's general purpose for developers:

You can take this project as a basis to automate your repetitive tasks through voice commands.

### Voice commands (English):

- select project : To locate your project directory
- open project. : Open your selected project in VS-Code
- create feature : Create the template of your new features using your bricks
- search brick. : Search for a new brick on brickhub.dev

<br>

## Installation

You just need to run **install.sh** to create a Python environment ready to use Mason Speaker

For Linux:

```bash
. linux_install.sh
```

For Mac:

```bash
souce mac_install.sh
```

<br>

## Play with Mason Speaker :)

Run the next command to use and config your personal Mason Speaker

```bash
python main.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
