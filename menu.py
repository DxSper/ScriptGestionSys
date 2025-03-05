import subprocess
import sys

# Afficher un texte stylisé
menutp_art = """

      ___          ___          ___          ___
     /\__\        /\  \        /\__\        /\__\
    /::|  |      /::\  \      /::|  |      /:/  /
   /:|:|  |     /:/\:\  \    /:|:|  |     /:/  /
  /:/|:|__|__  /::\~\:\  \  /:/|:|  |__  /:/  /  ___
 /:/ |::::\__\/:/\:\ \:\__\/:/ |:| /\__\/:/__/  /\__
 \/__/~~/:/  /\:\~\:\ \/__/\/__|:|/:/  /\:\  \ /:/  /
       /:/  /  \:\ \:\__\      |:/:/  /  \:\  /:/  /
      /:/  /    \:\ \/__/      |::/  /    \:\/:/  /
     /:/  /      \:\__\        /:/  /      \::/  /
     \/__/        \/__/        \/__/        \/__/

"""

# Menu des options
options = [
    "1 - Check CPU and RAM usage    | 6 - Show active network connections",
    "2 - Check updates              | 7 - Check disk usage of a directory",
    "3 - Check disk usage           | 8 - Show running services",
    "4 - Check DNS                  | 9 - Show recent system logs",
    "5 - Check IP                   | 10 - Check RAM usage stats",
    "e - Exit"
]

def afficher_menu():
    """Affiche le menu avec les options."""
    print(menutp_art)
    for option in options:
        print(option)

def executer_commande(commande):
    """Exécute une commande shell et affiche la sortie."""
    try:
        resultat = subprocess.run(commande, shell=True, check=True, text=True, capture_output=True)
        print(resultat.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de la commande: {e}")

def afficher_stats_ram():
    """Affiche les statistiques d'utilisation de la RAM de manière stylisée."""
    try:
        # Exécute la commande pour obtenir les informations sur la mémoire
        resultat = subprocess.run("free -h", shell=True, check=True, text=True, capture_output=True)
        lignes = resultat.stdout.splitlines()

        # Récupérer les valeurs de la mémoire
        mem_info = lignes[1].split()
        total_ram = mem_info[1]
        used_ram = mem_info[2]
        free_ram = mem_info[3]
        shared_ram = mem_info[4]
        buff_cache = mem_info[5]
        available_ram = mem_info[6]

        # Affichage stylisé
        print("\n=== Statistiques d'utilisation de la RAM ===")
        print(f"Total RAM: {total_ram}")
        print(f"Used RAM: {used_ram}")
        print(f"Free RAM: {free_ram}")
        print(f"Shared RAM: {shared_ram}")
        print(f"Buffer/Cache: {buff_cache}")
        print(f"Available RAM: {available_ram}")
        print("===============================================")

    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de la commande: {e}")

def choix_utilisateur():
    """Gère le choix de l'utilisateur."""
    choix = input("\nChoisissez [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [e]: \n")
    return choix

def main():
    """Boucle principale du programme."""
    while True:
        afficher_menu()
        choix = choix_utilisateur()

        if choix == "1":
            executer_commande("top -b -n 1 | head -n 10")  # Affiche les 10 premiers processus par utilisation CPU
        elif choix == "2":
            executer_commande("sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y")
        elif choix == "3":
            executer_commande("df -h | grep '^/dev'")
        elif choix == "4":
            domaine = input("Quel domaine voulez-vous scanner ? ")
            executer_commande(f'whois {domaine}')
        elif choix == "5":
            ip = input("Veuillez entrer l'IP: ")
            executer_commande(f'ping -c 4 {ip}')
        elif choix == "6":
            executer_commande("ss -tuln")  # Affiche les connexions réseau actives
        elif choix == "7":
            repertoire = input("Veuillez entrer le chemin du répertoire: ")
            executer_commande(f'du -sh {repertoire}')  # Affiche l'utilisation du disque pour le répertoire spécifié
        elif choix == "8":
            executer_commande("systemctl list-units --type=service --state=running")  # Affiche les services en cours d'exécution
        elif choix == "9":
            executer_commande("journalctl -n 50 --no-pager")  # Affiche les 50 dernières lignes des logs système
        elif choix == "10":
            afficher_stats_ram()  # Affiche les statistiques d'utilisation de la RAM
        elif choix.lower() == "e":
            print("Au revoir!")
            sys.exit()
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()