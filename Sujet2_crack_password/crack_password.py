#!/usr/bin/env python3
import sys, hashlib, json

def crack_hash(target_hash, dict_file):
    with open(dict_file, encoding="utf-8") as f:
        data = json.load(f)
    for entry in data:
        candidate = entry["nom"] + entry["age"] + entry["sexe"]
        if hashlib.md5(candidate.encode()).hexdigest() == target_hash:
            print(f"[+] Mot de passe trouvé : {candidate}")
            return
    print("[-] Mot de passe non trouvé.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: crack_password.py <md5_hash> <data.json>")
        sys.exit(1)
    crack_hash(sys.argv[1], sys.argv[2])
