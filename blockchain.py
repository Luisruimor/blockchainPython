import datetime
import hashlib  #para poder hashear los bloques
import json #codificar antes de hashearlo
from flask import Flask,jsonify

# Paso 1 - Crear nuestra blockchain
class Blockchain:
    def __init__(self):
        self.chain = [] # Al inicio nuestra cadena será una lista vacia
        self.create_block(proof=1,previous_hash='0')    # '' porque usaremos SHA256 que solo acepta comilla simple

    def create_block(self,proof,previous_hash):
        block = {'index':len(self.chain)+1,
                 'timestamp':str(datetime.datetime.now()), # Tiempo de cuando se crea el bloque
                 'proof': proof,
                 'previous_hash':previous_hash}
        self.chain.append(block)    # Adjuntamos el bloque a nuestra cadena
        return block

    def get_previous_block (self):
        return self.chain[-1]   # Usamos -1 para usar el último bloque

    # Un problema dificil de resolver y facil de verificar

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False

        while check_proof is False: # Hasta que encontremos el proof que resuelva el problema
            hash_operation = hashlib.sha256(str(new_proof**2-previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof+=1
        return new_proof

    # Debemos checkear el previous hash de la cadena
    def hash(self,block):
        encoded_block = json.dumps(block,sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self,chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain): # iterar sobre todos los bloques
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2-previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False

            previous_block = block
            block_index += 1
        return True

# Web App para interactuar con nuestra blockchain
app = Flask(__name__)   #estandar de flask
blockchain = Blockchain()

# Minar un Nuevo Bloque
@app.route('/mine_block',methods=['GET'])

def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']

    proof = blockchain.proof_of_work(previous_proof)

    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof,previous_hash)

    response = {
        'message': 'Felicidades has minado un bloque!',
        'index':block['index'],
        'timestamp':block['timestamp'],
        'proof':block['proof'],
        'previous_hash':block['previous_hash']
    }

    return jsonify(response),200

# Obtener toda la blockchain
@app.route('/get_chain',methods=['GET'])
def get_chain():
    response = {
        'chain':blockchain.chain,
        'length':len(blockchain.chain)
    }
    return jsonify(response),200


# Checkear la validez de la cadena de bloques
@app.route("/is_valid",methods=['GET'])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message':'El blockchain es valido'}
    else:
        response = {'meessage': 'El blockchain ES INVALIDO!!!!!'}
    return jsonify(response),200


app.run(host='0.0.0.0',port=5000)