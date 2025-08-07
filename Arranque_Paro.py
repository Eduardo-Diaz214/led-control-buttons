from machine import Pin
import time

# Definir los pines de los botones como entradas con resistencia de pull-up
boton_encender = Pin(23, Pin.IN, Pin.PULL_UP)  # Botón de encendido
boton_apagar = Pin(22, Pin.IN, Pin.PULL_UP)    # Botón de apagado

# Definir el pin del LED como salida
led = Pin(25, Pin.OUT)

# Variable para almacenar el estado del LED
estado_led = False

while True:
    # Verificar si se presionó el botón de encendido (activo en bajo con PULL_UP)
    if boton_encender.value() == 0:  # Botón presionado
        estado_led = True            # Cambia el estado del LED a encendido
        led.value(1)                 # Enciende el LED
        time.sleep(0.2)              # Retraso para evitar rebotes

    # Verificar si se presionó el botón de apagado
    if boton_apagar.value() == 0:    # Botón presionado
        estado_led = False           # Cambia el estado del LED a apagado
        led.value(0)                 # Apaga el LED
        time.sleep(0.2)              # Retraso para evitar rebotes