import board
import digitalio
import time

# Define los pines para las filas y las columnas (ajusta según tu configuración)
row_pins = [board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21, board.GP22, board.GP23]
col_pins = [board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8]

# Configurar pines de fila como salidas
rows = [digitalio.DigitalInOut(pin) for pin in row_pins]
for row in rows:
    row.direction = digitalio.Direction.OUTPUT
    row.value = False  # Inicializa en bajo

# Configurar pines de columna como entradas con pull-down
cols = [digitalio.DigitalInOut(pin) for pin in col_pins]
for col in cols:
    col.direction = digitalio.Direction.INPUT
    col.pull = digitalio.Pull.DOWN

def scan_matrix():
    for row_index, row in enumerate(rows):
        # Activa una fila a la vez
        row.value = True
        for col_index, col in enumerate(cols):
            if col.value:  # Si la columna está en alto, se detectó una tecla presionada
                print(f"Tecla pulsada: Fila {row_index+1}({row_pins[row_index]}), Columna {col_index+1}({col_pins[col_index]})")
        row.value = False  # Apaga la fila

try:
    print("Escaneando la matriz del teclado. Presiona las teclas...")
    while True:
        scan_matrix()
        time.sleep(0.1)  # Pequeña espera entre escaneos
except KeyboardInterrupt:
    print("Detenido por el usuario.")

finally:
    # Desinicializa todos los pines al finalizar
    for row in rows:
        row.deinit()
    for col in cols:
        col.deinit()
