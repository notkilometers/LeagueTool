from pynput import keyboard
from pynput.mouse import Button, Controller

mouse = Controller()
t = (0,0)
def on_press(key):
    t = mouse.position
    #try:
    #    print('key {0} was pressed'.format(key.char))
    #except AttributeError:
    #    print('special key {0} pressed'.format(key))

def mvmt(x,y):
    mouse.position = (x,y)
    mouse.press(Button.right)
    mouse.release(Button.right)

def org(t):
    mouse.position = t
    
def on_release(key):
    t = mouse.position
    print (t)
    #print('{0} released'.format(key))
    
    if key == keyboard.KeyCode.from_char("4"):
        mouse.press(Button.left)
        mouse.release(Button.left)
    if key == keyboard.KeyCode.from_char("u"):
        mvmt(730,400)
        org(t)
    if key == keyboard.KeyCode.from_char("i"):
        mvmt(1010, 400)
        org(t)
    if key == keyboard.KeyCode.from_char("h"):
        mvmt(560, 540)
        org(t)
    if key == keyboard.KeyCode.from_char("j"):
        mvmt(960, 540)
        org(t)
    if key == keyboard.KeyCode.from_char("k"):
        mvmt(1360, 540)
        org(t)
    if key == keyboard.KeyCode.from_char("n"):
        mvmt(700,880)
        org(t)
    if key == keyboard.KeyCode.from_char("m"):
        mvmt(1220,880)
        org(t)

       
        
    if key == keyboard.Key.esc:
        # Stop listener
        return False


ln = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
ln.start()
mouse.position = (0,0)
