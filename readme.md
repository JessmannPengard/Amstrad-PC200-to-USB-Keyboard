# Conversión de Teclado Amstrad Sinclair PC200/PPC 640/512 a USB con Raspberry Pi Pico

Este proyecto tiene como objetivo convertir un teclado de un Amstrad Sinclair PC200 o de un Amstrad PPC 640/512 en un dispositivo USB funcional utilizando una **Raspberry Pi Pico**. Esto se logra a través del uso de **CircuitPython** y la librería **KMK**, que permite la creación de firmware personalizable para teclados.

## Requisitos previos

Antes de comenzar, necesitarás los siguientes componentes y software:

### Hardware:
- Un teclado de un **Amstrad Sinclair PC200** o **Amstrad PPC 640/512**.
- Una **Raspberry Pi Pico**.
- Cables o conectores para realizar la conexión entre la Pico y la matriz del teclado.

### Software:
- **CircuitPython**: un sistema operativo ligero diseñado para microcontroladores como la Raspberry Pi Pico.
- **KMK Firmware**: una librería de Python para la creación de teclados personalizados.
- **Thonny IDE** (opcional): un entorno de desarrollo fácil de usar para trabajar con CircuitPython.

## Guía de instalación

### Paso 1: Instalación de CircuitPython en la Raspberry Pi Pico

1. **Descargar CircuitPython**:  
   Descarga la última versión de **CircuitPython** compatible con la Raspberry Pi Pico desde el siguiente enlace:  
   [CircuitPython para Raspberry Pi Pico](https://circuitpython.org/board/raspberry_pi_pico/)

2. **Flashear CircuitPython**:  
   Con la Raspberry Pi Pico desconectada, mantén presionado el botón **BOOTSEL** en la placa y conéctala al puerto USB de tu computadora. Esto la pondrá en modo almacenamiento masivo.

3. **Copiar el archivo `.uf2` de CircuitPython**:  
   Una vez que la Raspberry Pi Pico esté en modo almacenamiento, copia el archivo **`adafruit-circuitpython-raspberry_pi_pico-es-9.1.3.uf2`** a la raíz del dispositivo. La Pico se reiniciará automáticamente y se montará como una unidad de almacenamiento con el nombre **CIRCUITPY**.

### Paso 2: Configuración del entorno

1. **Copiar la carpeta `kmk`**:  
   Descarga la librería KMK desde el siguiente enlace:  
   [KMK Firmware](https://github.com/KMKfw/kmk_firmware)  
   Luego, copia la carpeta `kmk` a la raíz de la unidad **CIRCUITPY**.

2. **Copia de archivos de configuración**:  
   Copia los siguientes archivos al directorio raíz de **CIRCUITPY**:
   
   - `boot.py`: Este archivo se asegura de que la Raspberry Pi Pico no se monte como almacenamiento masivo al encenderse.
   - `main.py`: Contiene la lógica principal que convierte las entradas del teclado en señales USB.

3. **Reiniciar la Raspberry Pi Pico**:  
   Desconecta y vuelve a conectar la Raspberry Pi Pico. En este punto, el teclado debería estar funcional y listo para ser utilizado como dispositivo USB.

### Paso 3: Uso de la herramienta `scanner.py`

El archivo `scanner.py` es una utilidad diseñada para ayudar a identificar las conexiones de la matriz del teclado. Al ejecutar este script, puedes presionar las teclas del teclado Amstrad y obtener la fila y columna correspondiente, lo cual es útil para mapear correctamente las teclas en **KMK**.

1. **Ejecutar `scanner.py`**:  
   Usa **Thonny IDE** para ejecutar `scanner.py` en la Raspberry Pi Pico. Thonny puede descargarse desde el siguiente enlace:  
   [Descargar Thonny](https://thonny.org/)

2. **Mapeo de teclas**:  
   A medida que presiones las teclas, el script te mostrará la fila y columna a las que pertenecen junto a los GPIO de la Pi Pico correspondientes. Utiliza esta información para personalizar tu archivo `main.py` y crear el mapeo correcto del teclado.

## Recursos adicionales

- **CircuitPython**: [Guía de instalación y uso de CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython/overview)
- **KMK Firmware**: [Documentación oficial de KMK](https://github.com/KMKfw/kmk_firmware)
- **Thonny IDE**: [Descargar Thonny](https://thonny.org/)

## Problemas comunes y soluciones

### Reflasheo de la Raspberry Pi Pico

En caso de que necesites limpiar la memoria flash de la Raspberry Pi Pico por errores o mal funcionamiento:

1. Utiliza el archivo **`flash_nuke.uf2`**.

2. Con la Pico en modo almacenamiento masivo, copia el archivo a la raíz para limpiar la memoria flash completamente.

3. Repite el proceso de instalación de **CircuitPython** desde el Paso 1.

---
