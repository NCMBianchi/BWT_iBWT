from flask import Flask, request
import json

app = Flask(__name__)

def dna_to_bwt(s):
    s = '^' + s + '|'  # adding start and end markers
    table = sorted(s[i:] + s[:i] for i in range(len(s)))
    last_column = ''.join(row[-1] for row in table)
    return last_column

def bwt_to_dna(r):
    table = [""] * len(r)
    for _ in range(len(r)):
        table = sorted(r[i] + table[i] for i in range(len(r)))
    return table[r.index('|')].strip('^|')  # remove start and end markers

@app.route('/bwt', methods=['POST'])
def bwt():
    data = request.get_json()
    sequence = data.get('sequence')
    return json.dumps({'result': dna_to_bwt(sequence)})

@app.route('/ibwt', methods=['POST'])
def ibwt():
    data = request.get_json()
    bwt_sequence = data.get('bwt_sequence')
    return json.dumps({'result': bwt_to_dna(bwt_sequence)})

if __name__ == "__main__":
    with open("server_config.json") as config_file:
        config = json.load(config_file)
        app.run(host=config['host'], port=config['port'])