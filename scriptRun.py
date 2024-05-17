import subprocess
import time
import requests
import os

def open_terminal_windows(command, title):
    subprocess.Popen(f'start cmd /k "title {title} && {command}"', shell=True)

# Abrir terminales y ejecutar los archivos de blockchain
open_terminal_windows('python Cryptocurrency/LuisCoin5000.py', 'Blockchain Node 5000')
open_terminal_windows('python Cryptocurrency/LuisCoin5001.py', 'Blockchain Node 5001')
open_terminal_windows('python Cryptocurrency/LuisCoin5002.py', 'Blockchain Node 5002')

time.sleep(5)

# Direcciones de los nodos
nodes = [
    'http://127.0.0.1:5000',
    'http://127.0.0.1:5001',
    'http://127.0.0.1:5002'
]

# Conectar los nodos
for i, node in enumerate(nodes):
    other_nodes = [n for j, n in enumerate(nodes) if j != i]
    response = requests.post(f'{node}/connect_node', json={'nodes': other_nodes})
    print(f'Conectando {node} con {other_nodes}: {response.json()}')

# Mantener los procesos en ejecución
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Terminating...")
