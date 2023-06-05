# BWT_iBWT
A test GitHub repository for a set of client/server python scripts (as part of the Scientific Programming class).

## Python scripts
### CLIENT
This script allows the user to send a request conversion:
- from **DNA sequence** to a Borrows-Wheeler Transform string
- from a **Burrows-Wheeler Transform** string to a DNA sequence
The host:port required by *flask* (an external package https://flask.palletsprojects.com/en/2.3.x/) is manually inputed by the user when invoking the client-to-server connection. Here's an example of the syntax required:
> python3 BWT_client.py method host port sequence

The method can either be *bwt* (*i.e.* DNA to BWT) or *ibwt* (*i.e.* inverse bwt, BWT to DNA), the host should be in the 0.0.0.0 format and port should be in the *10^3* order of magnitude.
Sequence can be inputed either directly as a string between "", or from an external .txt file: the script handles both approaches, recognising the extension in the name and reading the file: this file should only contain the sequence itself, with characters 'A', 'C', 'G', 'T' and '-' for mismatches.
Whenever a sequence is passed to the client and server from a .txt file, the client - upon receival of the output from the server and having displayed it – asks the user to input the name of a file where the sequence would be saved. Whenever a sequence is instead passed directly in the invoke command, the output is only displayed. 
The script also handles a simple timer (via the built-in *time* python package) to measure the computation and response time.

### SERVER
Two options are provided: one using a very simple (*i.e.* BWT_server_simple.py) – yet not very fast or efficient – set of functions for conversion, and one more advanced using suffix arrays (*i.e.* BWT_server_advanced.py) – which is slightly more efficient. Both avoid using external packages that would be even more efficient, yet would miss the point of this project. Here's an example of the syntax required:
> python3 BWT_server______.py

The *dna_to_bwt()* function used when the client invokes the *bwt* method adds '^' at the beginning of the sequence, and '|' at the end of it, to then perform the Burrows-Wheeler transformation and return the string with the markers included.
The *bwt_to_dna()* function used then the client invoked the *ibwt* method reorganises correctly the string using the '^' and '|' as markers, to then remove them before returning the string to the client.

## Server host:port reconfiguration
In order to avoid hard-coding the server host:port in the script, those were written in a .json file which is accessed by the *BWT_server.py* script when invoked. Moreover, such host:port combination can be modified via the **modify_config.py** script and the following syntax:
> python3 modify_config.py 0.0.0.0 5000

## Technical notes
Since I decided to use *flask* instead of *socket*, there's **no size cap** for the file transmission from client to server. This could anyway be implemented via:
> from flask import Flask
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # e.g., limit upload size to 16MB

Such a limitation could be required to avoid DoS (denial-of-services) attacks or resource exhaustion.
Moreover, since this tool is going to handle only DNA sequences and BWT strings, no EOF (end of file) terminator was used. And no multiprocessing approach was implemented - although both could be easily implemented without the need of huge alterations to the code.

## Example files
Some examples of **shell commands** are provided in the *commands_example.sh* file, while some examples of DNA sequences and BWT strings are respectively in the *dna_seq.txt* and *bwt_seq.txt* files. 

## Literature on the topic
https://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform
https://www.cs.jhu.edu/~langmea/resources/bwt_fm.pdf
https://www.cs.jhu.edu/~langmea/resources/burrows_wheeler.pdf