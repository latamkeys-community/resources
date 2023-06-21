# Macropad Arduino Nano (Atmega 328p)
## Contenido / Content
- [Macropad Arduino Nano (Atmega 328p)](#macropad-arduino-nano-atmega-328p)
  - [Contenido / Content](#contenido--content)
- [ES](#es)
  - [Requisitos](#requisitos)
  - [Arduino](#arduino)
    - [Librería de arduino](#librería-de-arduino)
    - [Código](#código)
  - [Python](#python)
    - [Actualizando pip](#actualizando-pip)
    - [pyserial](#pyserial)
    - [pyautogui](#pyautogui)
  - [Esquema de conexión](#esquema-de-conexión)
  - [Case](#case)
- [EN](#en)
  - [Requirements](#requirements)
  - [Arduino](#arduino-1)
    - [Arduino library](#arduino-library)
    - [Code](#code)
  - [Python](#python-1)
    - [Updating pip](#updating-pip)
    - [pyserial](#pyserial-1)
    - [pyautogui](#pyautogui-1)
  - [Wiring diagram](#wiring-diagram)
  - [Case](#case-1)
- [Referencias / References](#referencias--references)
# ES
Normalmente se hacen teclados o macropads con Arduino Micro Pro. 
Sin embargo, puede que no tengas a tu disposición uno de estos o te hayas equivocado al comprar (como yo).
El arduino nano no tiene HID, es decir que la PC no lo puede recnocer como teclado.

En arduino, cada vez que presionemos una tecla enviará un carácter a través de Serial.  
Con python debemos capturar qué carácter fue y que acción de teclado se ejecutará.  
Esto para cada tecla del Keypad.
## Requisitos
* [IDE de arduino](https://www.arduino.cc/en/Main/Software)
* [Python 3.x](https://www.python.org/)

## Arduino
### Librería de arduino
A través del administrador de librerías de Arduino debemos instalar **Keypad** de los autores **Mark Stanley** y **Alexander Brevig**.
![libreria](https://i.imgur.com/13DPav0.png)

### Código
En ./arduino hay dos códigos, uno para un keypad de 3x3 y otro para 4x4, tomando esos códigos como ejemplo podrías modificarlos para hacer de otra matriz.

## Python
Después de instalar python, es necesario instalar unas dependencias para que funcione el código.
### Actualizando pip
**Windows:** Ejecutar Power Shell / CMD como administrador
```shell
python -m pip install --upgrade pip
```
### pyserial
Esta librería nos ayudará con la comunicación entre el arduino y python a través del puerto serial.
```shell
python -m pip install pyserial
```
### pyautogui
Con pyautogui seremos capaces de "presionar" teclas a través de código.
```shell
python -m pip install pyautogui
```
  
  
En macro_key_pad_XxX.pyw modificar el COMx, podes ver qué numero va en ArduinoIDE.

También podés modificar qué hace cada tecla en macro_key_pad_xXx.pyw, toda la documentación está en su [página](https://pyautogui.readthedocs.io/en/latest/keyboard.html).

Correr **macro_key_pad_xXx.pyw**.

## Esquema de conexión

Generalmente estos teclados suelen tener pines que representan las filas y las columnas de la matriz de pulsadores. Conectarás cada pin del teclado a un pin **digital** del arduino.
![esquema](https://i.imgur.com/ZAS0U6P.jpeg)
Se haría lo mismo pero con dos pines menos en una matriz de 3x3.

## Case
Podés usar el case que quieras, te dejo dos cases que funcionan con arduino nano.  
* `./case/XxX`
* Hicimos uno de 3x3 y uno de 4x4, cada uno tiene un case inclinado 5 grados y otro recto.

Si se quiere modificar algo, está el archivo de Fusion 360 en `./case/XxX/macropad_XxX.f3d`.   
Hecho por: Mante#7952 (discord).
# EN
Keyboards or macropads are usually made with Arduino Micro Pro. 
However, you may not have one of these at your disposal or you may have made a mistake when buying (like me).
The arduino nano does not have HID, meaning that the PC cannot recognize it as a keyboard.

In arduino, every time we press a key it will send a character through Serial.  
With python we must capture what character it was and what keyboard action will be executed.  
This for each key on the Keypad.
## Requirements
* [arduino IDE](https://www.arduino.cc/en/Main/Software)
* [Python 3.x](https://www.python.org/)

## Arduino
### Arduino library
Through the Arduino library manager we must install **Keypad** by authors **Mark Stanley** and **Alexander Brevig**.
![library](https://i.imgur.com/13DPav0.png)

### Code
In ./arduino there are two codes, one for a 3x3 keypad and one for 4x4, taking those codes as an example you could modify them to make another matrix.

## Python
After installing python, you need to install some dependencies for the code to work.
### Updating pip
**Windows:** Run Power Shell / CMD as administrator
```shell
python -m pip install --upgrade pip
```
### pyserial
This library will help us with the communication between the arduino and python through the serial port.
```shell
python -m pip install pyserial
```
### pyautogui
With pyautogui we will be able to "press" keys through code.
```shell
python -m pip install pyautogui
```
In macro_key_pad_xXx.pyw modify the COMx, you can see which number goes in ArduinoIDE.  

You can also modify what each key does in MacroKeyPadxXx.pyw, all the documentation is in its [page](https://pyautogui.readthedocs.io/en/latest/keyboard.html).  

Run **macro_key_pad_xXx.pyw**.
## Wiring diagram

Generally these keyboards usually have pins that represent the rows and columns of the pushbutton matrix. You will connect each pin on the keypad to a **digital** pin on the arduino.
![schematic](https://i.imgur.com/ZAS0U6P.jpeg)
You would do the same but with two less pins in a 3x3 matrix.  
  
## Case
You can use any case you want, here are two cases that work with arduino nano.  
* case/XxX`.
* We made a 3x3 and a 4x4, each one has a case inclined 5 degrees and another one straight.

If you want to modify something, there is the Fusion 360 file in `./case/XxX/macropad_XxX.f3d`.
  
# Referencias / References
Código principal: [@crixodia](https://www.twitter.com/crixodia), [código](https://github.com/crixodia/arduino-nano-macro-keypad/tree/master).  
Video relacionado: [@Hazz Techno Dance](https://www.youtube.com/@hazztechnodance8190), [Video](https://www.youtube.com/watch?v=JGrRwc5wo2s).