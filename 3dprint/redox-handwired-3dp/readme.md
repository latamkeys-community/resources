# redox-handwired-3dp by Brockar
## Contenido / Content
- [redox-handwired-3dp by Brockar](#redox-handwired-3dp-by-brockar)
  - [Contenido / Content](#contenido--content)
- [ES](#es)
  - [Materiales](#materiales)
  - [Pasos a seguir](#pasos-a-seguir)
  - [QMK](#qmk)
    - [Instalación](#instalación)
    - [Configuración](#configuración)
    - [Cargar firmware](#cargar-firmware)
  - [VIAL](#vial)
- [EN](#en)
  - [Materials](#materials)
  - [Steps to follow](#steps-to-follow)
  - [QMK](#qmk-1)
    - [Installation](#installation)
    - [Configuration](#configuration)
    - [Load firmware](#load-firmware)
  - [VIAL](#vial-1)
- [Referencias / References](#referencias--references)

![my-redox](https://i.imgur.com/6SMD83O.jpeg)
![other-redox](https://i.imgur.com/jXOqhLl.jpeg)
# ES
Hice un Redox Handwired siguiendo todas las referencias que encontré pero se me hizo coomo que estaba todo muy disperso o poco explicado, así que voy a explicar cómo hacerlo.
 
## Materiales
* 70x: Switches compatibles con Cherry.  
* 70x: Diodos (1N4148).  
* 70x: Keycaps compatible con Cherry.  
  * 10x (8x para layout 1u): 1.25u keycaps.  
  * 6x: 1.5u keycaps.  
  * 54x (56x para layout 1u): 1u keycaps.  
* 14x: tornillos M3 8mm.  
* 2x: 3.5 mm plug de 3 polos.  
* 2x: Arduino pro micros.  
* Cable.
* Estaño.
* Soldadora.

## Pasos a seguir
1. Imprimir plates. Se puede elegir que sean todas 1u, yo imprimí ese. [link](https://www.thingiverse.com/thing:2704567/files).  
2. Poner switches con el "huequito" mirando para abajo.
3. Imprimir el case mientras haces el resto.
4. Soldar segun muestra el [Buildlog](https://i.imgur.com/WoZ36il.jpeg). Conectar todo excepto la conexión entre los dos arduinos. Eso se conecta en [serial](https://github.com/qmk/qmk_firmware/blob/master/docs/feature_split_keyboard.md). [Imagen](https://user-images.githubusercontent.com/2170248/92296490-2d15cb00-ef70-11ea-801f-5ace313013e6.JPG).  
5. Poner el plate con el case.   

Ahora solo queda configurar [QMK](#qmk), compilarlo y ponerlo el arduino. 

Si queres usar VIAL, podes hacerlo salteando este paso y siguiendo los pasos de [VIAL](#vial).

## QMK 
### Instalación  
[Docs instalación](https://docs.qmk.fm/#/newbs_getting_started).  
1. Instalar [VS Code](https://code.visualstudio.com/download).  
2. Instalar [QMK MSYS](https://msys.qmk.fm/).
3. Abrir QMK MSYS. Correr `qmk setup`. Te va a pedir clonar el repositorio, lo clonas.
4. Te pregunta si queres cambiar el directorio principal de QMK, escribis `y` + enter.
5. Te pregunta si queres instalar las dependencias, escribis `y` + enter.  

### Configuración 
6. En `qmk_firmware/keyboards/redox` va a estar la configuración de tu teclado.
7. Escribir lo siguiente en la consola de QMK MSYS.
   1. `qmk config user.keyboard=redox/rev1`
   2. `qmk config user.keymap=default`
8. En `qmk-firmware/keyboards/redox/rev1/config.h` agregar `#define SPLIT_HAND_PIN D2` comentar la linea 29  `//#define MATRIX_COL_PINS { F5, F6, F7, B1, B3, B2, B6 }`  
y descomentar la 30 `#define MATRIX_COL_PINS { B6, B2, B3, B1, F7, F6, F5}`
9.  Modificar `qmk_firmware/keyboards/redox/keymaps/default/keymap.c` a gusto, te podes guiar con la [documentación](https://docs.qmk.fm/#/keycodes).   
10.   Escribir `qmk compile -kb redox -km default` + enter, en QMK MSYS.

### Cargar firmware
Instalar [QMK Toolbox](https://github.com/qmk/qmk_toolbox/releases/tag/0.2.2). Si te pide instalar drivers, instalalos. 

En ``qmk_firmware/`` va a quedar un archivo llamado ``redox_rev1_default.hex`` o algo parecido, lo importante es que sea un archivo .hex. 

* Abrimos QMK Toolbox, 
* seleccionamos el archivo, 
* seleccionamos atmega32u4, 
* marcamos Auto-Flash, 
* conectamos el teclado y hacemos puente con algo que sea conductivo (el estaño por ejemplo) entre estos dos [pines](https://www.shellhacks.com/wp-content/uploads/arduino_pro_micro_reset_pins.jpg).  
Te tendria que aparecer un texto amarillo en el QMK Toolbox, cuando te aparezca el segundo tecto amarillo que dice algo como: ``Atmel DFU dive disconected (libusb0): ...``  

LISTO! Ya tenes tu teclado. Cuando quieras cambiar la configuración del QMK, lo cambias en `qmk_firmware/keyboards/redox/keymaps/default/keymap.c`, lo volves a compilar (`10. `) y lo volves a [Cargar](#cargar-firmware).  

## VIAL
Hacemos el mismo proceso que en [QMK](#QMK), pero en lugar de utilizar `redox/keymaps/default` utilizamos `redox/keymaps/vial`, el cual debemos copiar y desde este repositorio `vial-qmk/keyboards/`.
Yo lo que hago es compilarlo tal cual esta y después modificar el keymap en vial directamente.  
Para hacer el paso 10, hacemos `qmk compile -kb redox -km vial`. buscamos `redox_rev1_base_vial` y subimos ese archivo con [QMK Toolbox](#cargar-firmware).  

Descargar la app para modificar el teclado en [get vial](https://get.vial.today/download/).

---
# EN
I made a Redox Handwired following all the references I found but it seemed to me that everything was too scattered or poorly explained, so I will explain how to do it.
 
## Materials
* 70x: Cherry compatible switches.  
* 70x: Diodes (1N4148).  
* 70x: Cherry compatible keycaps.  
  * 10x (8x for layout 1u): 1.25u keycaps.  
  * 6x: 1.5u keycaps.  
  * 54x (56x for 1u layout): 1u keycaps.  
* 14x: M3 8mm screws.  
* 2x: 3.5 mm 3-pin plug.  
* 2x: Arduino pro micros.  
* Cable.
* Tin.
* Tin welder.

## Steps to follow
1. Print plates. You can choose that they are all 1u, I printed that one. [link](https://www.thingiverse.com/thing:2704567/files).  
2. Put switches with the "hole" facing down.
3. Print the case while you do the rest.
4. Solder as shown in the [Buildlog](https://i.imgur.com/WoZ36il.jpeg). Connect everything except the connection between the two arduinos. That is connected in [serial](https://github.com/qmk/qmk_firmware/blob/master/docs/feature_split_keyboard.md). [Imagen](https://user-images.githubusercontent.com/2170248/92296490-2d15cb00-ef70-11ea-801f-5ace313013e6.JPG).  
5. Put the plate with the case.   

Now just configure [QMK](#qmk), compile it and put it on the arduino. 

If you want to use VIAL, you can do it by skipping this step and following the steps in [VIAL](#vial).

## QMK 
### Installation  
[Docs installation](https://docs.qmk.fm/#/newbs_getting_started).  
1. Install [VS Code](https://code.visualstudio.com/download).  
2. Install [QMK MSYS](https://msys.qmk.fm/).
3. Open QMK MSYS. Run `qmk setup`. It will ask you to clone the repository, clone it.
4. It asks if you want to change the QMK home directory, type `y` + enter.
5. It will ask you if you want to install the dependencies, type `y` + enter.  

### Configuration 
6. In `qmk_firmware/keyboards/redox` will be your keyboard configuration.
7. Type the following in the QMK MSYS console.
   1. `qmk config user.keyboard=redox/rev1` 2.
   2. `qmk config user.keymap=default`.
8. In `qmk-firmware/keyboards/redox/rev1/config.h` add `#define SPLIT_HAND_PIN D2` comment line 29 `//#define MATRIX_COL_PINS { F5, F6, F7, B1, B3, B2, B6 }` and uncomment line 30 `/#define MATRIX_COL_PINS { F5, F6, F7, B1, B3, B2, B6 }`.  
and uncomment line 30 `/#define MATRIX_COL_PINS { B6, B2, B3, B1, F7, F6, F5}`.
9.  Modify `qmk_firmware/keyboards/redox/keymaps/default/keymap.c` as you like, you can guide yourself with the [documentation](https://docs.qmk.fm/#/keycodes).   
10.   Type `qmk compile -kb redox -km default` + enter, in QMK MSYS.

### Load firmware
Install [QMK Toolbox](https://github.com/qmk/qmk_toolbox/releases/tag/0.2.2). If you are prompted to install drivers, install them. 

In ``qmk_firmware/`` there will be a file called ``redox_rev1_default.hex`` or something similar, the important thing is that it is a .hex file. 

* Open QMK Toolbox, 
* select the file, 
* select atmega32u4, 
* check Auto-Flash, 
* connect the keyboard and make a bridge with something conductive (tin for example) between these two [pins](https://www.shellhacks.com/wp-content/uploads/arduino_pro_micro_reset_pins.jpg).  
You should get a yellow text in the QMK Toolbox, when you get the second yellow text that says something like: ``Atmel DFU dive disconected (libusb0): ...``.  

DONE! You have your keyboard. When you want to change the QMK configuration, change it in `qmk_firmware/keyboards/redox/keymaps/default/keymap.c`, recompile it (`10. `) and go back to [Load](#load-firmware).  

## VIAL
We do the same process as in [QMK](#QMK), but instead of using `redox/keymaps/default` we use `redox/keymaps/vial`, which we must copy and from this repository `vial-qmk/keyboards/`.
What I do is to compile it as it is and then modify the keymap in vial directly.  
To do step 10, we do `qmk compile -kb redox -km vial`. We look for `redox_rev1_base_vial` and upload that file with [QMK Toolbox](#load-firmware).  

Download the app to modify the keyboard in [get vial](https://get.vial.today/download/).

# Referencias / References
Proyecto HW: [@MattDB](https://www.thingiverse.com/thing:2704567).  
Proyecto Original: [@mattdibi](https://github.com/mattdibi/redox-keyboard).  
Biuldlog: [IDK](https://imgur.com/a/phr2z).  
QMK Docs: [Docs](https://docs.qmk.fm/#/).  
Video (ESP): [JC Nerd](https://www.youtube.com/watch?v=mz8WG5e--jA&t=12s). 