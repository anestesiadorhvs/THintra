import json
import os
import time
import threading
from datetime import datetime
from pynput import keyboard
from ipv_data_source import ipv_data_source as device

class VitalSignsLogger:
    def __init__(self):
        pass

    def display_values(self, timestamp, temp_l):
        print(f"Timestamp: {timestamp}")
        for item in temp_l:
            print(f"{item[0]} = {item[1]}")

    def write_to_json(self, timestamp, temp_l, filename='vital_signs.json'):
        data = {'timestamp': timestamp}
        for item in temp_l:
            data[item[0]] = item[1]
        
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                file_data = json.load(file)
            file_data.append(data)
        else:
            file_data = [data]
        
        with open(filename, 'w') as file:
            json.dump(file_data, file, indent=4)
    
    def write_event_to_json(self, event, filename='events.json'):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = {'timestamp': timestamp, 'event': event}
        
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                file_data = json.load(file)
            file_data.append(data)
        else:
            file_data = [data]
        
        with open(filename, 'w') as file:
            json.dump(file_data, file, indent=4)

def on_press(key):
    if key == keyboard.Key.space:
        event = input("Ingrese un evento: ")
        logger.write_event_to_json(event)

# IP del monitor
dev_1 = device("192.168.0.192")
logger = VitalSignsLogger()

dev_1.start_client()
dev_1.start_watchdog()

last_update_time = time.time()

# Hilo para detectar la barra espaciadora
listener = keyboard.Listener(on_press=on_press)
listener.start()

try:
    while True:
        current_time = time.time()
        if current_time - last_update_time >= 5:  # Actualización cada 5 segundos
            temp_l = dev_1.get_vital_signs()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            logger.display_values(timestamp, temp_l)
            logger.write_to_json(timestamp, temp_l)
            last_update_time = current_time
except:
    dev_1.halt_client()
    print("\nCliente detenido...\n")
    print("Salida...[OK]")
