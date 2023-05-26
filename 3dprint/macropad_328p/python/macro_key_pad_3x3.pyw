#! python3
import pyautogui, sys, time, serial

port = 'COM3'   #Windows COMX, u can look it in Arduino IDE
baud = 9600

NanoSerial = serial.Serial(port, baud)
time.sleep(1)

print("MacroKeyPad:", port, baud)

while 1:
    data = str(NanoSerial.readline())[2]
    if data == '1':
        pyautogui.press('prevtrack')    #Previous track
    elif data == '2':
        pyautogui.press('playpause')    #Play/Pause
    elif data == '3':
        pyautogui.press('nexttrack')    #Next track
    elif data == '4':
        pyautogui.press('volumedown')   #Turn volume down
    elif data == '5':
        pyautogui.press('volumemute')   #Turn volume on/off
    elif data == '6':
        pyautogui.press('volumeup')     #Turn volume up
    elif data == '7':
        pyautogui.hotkey('ctrl', 'b', '"')
    elif data == '8':
        pyautogui.hotkey('ctrl', 'b', '%')
    elif data == '9':
        pyautogui.hotkey('ctrl', 'b', 'c')