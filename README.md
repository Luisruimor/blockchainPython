# Blockchain en Python

https://youtu.be/lbwK7kLjm4Y?si=Ti8AIhikKfwxBbG2

<iframe width="350" height="197" src="https://youtu.be/lbwK7kLjm4Y?si=Ti8AIhikKfwxBbG2" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Este proyecto implementa una blockchain simple en Python utilizando Flask para la creación de una API web que permita operar con la blockchain.

Una vez ejecutado el programa, se levantará un servidor al que podrán realizar las siguientes peticiones a la siguiente URL: http://localhost:5000

Archivo para importar las peticiones en Postman: [postmanAPI.json](postmanAPI.json)

## `GET /mine_block`

Mina un bloque y devuelve un mensaje de éxito con la información del bloque minado.
    
```json
    {
        "message": "¡Felicidades, has minado un bloque!",
        "index": 2,
        "timestamp": "2024-05-15 12:34:56.789123",
        "proof": 533,
        "previous_hash": "abc123def456..."
    }
````



## `GET /get_chain`

Devuelve la cadena de bloques completa.

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


## `GET /is_valid`

Verifica si la cadena de bloques es válida.

```json
{
  "message": "El blockchain es valido"
}
````