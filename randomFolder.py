import os, random
import webbrowser
basedir = "C:\\"

file = random.choice([x for x in os.listdir(basedir) if os.path.isdir(os.path.join(basedir, x))])

print("폴더를 엽니다. {}...".format(file))
webbrowser.open(os.path.join(basedir, file))
