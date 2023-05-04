# hugging-chat-simple-cli

## Quick Implementation of Code Found within this Artcile:
https://www.kdnuggets.com/2023/05/huggingchat-python-api-alternative.html

## HuggingChat Python API: Your No-Cost Alternative

## Setup
* No license key is needed! =)
* Create a new local Python environment
```bash
$ python3 -m venv env
$ source ./env/bin/activate
$ pip install hugchat
$ python main.py
```

## CLI Interface
```bash
(env) jonkiddy@local hugging-chat-simple-cli % python main.py
[[ Welcome to HugChat. Let's talk! ]]
'q' or 'quit' to exit
'c' or 'change' to change conversation
'n' or 'new' to start a new conversation
> 
```

## Sample Prompts:

### Simple "Hello!":
``` bash
(env) jonkiddy@local hugging-chat-simple-cli % python main.py
[[ Welcome to HugChat. Let's talk! ]]
'q' or 'quit' to exit
'c' or 'change' to change conversation
'n' or 'new' to start a new conversation
>  Hello!
Hello! How can I assist you today?
>
```

### More elaborate request:
``` bash
(env) jonkiddy@local hugging-chat-simple-cli % python main.py
[[ Welcome to HugChat. Let's talk! ]]
'q' or 'quit' to exit
'c' or 'change' to change conversation
'n' or 'new' to start a new conversation
> Hi, I am looking for inspiration on how to make my bedroom more comfy, would you have some ideas?
Of course! Making your bedroom comfortable and cozy can be a great project. Some things that might help include:

1. Choosing comfortable and inviting furniture such as soft chairs or a reading nook.
2. Adding warm lighting sources like lamps or dim overhead lights.
3. Using throw blankets and pillows in cozy materials like fleece or flannel.
4. Creating a peaceful and relaxing atmosphere by choosing calm colors and natural materials like wood or stone.
5. Including elements that bring joy to you personally, like artwork, photos, or souvenirs.
6. Keeping the space clean and organized so that it feels serene rather than cluttered.
Does this give you some good starting points? Let me know if there's anything else specific I can help with!
>
```