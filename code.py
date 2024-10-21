
import board 
import digitalio 
import time
import usb_hid 
from adafruit_hid.keyboard import Keyboard 
from adafruit_hid.keycode import Keycode 
from adafruit_hid.consumer_control import ConsumerControl 
from adafruit_hid.consumer_control_code import ConsumerControlCode 

# Initialisation du clavier HID
keyboard = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)


# Configuration du pin 28 en tant qu'entree (sw1)
sw1 = digitalio.DigitalInOut(board.GP28)
sw1.direction = digitalio.Direction.INPUT
sw1.pull = digitalio.Pull.DOWN  # Activer la resistance de pull-down interne pour eviter les flottements

sw2 = digitalio.DigitalInOut(board.GP27)
sw2.direction = digitalio.Direction.INPUT
sw2.pull = digitalio.Pull.DOWN

sw3 = digitalio.DigitalInOut(board.GP26)
sw3.direction = digitalio.Direction.INPUT
sw3.pull = digitalio.Pull.DOWN

sw4 = digitalio.DigitalInOut(board.GP22)
sw4.direction = digitalio.Direction.INPUT
sw4.pull = digitalio.Pull.DOWN

sw5 = digitalio.DigitalInOut(board.GP21)
sw5.direction = digitalio.Direction.INPUT
sw5.pull = digitalio.Pull.DOWN


sw6 = digitalio.DigitalInOut(board.GP20)
sw6.direction = digitalio.Direction.INPUT
sw6.pull = digitalio.Pull.DOWN

sw7 = digitalio.DigitalInOut(board.GP19)
sw7.direction = digitalio.Direction.INPUT
sw7.pull = digitalio.Pull.DOWN

sw8 = digitalio.DigitalInOut(board.GP18)
sw8.direction = digitalio.Direction.INPUT
sw8.pull = digitalio.Pull.DOWN

sw9 = digitalio.DigitalInOut(board.GP17)
sw9.direction = digitalio.Direction.INPUT
sw9.pull = digitalio.Pull.DOWN

while True:
    # Si sw1 detecte un signal haut (3.3V), envoyer Ctrl+Alt+Suppr
    if sw1.value:
        keyboard.press(Keycode.CONTROL, Keycode.ALT, Keycode.DELETE)
        keyboard.release_all()  # Relacher toutes les touches apres la combinaison
        time.sleep(1)  # Attendre une seconde avant de reagir a nouveau
        
    
    if sw2.value:
        keyboard.press(Keycode.WINDOWS, Keycode.SHIFT, Keycode.S) # Screenshot
        keyboard.release_all()  
        time.sleep(1)
    
    if sw3.value:
        keyboard.press(Keycode.CONTROL, Keycode.SHIFT, Keycode.ESCAPE) # task manager
        keyboard.release_all()  
        time.sleep(1)
    if sw4.value:
        keyboard.press(Keycode.CONTROL, Keycode.C) # copy
        keyboard.release_all()  
        time.sleep(1)

    if sw5.value:
        keyboard.press(Keycode.CONTROL, Keycode.V) # past
        keyboard.release_all()  
        time.sleep(1)

    if sw6.value:
        keyboard.press(Keycode.CONTROL, Keycode.W) # back
        keyboard.release_all()  
        time.sleep(1)

    if sw7.value:
        cc.send(ConsumerControlCode.SCAN_PREVIOUS_TRACK) # Go back to next track  
        time.sleep(1)
    
    if sw8.value:
        cc.send(ConsumerControlCode.SCAN_NEXT_TRACK) # Go back to previous track  
        time.sleep(1)
    
    
    if sw9.value:
        cc.send(ConsumerControlCode.PLAY_PAUSE) # pause 
        time.sleep(1)   

    
     
    
    
    
    
    time.sleep(0.1)  # Petite pause pour eviter une detection trop rapide

