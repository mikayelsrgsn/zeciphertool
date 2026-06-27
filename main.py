import json
import ast
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
keysJson = os.path.join(script_dir, "keys.json")
cipherKey = {}
print("Ze Cipher tool.")
print("Use 'help' to get all commands.")
print("There won't be any support for this project.")
print("_______________________________")

def splitString(text, index):
    return [text[i:i+index] for i in range(0, len(text), index)]

def loadKey(keyName):
    global cipherKey
    with open(keysJson, "r") as f:
        data = json.load(f)
        if keyName not in data:
            print("Error: '"+keyName+"' not found in keys.json.")
            print("_______________________________")
        else:
            cipherKey = data[keyName]

def encode(text):
    global cipherKey
    if not cipherKey:
        print("Error: cipherKey not chosen.")
        print("_______________________________")

        return
    cipher = cipherKey["cipher"]
    splitText = splitString(text, 1)

    encodedText = ""

    for letter in splitText:
        if letter not in cipher:
            print("Error: key doesn't support character: '" +letter+ "'.")
            print("_______________________________")
            return

        encodedText = encodedText + cipher[letter]
    
    print("Encoded text: " + encodedText)
    print("_______________________________")

def decode(text):
    global cipherKey
    if not cipherKey:
        print("Error: cipherKey not chosen.")
        print("_______________________________")
        return
    reverse_cipher = {value: key for key, value in cipherKey["cipher"].items()}
    splitText = splitString(text, cipherKey["index"])

    decodedText = ""

    for letter in splitText:
        if letter not in reverse_cipher:
            print("Error: key doesn't support character: '"+letter+"'.")
            print("_______________________________")
            return
        decodedText = decodedText + reverse_cipher[letter]
    
    print("Decoded text: " + decodedText)
    print("_______________________________")

def addKey(text, name):
    try:
        key = ast.literal_eval(text)
    except Exception:
        print("Error: wrong key format, the addkey command can only use: Booleans, None, Strings, Sets, Tuples, Lists, and Dictionaries.")
        print("Use the command 'help-customkeys' for help with customkeys.")
        print("_______________________________")


    if "index" not in key:
        print("Error: incorrect key format, 'index' not found in key.")
        print("Use the command 'help-customkeys' for help with customkeys.")
        print("_______________________________")
        return
    if "cipher" not in key:
        print("Error: incorrect key format, 'cipher' not found in key.")
        print("Use the command 'help-customkeys' for help with customkeys.")
        print("_______________________________")
        return

    keyData = {name: key}

    with open(keysJson, "r") as f:
        jsondata = json.load(f)
        
    jsondata.update(keyData)
        
    with open(keysJson, "w") as f:
        json.dump(jsondata, f)
        print("Success: '"+name+"' added to 'keys.json'.")
        print("_______________________________")

while True:
    cmd = input("Command: ")

    if cmd == "help":
        print("Encode text: 'encode'.")
        print("Decode text: 'decode'.")
        print("Choose key: 'setkey'.")
        print("Add custom cipher key: 'addkey'.")
        print("Special help for custom cipher keys: 'help-customkeys'.")
        print("_______________________________")

    elif cmd == "encode":
        text = input("Text to encode: ")
        encode(text)

    elif cmd == "decode":
        text = input("Text to decode: ")
        decode(text)
    
    elif cmd == "setkey":
        key = input("Set key: ")
        loadKey(key)

    elif cmd == "addkey":
        keyName = input("Key Name: ")
        key = input("Paste your key: ")
        addKey(key, keyName)

    elif cmd == "help-customkeys":
        print("CustomKey manual")
        print('   Example key structure: {"key-name": {"index":1,"cipher":{"letter": "encoded_letter"}}}')
        print('   "key-name" is the name of the custom cipher key.')
        print('   "index" is the amount of encoded letters for each regular letter. Example: "A": "aaa" then index is 3.')
        print('   "letter" is the regular alphabet letter such as "A" or "B".')
        print('   "encoded_letter" is the encoded alphabet letter.')
        print("Visit the 'keys.json' file for better understanding.")
        print("_______________________________")

    else:
        print("Error: command '"+cmd+"' not recognized. Use 'help' to get all commands.")
        print("_______________________________")
