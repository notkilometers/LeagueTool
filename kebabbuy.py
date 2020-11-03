from pynput import keyboard
from pynput.mouse import Button, Controller
import time

mouse = Controller()
t = (0,0)
a = (688,298)
b = (755, 970)
c = (641,941)
d = (538, 969)

def on_press(key):
    t = mouse.position
    
def mvmt(x,y):
    mouse.position = (x,y)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(1)
    
def org(t):
    mouse.position = t
    
def on_release(key):
    t = mouse.position
    print (t)
    #print('{0} released'.format(key))

    if key == keyboard.KeyCode.from_char("z"):
        mvmt(t[0],t[1])
        mvmt(b[0],b[1])
        mvmt(c[0],c[1])
        mvmt(d[0],d[1])
        org(t)
        
    if key == keyboard.Key.esc:
        # Stop listener
        return False


ln = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
ln.start()
mouse.position = (0,0)
