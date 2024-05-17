import subprocess
import time
import requests
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

# Comando para abrir una nueva terminal en macOS
def open_terminal_mac(command):
    script = f'''
    tell application "Terminal"
        do script "{command}"
    end tell
    '''
    subprocess.run(["osascript", "-e", script])

scripts = [
    os.path.join(current_dir, 'Cryptocurrency/LuisCoin5000.py'),
    os.path.join(current_dir, 'Cryptocurrency/LuisCoin5001.py'),
    os.path.join(current_dir, 'Cryptocurrency/LuisCoin5002.py')
]

# Abrir nuevas terminales y ejecutar los archivos de blockchain
print("Abriendo terminales y ejecutando los scripts de blockchain...")
open_terminal_mac(f'python3 {scripts[0]}')
open_terminal_mac(f'python3 {scripts[1]}')
open_terminal_mac(f'python3 {scripts[2]}')

# Esperar unos segundos para asegurarse de que los servidores se hayan iniciado
print("Esperando a que los servidores de Flask se inicien...")
time.sleep(10)  # Aumentar el tiempo de espera

# Direcciones de los nodos
nodes = [
    'http://127.0.0.1:5000',
    'http://127.0.0.1:5001',
    'http://127.0.0.1:5002'
]

# Verificar que los servidores están en funcionamiento
def check_server(node):
    try:
        response = requests.get(f'{node}/get_chain')
        if response.status_code == 200:
            return True
    except requests.exceptions.ConnectionError:
        return False

for node in nodes:
    while not check_server(node):
        print(f'Esperando a que el servidor {node} se inicie...')
        time.sleep(2)  # Esperar antes de volver a intentar
    print(f'Servidor {node} iniciado.')

# Conectar los nodos entre sí
for i, node in enumerate(nodes):
    other_nodes = [n for j, n in enumerate(nodes) if j != i]
    try:
        response = requests.post(f'{node}/connect_node', json={'nodes': other_nodes})
        print(f'Conectando {node} con {other_nodes}: {response.json()}')
    except requests.exceptions.ConnectionError as e:
        print(f'Error al conectar {node}: {e}')

# Mantener los procesos en ejecución
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Terminating...")
