import gpiozero as GPIO
import time 

led_verde= LED(18)
led_rojo= LED(19)
led_azul= LED(17)


diccionario_colores = {
    "verde": led_verde,
    "rojo": led_rojo,
    "azul": led_azul
}

def encender_led_verde():
    led_verde.on()
    time.sleep(1)
    led_verde.off()

def encender_led_rojo():
    led_rojo.on()
    time.sleep(1)
    led_rojo.off()

def encender_led_azul():
    led_azul.on()
    time.sleep(1)
    led_azul.off()


while True:
    color = input("Ingresa el color del led que quieras encender (verde, rojo o azul): ")
    if color == "verde":
        encender_led_verde()
    elif color == "rojo":
        encender_led_rojo()
    elif color == "rojo":
        encender_led_azul()
        color == "azul"
    else:
        print("Color no válido elije entre", list(diccionario_colores.keys()))

        parpadear = input("¿Quieres que parpadee? (si/no): ")
        if parpadear == "si":
            diccionario_colores[color].blink()
        elif color == "no":
                diccionario_colores[color].on()
        else:
                print("Opción no válida")

        
    salir = input("¿Quieres salir del programa? (si/no): ") 
    if salir == "si":
                break
    else:
     print("Color no válido elije entre", list(diccionario_colores.keys()))