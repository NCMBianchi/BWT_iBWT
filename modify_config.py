import json

def modify_config(host, port):
    config = {
        "host": host,
        "port": port
    }
    
    with open("config.json", "w") as config_file:
        json.dump(config, config_file)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python3 modify_config.py <host> <port>")
    else:
        host = sys.argv[1]
        port = int(sys.argv[2])
        modify_config(host, port)