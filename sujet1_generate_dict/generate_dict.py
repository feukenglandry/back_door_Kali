#!/usr/bin/env python3
import argparse, json

def generate_dict(nom, age, sexe, entries):
    data = []
    for _ in range(entries):
        data.append({"nom": nom, "age": age, "sexe": sexe})
    return data

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Générateur de dictionnaire")
    parser.add_argument("nom", type=str)
    parser.add_argument("age", type=str)
    parser.add_argument("sexe", type=str)
    parser.add_argument("entries", type=int)
    args = parser.parse_args()
    result = generate_dict(args.nom, args.age, args.sexe, args.entries)
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"[+] Écrit {len(result)} entrées dans data.json")
