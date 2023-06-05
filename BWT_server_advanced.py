from flask import Flask, request
import json

app = Flask(__name__)

def dna_to_bwt(s):
    s = '^' + s + '|'  # adding start and end markers
    # construct suffix array
    suffixes = sorted([(s[i:], i) for i in range(len(s))])
    suffix_array = [i for _, i in suffixes]

    # construct BWT
    bwt = [s[j-1] for j in suffix_array]
    return ''.join(bwt)

def bwt_to_dna(bwt):
    # construct the table
    table = [''] * len(bwt)
    for _ in bwt:
        table = sorted(b + t for b, t in zip(bwt, table))
    # find the row that ends with '|'
    dna = next(row for row in table if row.endswith('|'))
    return dna.strip('^|')  # remove start and end markers

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