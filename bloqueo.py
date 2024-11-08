import socket
import keyboard
import mouse
import time

def bloquear_entrada():
  print("Teclado y mouse bloqueados.")
  while True:
    keyboard.block_key('a')  # Bloquear una tecla específica
