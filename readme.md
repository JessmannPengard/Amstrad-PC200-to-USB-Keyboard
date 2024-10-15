# Conversión de Teclado Amstrad Sinclair PC200/PPC 640/512 a USB con Raspberry Pi Pico

[Versión en Español](#versi%C3%B3n-en-espa%C3%B1ol) | [English Version](#english-version)

---

## Versión en Español

Este proyecto tiene como objetivo convertir un teclado de un Amstrad Sinclair PC200 o de un Amstrad PPC 640/512 en un dispositivo USB funcional utilizando una Raspberry Pi Pico. Esto se logra a través del uso de CircuitPython y la librería KMK, que permite la creación de firmware personalizable para teclados.

### Requisitos previos

#### Hardware:
- Un teclado de un Amstrad Sinclair PC200 o Amstrad PPC 640/512.
- Una Raspberry Pi Pico.
- Cables o conectores para realizar la conexión entre la Pico y la matriz del teclado.

#### Software:
- **CircuitPython**: un sistema operativo ligero diseñado para microcontroladores como la Raspberry Pi Pico.
- **KMK Firmware**: una librería de Python para la creación de teclados personalizados.
- **Thonny IDE (opcional)**: un entorno de desarrollo fácil de usar para trabajar con CircuitPython.

### Guía de instalación

#### Paso 1: Instalación de CircuitPython en la Raspberry Pi Pico

##### Descargar CircuitPython:
Descarga la última versión de CircuitPython compatible con la Raspberry Pi Pico desde el siguiente enlace:  
[CircuitPython para Raspberry Pi Pico](https://circuitpython.org/board/raspberry_pi_pico/)

##### Flashear CircuitPython:
1. Con la Raspberry Pi Pico desconectada, mantén presionado el botón BOOTSEL en la placa y conéctala al puerto USB de tu computadora. Esto la pondrá en modo almacenamiento masivo.
2. Una vez que la Raspberry Pi Pico esté en modo almacenamiento, copia el archivo `adafruit-circuitpython-raspberry_pi_pico-es-9.1.3.uf2` a la raíz del dispositivo. La Pico se reiniciará automáticamente y se montará como una unidad de almacenamiento con el nombre `CIRCUITPY`.

#### Paso 2: Configuración del entorno

##### Copiar la carpeta KMK:
Descarga la librería KMK desde el siguiente enlace:  
[KMK Firmware](https://github.com/KMKfw/kmk_firmware)  
Luego, copia la carpeta `kmk` a la raíz de la unidad `CIRCUITPY`.

##### Copia de archivos de configuración:
Copia los siguientes archivos al directorio raíz de `CIRCUITPY`:
- `boot.py`: Este archivo se asegura de que la Raspberry Pi Pico no se monte como almacenamiento masivo al encenderse.
- `code.py`: Contiene la lógica principal que convierte las entradas del teclado en señales USB.

##### Reiniciar la Raspberry Pi Pico:
Desconecta y vuelve a conectar la Raspberry Pi Pico. En este punto, el teclado debería estar funcional y listo para ser utilizado como dispositivo USB.

#### Paso 3: Uso de la herramienta `scanner.py`

El archivo `scanner.py` es una utilidad diseñada para ayudar a identificar las conexiones de la matriz del teclado. Al ejecutar este script, puedes presionar las teclas del teclado Amstrad y obtener la fila y columna correspondiente, lo cual es útil para mapear correctamente las teclas en KMK.

##### Ejecutar `scanner.py`:
Usa Thonny IDE para ejecutar `scanner.py` en la Raspberry Pi Pico. Puedes descargar Thonny desde el siguiente enlace:  
[Descargar Thonny](https://thonny.org/)

##### Mapeo de teclas:
A medida que presiones las teclas, el script te mostrará la fila y columna a las que pertenecen junto a los GPIO de la Pi Pico correspondientes. Utiliza esta información para personalizar tu archivo `main.py` y crear el mapeo correcto del teclado.

### Conexiones de hardware

La siguiente tabla describe cómo deben conectarse los pines del cable Flex del teclado al GPIO de la Raspberry Pi Pico. He utilizado dos conectores FPC de paso 2,54mm de 13 pines para los cables Flex:

| Pin del Cable Flex    | Conexión a GPIO en Raspberry Pi Pico      |
|-----------------------|-------------------------------------------|
| 1 (Cable Flex Superior)| GPIO13                                   |
| 2                     | GPIO12                                   |
| 3                     | GPIO14                                   |
| 4                     | GPIO11                                   |
| 5                     | GPIO10                                   |
| 6                     | GPIO15                                   |
| 7                     | GPIO9                                    |
| 8                     | GPIO16                                   |
| 9                     | GPIO18                                   |
| 10                    | GPIO17                                   |
| 11                    | GPIO19                                   |
| 12                    | GPIO20                                   |
| 13                    | GPIO21                                   |
| 14 (Cable Flex Inferior)| Resistencia 270 Ohm -> GPIO26            |
| 15                    | GPIO0                                    |
| 16                    | GPIO1                                    |
| 17                    | GPIO2                                    |
| 18                    | GPIO3                                    |
| 19                    | GPIO4                                    |
| 20                    | GPIO7                                    |
| 21                    | GPIO6                                    |
| 22                    | GPIO5                                    |
| 23                    | VBUS                                     |
| 24                    | Resistencia 270 Ohm -> GPIO28             |
| 25                    | Resistencia 270 Ohm -> GPIO27             |
| 26                    | GND                                      |

### Recursos adicionales
- [CircuitPython: Guía de instalación y uso de CircuitPython](https://circuitpython.org/)
- [KMK Firmware: Documentación oficial de KMK](https://github.com/KMKfw/kmk_firmware)
- [Thonny IDE: Descargar Thonny](https://thonny.org/)

### Problemas comunes y soluciones

#### Reflasheo de la Raspberry Pi Pico
En caso de que necesites limpiar la memoria flash de la Raspberry Pi Pico por errores o mal funcionamiento:

1. Utiliza el archivo `flash_nuke.uf2`.
2. Con la Pico en modo almacenamiento masivo, copia el archivo a la raíz para limpiar la memoria flash completamente.
3. Repite el proceso de instalación de CircuitPython desde el Paso 1.

---

## English Version

### Amstrad Sinclair PC200/PPC 640/512 Keyboard to USB Conversion with Raspberry Pi Pico

This project aims to convert a keyboard from an Amstrad Sinclair PC200 or an Amstrad PPC 640/512 into a functional USB device using a Raspberry Pi Pico. This is achieved using CircuitPython and the KMK library, which allows the creation of customizable keyboard firmware.

### Prerequisites

#### Hardware:
- A keyboard from an Amstrad Sinclair PC200 or Amstrad PPC 640/512.
- A Raspberry Pi Pico.
- Wires or connectors to connect the Pico to the keyboard matrix.

#### Software:
- **CircuitPython**: a lightweight operating system designed for microcontrollers like the Raspberry Pi Pico.
- **KMK Firmware**: a Python library for creating custom keyboards.
- **Thonny IDE (optional)**: a user-friendly development environment for working with CircuitPython.

### Installation Guide

#### Step 1: Install CircuitPython on the Raspberry Pi Pico

##### Download CircuitPython:
Download the latest version of CircuitPython compatible with the Raspberry Pi Pico from the following link:  
[CircuitPython for Raspberry Pi Pico](https://circuitpython.org/board/raspberry_pi_pico/)

##### Flash CircuitPython:
1. With the Raspberry Pi Pico disconnected, press and hold the BOOTSEL button on the board and connect it to your computer’s USB port. This will put it in mass storage mode.
2. Once the Raspberry Pi Pico is in mass storage mode, copy the `adafruit-circuitpython-raspberry_pi_pico-en-9.1.3.uf2` file to the device’s root. The Pico will automatically reboot and mount as a storage device named `CIRCUITPY`.

#### Step 2: Setup the Environment

##### Copy the KMK folder:
Download the KMK library from the following link:  
[KMK Firmware](https://github.com/KMKfw/kmk_firmware)  
Then copy the `kmk` folder to the root of the `CIRCUITPY` drive.

##### Copy configuration files:
Copy the following files to the root directory of `CIRCUITPY`:
- `boot.py`: This file ensures that the Raspberry Pi Pico does not mount as mass storage on boot.
- `code.py`: Contains the main logic that converts the keyboard inputs into USB signals.

##### Reboot the Raspberry Pi Pico:
Disconnect and reconnect the Raspberry Pi Pico. At this point, the keyboard should be functional and ready to use as a USB device.

#### Step 3: Use the `scanner.py` Tool

The `scanner.py` file is a utility designed to help identify the connections of the keyboard matrix. When running this script, you can press keys on the Amstrad keyboard and obtain the corresponding row and column, which is useful for correctly mapping the keys in KMK.

##### Run `scanner.py`:
Use Thonny IDE to run `scanner.py` on the Raspberry Pi Pico. You can download Thonny from the following link:  
[Download Thonny](https://thonny.org/)

##### Key Mapping:
As you press keys, the script will show the row and column they belong to along with the corresponding Raspberry Pi Pico GPIO. Use this information to customize your `main.py` file and create the correct key mapping for the keyboard.

### Hardware Connections

The following table describes how the pins of the Flex cable from the keyboard should be connected to the GPIO of the Raspberry Pi Pico. I have used two 2.54mm pitch 13-pin FPC connectors for the Flex cables:

| Flex Cable Pin        | Connection to Raspberry Pi Pico GPIO      |
|-----------------------|-------------------------------------------|
| 1 (Upper Flex Cable)   | GPIO13                                   |
| 2                     | GPIO12                                   |
| 3                     | GPIO14                                   |
| 4                     | GPIO11                                   |
| 5                     | GPIO10                                   |
| 6                     | GPIO15                                   |
| 7                     | GPIO9                                    |
| 8                     | GPIO16                                   |
| 9                     | GPIO18                                   |
| 10                    | GPIO17                                   |
| 11                    | GPIO19                                   |
| 12                    | GPIO20                                   |
| 13                    | GPIO21                                   |
| 14 (Lower Flex Cable)  | 270 Ohm Resistor -> GPIO26               |
| 15                    | GPIO0                                    |
| 16                    | GPIO1                                    |
| 17                    | GPIO2                                    |
| 18                    | GPIO3                                    |
| 19                    | GPIO4                                    |
| 20                    | GPIO7                                    |
| 21                    | GPIO6                                    |
| 22                    | GPIO5                                    |
| 23                    | VBUS                                     |
| 24                    | 270 Ohm Resistor -> GPIO28               |
| 25                    | 270 Ohm Resistor -> GPIO27               |
| 26                    | GND                                      |

### Additional Resources
- [CircuitPython: Installation and usage guide](https://circuitpython.org/)
- [KMK Firmware: Official KMK documentation](https://github.com/KMKfw/kmk_firmware)
- [Thonny IDE: Download Thonny](https://thonny.org/)

### Common Issues and Solutions

#### Reflashing the Raspberry Pi Pico
If you need to wipe the Raspberry Pi Pico’s flash memory due to errors or malfunction:

1. Use the `flash_nuke.uf2` file.
2. While the Pico is in mass storage mode, copy the file to the root to completely wipe the flash memory.
3. Repeat the CircuitPython installation process from Step 1.
