from pyfirmata2 import Arduino, OUTPUT
from time import sleep

# Definir los pines de los motores en la placa Arduino Mega
motor_izquierdo_ena = 9
motor_izquierdo_in1 = 8
motor_izquierdo_in2 = 7
motor_derecho_enb = 3
motor_derecho_in3 = 6
motor_derecho_in4 = 5

# Crear una instancia de Arduino
board = Arduino('COM3')  # Asegúrate de ajustar el puerto adecuado

# Configurar los pines de los motores como salidas
#board.digital[motor_izquierdo_ena].mode = Arduino.OUTPUT 
#board.digital[motor_izquierdo_in1].mode = Arduino.OUTPUT
#board.digital[motor_izquierdo_in2].mode = Arduino.OUTPUT
#board.digital[motor_derecho_enb].mode = Arduino.OUTPUT
#board.digital[motor_derecho_in3].mode = Arduino.OUTPUT
#board.digital[motor_derecho_in4].mode = Arduino.OUTPUT
board.set_pin_mode(motor_izquierdo_ena, OUTPUT)
board.set_pin_mode(motor_izquierdo_in1, OUTPUT)
board.set_pin_mode(motor_izquierdo_in2, OUTPUT)
board.set_pin_mode(motor_derecho_enb, OUTPUT)
board.set_pin_mode(motor_derecho_in3, OUTPUT)
board.set_pin_mode(motor_derecho_in4, OUTPUT)
# Definir constantes para las direcciones
FORWARD = 1
BACKWARD = 0
LEFT = 1
RIGHT = 0
BOTH = 2

def move(motor, direction):
    if motor == LEFT:
        if direction == FORWARD:
            board.digital[motor_izquierdo_ena].write(1)
            board.digital[motor_izquierdo_in1].write(0)
            board.digital[motor_izquierdo_in2].write(1)
        else:
            board.digital[motor_izquierdo_ena].write(1)
            board.digital[motor_izquierdo_in1].write(1)
            board.digital[motor_izquierdo_in2].write(0)
    else:
        if direction == FORWARD:
            board.digital[motor_derecho_enb].write(1)
            board.digital[motor_derecho_in3].write(1)
            board.digital[motor_derecho_in4].write(0)
        else:
            board.digital[motor_derecho_enb].write(1)
            board.digital[motor_derecho_in3].write(0)
            board.digital[motor_derecho_in4].write(1)

def stop(motor):
    if motor == LEFT or motor == BOTH:
        board.digital[motor_izquierdo_ena].write(0)
    if motor == RIGHT or motor == BOTH:
        board.digital[motor_derecho_enb].write(0)

# Configurar motores y mostrar mensaje de inicio
print("Probando motores")

try:
    while True:
        # Realizar movimientos de prueba
        move(LEFT, FORWARD)
        move(RIGHT, FORWARD)
        sleep(2)
        stop(LEFT)
        sleep(2)
        move(LEFT, FORWARD)
        move(RIGHT, FORWARD)
        sleep(2)

except KeyboardInterrupt:
    # Detener los motores si se interrumpe el programa con Ctrl+C
    stop(BOTH)



