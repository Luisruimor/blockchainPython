# Blockchain en Python

![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)

[Enviroment Anaconda](environment.yml)

Este repositorio está basado en un tutorial de Youtube => https://youtu.be/lbwK7kLjm4Y?si=Ti8AIhikKfwxBbG2

Consta de 3 partes:

[1ª Parte](#parte-1-creación-de-una-blockchain-simple):
Creación de una blockchain simple en Python utilizando Flask para la creación de una API web que permita operar sobre ella.

[2ª Parte](#parte-2-creación-de-una-criptomoneda-simple):
Creación de una criptomoneda simple basada en la blockchain creada en la parte 1. 

3ª Parte: Contratos inteligentes (no implementado en este repositorio


## Parte 1: Creación de una blockchain simple

### Ejecución

```bash'
python blockchain.py
```

Una vez ejecutado el programa, se levantará un servidor en `http://localhost:5000/` que permitirá interactuar con la blockchain a través de las siguientes rutas:

### Peticiones disponibles
Archivo para importar las peticiones en Postman: [postmanAPI.json](postmanAPI.json)

#### Minar un bloque 
Mina un bloque y devuelve un mensaje de éxito con la información del bloque minado.

`GET /mine_block`
    
```json
    {
        "message": "¡Felicidades, has minado un bloque!",
        "index": 2,
        "timestamp": "2024-05-15 12:34:56.789123",
        "proof": 533,
        "previous_hash": "abc123def456..."
    }
````

#### Devolver la cadena de bloques
Devuelve la cadena de bloques completa.

`GET /get_chain`

```json
{
  "chain": [
      {
        "index": 1,
        "timestamp": "2024-05-15 12:34:56.789123",
        "proof": 1,
        "previous_hash": "0"
      },
      {
        "index": 2,
        "timestamp": "2024-05-15 12:36:01.123456",
        "proof": 533,
        "previous_hash": "abc123def456..."
      }
    ],
  "length": 2
}
````

#### Validar la cadena de bloques 
Verifica si la cadena de bloques es válida.

`GET /is_valid`

```json
{
  "message": "El blockchain es valido"
}
````

### ¿Que aptitudes he adquirido con este proyecto?:
#### Flask
Flask es un microframework de Python que facilita la creación de aplicaciones web. Con este proyecto, aprendí a:

<img alt="Flask" src="img/flask.png" width="400"/>

- Crear una API RESTful para interactuar con la blockchain.
- Manejar rutas y métodos HTTP en Flask.
- Ejecutar y probar la aplicación web localmente.

#### Clases y Objetos en Python
Este proyecto reforzó mi conocimiento sobre la programación orientada a objetos en Python. Específicamente, aprendí a:

<img alt="Python" src="img/python.svg" width="400"/>

- Definir clases y métodos para representar la estructura y comportamiento de una blockchain.
- Utilizar instancias de clase para gestionar la cadena de bloques y las transacciones.
- Implementar métodos para resolver problemas específicos, como la prueba de trabajo y la validación de la cadena.

#### Blockchain
Me ha permitido entender y aplicar los conceptos básicos de blockchain. Con este proyecto, aprendí a:

<img alt="Blockchain" src="img/bitcoin.png" width="400"/>

- Crear y gestionar una cadena de bloques.
- Implementar la prueba de trabajo (Proof of Work) para minar nuevos bloques.
- Verificar la integridad y validez de la cadena de bloques.

## Parte 2: Creación de una criptomoneda simple
Esta parte se basa en crear una criptomoneda basada en la blockchain creada en la parte 1. Al crear una criptomoneda, lo que conseguimos es descentralizar la red y permitir que los usuarios realicen transacciones entre ellos.

### Ejecución

Para cada nodo que queramos añadir a la red, ejecutar el siguiente comando:

Si quieres añadir un puerto más, solo tienes que añadir un archivo con el nombre LuisCoin5003.py, cambiar el puerto de escucha de Flask y y añadir el siguiente comando:
```bash'
python LuisCoin5003.py
```

En este caso vamos a añadir 3 nodos a la red, por lo que ejecutaremos los siguientes comandos:

```bash'
python LuisCoin5000.py
python LuisCoin5001.py
python LuisCoin5002
```

Una vez ejecutado el programa, se levantará un servidor en `http://localhost:5000/` que permitirá interactuar con la blockchain a través de las siguientes rutas:

Posteriormente antes de cualquier operación, se debe desde cada nodo conectarse a los demás nodos, para ello se debe ejecutar la peticion [POST /connect_node](#conectar-un-nuevo-nodo) en cada nodo.

Para automatizar este proceso, he creado dos scripts para que ejecuten los nodos y se conecten entre ellos:

#### Windows
```bash'
python scriptsToRun/scriptRun.py
```

#### MacOS

```bash'
python scriptsToRun/scriptRunMac.py
```


### Peticiones disponibles (Aparte de las de la parte 1)
Archivo para importar las peticiones en Postman: [postmanAPI.json](postmanAPI.json)

#### Añadir una Nueva Transacción
Añade una nueva transacción a la cadena de bloques.

`POST /add_transaction`

**Cuerpo de la solicitud:**
```json
{
  "sender": "dirección_origen",
  "receiver": "dirección_destino",
  "amount": 10
}
```

**Ejemplo de respuesta:**
```json
{
  "message": "La transacción será añadida al bloque 2"
}
```

#### Conectar un Nuevo Nodo
Conecta un nuevo nodo a la red de blockchain.

`POST /connect_node`

**Cuerpo de la solicitud:**
```json
{
  "nodes": ["http://127.0.0.1:5001", "http://127.0.0.1:5002"]
}
```

**Ejemplo de respuesta:**
```json
{
  "message": "Todos los nodos han sido conectados",
  "total_nodes": ["127.0.0.1:5001", "127.0.0.1:5002"]
}
```

#### Reemplazar la Cadena por la Más Larga
Reemplaza la cadena local por la más larga en la red si es necesario. El propósito de esta función es asegurar que todos los nodos de la red tengan la misma cadena de bloques.

`GET /replace_chain`

**Ejemplo de respuesta si la cadena fue reemplazada:**
```json
{
  "message": "La cadena fue reemplazada por la más larga.",
  "new_chain": [...]
}
```

**Ejemplo de respuesta si la cadena es la más larga:**
```json
{
  "message": "La cadena es la más larga.",
  "actual_chain": [...]
}
```

### ¿Qué aptitudes he adquirido con este proyecto?
#### Orphaned Blocks
Una de las aptitudes que he adquirido con este proyecto es el conocimiento sobre los orphaned blocks. He aprendido cómo 
se generan estos bloques huérfanos cuando dos mineros encuentran soluciones válidas al mismo tiempo y cómo la red decide
cuál de las cadenas resultantes se adopta, dejando al otro bloque como huérfano. Esta comprensión es crucial para asegurar
la integridad y consenso en una blockchain.

#### UUID (Universally Unique Identifier)
Un UUID (Universally Unique Identifier) es un estándar de identificación que permite crear un identificador único en 
prácticamente cualquier contexto, sin necesidad de coordinar con una autoridad central para asegurarse de que no se repita.

La biblioteca uuid en Python permite generar estos identificadores de manera sencilla. Ofrece varias versiones de UUIDs, cada una con un método diferente de generación:
En este proyecto, utilicé UUID 4.

#### Descentralización y Consenso
La descentralización y el consenso son conceptos fundamentales en blockchain.

En este proyecto, es una blockchain de "cadena más larga", la cadena de bloques con más trabajo acumulado, es decir, la 
que ha requerido más esfuerzo computacional para ser creada.