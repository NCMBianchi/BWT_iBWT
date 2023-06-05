import requests
import sys
import os
import time

def is_valid_dna_sequence(sequence):
    return all(char in 'ACTG-' for char in sequence)

def is_valid_bwt_sequence(sequence):
    return all(char in 'ACTG-^|' for char in sequence)

def send_request(url, data):
    try:
        res = requests.post(url, json=data)
        return res.json()
    except requests.exceptions.ConnectionError:
        return {"error": "Please, provide a working combination of host and port as in this example: 'python3 BWT_client.py bwt host port \"sequence\"."}

def bwt_client(host, port, sequence):
    if not is_valid_dna_sequence(sequence):
        return {"error": "Invalid sequence. Sequence should only contain 'A', 'C', 'T', 'G', or '-'."}
    return send_request(f'http://{host}:{port}/bwt', {'sequence': sequence})

def ibwt_client(host, port, bwt_sequence):
    if not is_valid_bwt_sequence(bwt_sequence):
        return {"error": "Invalid BWT sequence. BWT sequence should only contain 'A', 'C', 'T', 'G', or '-'."}
    return send_request(f'http://{host}:{port}/ibwt', {'bwt_sequence': bwt_sequence})

def read_sequence_from_file(filename):
    with open(filename, 'r') as file:
        return file.read().strip()

def write_sequence_to_file(filename, sequence):
    if not filename.endswith('.txt'):
        filename += '.txt'
    with open(filename, 'w') as file:
        file.write(sequence)

if __name__ == "__main__":
    command = sys.argv[1]
    host = sys.argv[2]
    port = sys.argv[3]
    sequence = sys.argv[4]
    is_file_input = os.path.isfile(sequence)
    if is_file_input:
        sequence = read_sequence_from_file(sequence)
    if command in ['bwt', 'ibwt']:
        start_time = time.time()
        if command == 'bwt':
            result = bwt_client(host, port, sequence)
            print(result)
        elif command == 'ibwt':
            result = ibwt_client(host, port, sequence)
            print(result)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time} seconds")
        if is_file_input:
            output_filename = input("Please enter a name for the output file or type 'none' to skip: ")
            if output_filename.lower() != 'none':
                if 'result' in result:
                    write_sequence_to_file(output_filename, result['result'])
                else:
                    print("There was an error in the request. Output file was not created.")
    else:
        print("Please, provide a method between 'bwt' and 'ibwt' as in this example: 'python3 BWT_client.py bwt host port \"sequence\"'.")
        sys.exit(1)