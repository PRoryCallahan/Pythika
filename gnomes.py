import random
from guizero import App, Text, PushButton

def gnome_me():
    gnome = random.choice(list_a)
    return gnome

def new_gnome():
    new_gnome = gnome_me()
    message.value = new_gnome

list_a = []

with open("gnomes.csv", "r") as f:
    for line in f:
        words = line.split('//')
        list_a.append(words[0])
    gnome_me()

app = App("Gnome Generator")
message = Text(app, gnome_me() )
buttom = PushButton(app, new_gnome, text="Know thyself")
app.diplay()
