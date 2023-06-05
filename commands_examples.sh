#################################
####### NORMAL  OPERATION #######
#################################

#### to invoke the server (simple)
python3 BWT_server_simple.py

#### to invoke the server (advanced)
python3 BWT_server_advanced.py

#### to invoke the client
python3 BWT_client.py bwt 127.0.0.1 5000 "CGATCGATCTGACGTACGATCGATC"
python3 BWT_client.py bwt 127.0.0.1 5000 dna_seq.txt
python3 BWT_client.py ibwt 127.0.0.1 5000 "TGGGGG^ATTATTTCCCCCGAAAAC|C"
python3 BWT_client.py ibwt 127.0.0.1 5000 bwt_seq.txt




#################################
############# EXTRA #############
#################################

#### to modify the BWT_server_congif.json file:
python3 modify_config.py 127.0.0.2 5000