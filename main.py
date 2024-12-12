Fichier = "produits.txt"

def produits():
    try:
        open(Fichier, "a").close()
    except Exception as e:
        print(f"Erreur lors de la création du fichier : {e}")

def afficher():
    try:
        with open(Fichier, "r") as fichier:
            lignes = fichier.readlines()
            if not lignes:
                print("La liste des produits est vide.")
            else:
                print("\nListe des produits :")
                for index, ligne in enumerate(lignes, start=1):
                    nom, prix, quantite = ligne.strip().split(", ")
                    print(f"{index}. {nom} - Prix : {prix} $ - Quantité : {quantite}")
    except FileNotFoundError:
        print("Le fichier des produits n'existe pas encore.")
    except Exception as e:
        print(f"Erreur lors de la lecture des produits : {e}")

def ajouter():
    try:
        nom = input("Nom du produit : ").strip()
        prix = input("Prix : ").strip()
        quantite = input("Quantité : ").strip()

        with open(Fichier, "a") as fichier:
            fichier.write(f"{nom}, {prix}, {quantite}\n")
        print("Produit ajouté avec succès !")
    except Exception as e:
        print(f"Erreur lors de l'ajout du produit : {e}")

def recherche_produit():
    print("\nRecherche de produit :")
    print("1. Recherche séquentielle")
    print("2. Recherche dichotomique")

    choix = input("Faites votre choix : ")
    rechercher_nom = input("Entrez le nom du produit : ").strip()

    if choix == "1":
        recherche_sequentielle(rechercher_nom)
    elif choix == "2":
        recherche_dichotomique(rechercher_nom)
    else:
        print("Choix incorrect.")

def recherche_sequentielle(rechercher_nom):
    try:
        with open(Fichier, "r") as fichier:
            lignes = fichier.readlines()
            for ligne in lignes:
                nom, prix, quantite = ligne.strip().split(", ")
                if nom.lower() == rechercher_nom.lower():
                    print(f"Produit trouvé : {nom} - Prix : {prix} $ - Quantité : {quantite}")
                    return
            print("Produit non trouvé.")
    except Exception as e:
        print(f"Erreur lors de la recherche séquentielle : {e}")

def recherche_dichotomique(rechercher_nom):
    try:
        with open(Fichier, "r") as fichier:
            produits = [ligne.strip() for ligne in fichier]
            produits.sort()

            debut = 0
            fin = len(produits) - 1

            while debut <= fin:
                milieu = (debut + fin) // 2
                nom, prix, quantite = produits[milieu].split(", ")
                if nom.lower() == rechercher_nom.lower():
                    print(f"Produit trouvé : {nom} - Prix : {prix} $ - Quantité : {quantite}")
                    return
                elif nom.lower() < rechercher_nom.lower():
                    debut = milieu + 1
                else:
                    fin = milieu - 1

            print("Produit non trouvé.")
    except Exception as e:
        print(f"Erreur lors de la recherche dichotomique : {e}")

def tri_selection(liste):
    for i in range(len(liste)):
        max_index = i
        for j in range(i + 1, len(liste)):
            if liste[j] > liste[max_index]:
                max_index = j
        liste[i], liste[max_index] = liste[max_index], liste[i]
    return liste

def tri_bulles(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n - i - 1):
            if liste[j] < liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    return liste

def tri_insertion(liste):
    for i in range(1, len(liste)):
        key = liste[i]
        j = i - 1
        while j >= 0 and key > liste[j]:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = key
    return liste

def tri_rapide(liste):
    if len(liste) <= 1:
        return liste
    pivot = liste[len(liste) // 2]
    gauche = [x for x in liste if x > pivot]
    centre = [x for x in liste if x == pivot]
    droite = [x for x in liste if x < pivot]
    return tri_rapide(gauche) + centre + tri_rapide(droite)

def tri():
    try:
        with open(Fichier, "r") as fichier:
            lignes = fichier.readlines()

        if not lignes:
            print("La liste des produits est vide. Impossible de trier.")
            return

        print("\nTri de produit :")
        print("1. Tri par insertion")
        print("2. Tri à bulles")
        print("3. Tri par sélection")
        print("4. Tri rapide")
        choix_tri = input("Faites votre choix pour la méthode de tri : ")

        print("\nChoisissez le critère de tri :")
        print("1. Par nom")
        print("2. Par prix")
        print("3. Par quantité")
        choix_critere = input("Faites votre choix pour le critère : ")

        def critere_produit(ligne):
            nom, prix, quantite = ligne.strip().split(", ")
            if choix_critere == "1":
                return nom.lower()
            elif choix_critere == "2":
                return -float(prix)
            elif choix_critere == "3":
                return -int(quantite)
            else:
                raise ValueError("Critère de tri invalide.")

        liste_produits = sorted(lignes, key=critere_produit)

        if choix_tri == "1":
            liste_produits = tri_insertion(liste_produits)
        elif choix_tri == "2":
            liste_produits = tri_bulles(liste_produits)
        elif choix_tri == "3":
            liste_produits = tri_selection(liste_produits)
        elif choix_tri == "4":
            liste_produits = tri_rapide(liste_produits)
        else:
            print("Choix de tri invalide.")
            return

        with open(Fichier, "w") as fichier:
            fichier.write("".join(liste_produits))

        print("Liste triée avec succès !")
        afficher()

    except Exception as e:
        print(f"Erreur lors du tri : {e}")

def menu():
    produits()
    while True:
        print("\nMenu de gestion des produits")
        print("1. Afficher la liste des produits")
        print("2. Ajouter un produit")
        print("3. Rechercher un produit")
        print("4. Faire un tri")
        print("5. Quitter")

        choix = input("Entrez un numéro : ")
        if choix == "1":
            afficher()
        elif choix == "2":
            ajouter()
        elif choix == "3":
            recherche_produit()
        elif choix == "4":
            tri()
        elif choix == "5":
            print("Merci pour votre visite !")
            break
        else:
            print("Choix incorrect. Veuillez réessayer.")

if __name__ == "__main__":
    menu()