# try:
#     with open ('produits.txt', 'r') as fichier:
#         contenu = fichier.read()
# except FileNotFoundError:
#     print("Erreur : le fichier n'a pas été trouvé.")
# except PermissionError:
#     print("Erreur : permission insuffisantes pour ouvrir le fichier.")
# except Exception as e:
#     print(f"Erreur inattendu : {e}")

# Fichier = "produits.txt"

# def produits():
#     try:
#         open(Fichier, "a").close()
#     except Exception as e:
#         print(f"Erreur lors de la création du fichier : {e}")

# def afficher():
#     try:
#         with open(Fichier, "r") as fichier:
#             lignes = fichier.readlines()
#             if not lignes:
#                 print("La liste des produits est vide.")
#             else:
#                 print("\nListe des produits :")
#                 for index, ligne in enumerate(lignes, start=1):
#                     nom, prix, quantite = ligne.strip().split(", ")
#                     print(f"{index}. {nom} - Prix : {prix} $ - Quantité : {quantite}")
#     except FileNotFoundError:
#         print("Le fichier des produits n'existe pas encore.")
#     except Exception as e:
#         print(f"Erreur lors de la lecture des produits : {e}")

# def ajouter():
#     try:
#         nom = input("Nom du produit : ").strip()
#         prix = input("Prix : ").strip()
#         quantite = input("Quantité : ").strip()

#         with open(Fichier, "a") as fichier:
#             fichier.write(f"{nom}, {prix}, {quantite}\n")
#         print("Produit ajouté avec succès !")
#     except Exception as e:
#         print(f"Erreur lors de l'ajout du produit : {e}")

# def recherche_produit():
#     print("\nRecherche de produit :")
#     print("1. Recherche séquentielle")
#     print("2. Recherche dichotomique")

#     choix = input("Faite votre choix :")
#     rechercher_nom = input("Entre le nom du produit : ").strip()

#     if choix == "1":
#         recherche_sequentielle(rechercher_nom)
#     elif choix == "2":
#         recherche_dichotomique(rechercher_nom)
#     else:
#         print("Choix incorrect.")

# def recherche_sequentielle(rechercher_nom):
#     try:
#         with open(Fichier, "r") as fichier:
#             lignes = fichier.readlines()
#             for ligne in lignes:
#                 nom, prix, quantite = ligne.strip().split(", ")
#                 if nom.lower() == rechercher_nom.lower():
#                     print(f"Produit trouvé : {nom} - Prix : {prix} $ - Quantité : {quantite}")
#                     return
#             print("Produit non trouvé.")
#     except Exception as e:
#         print(f"Erreur lors de la recherche séquentielle : {e}")

# def recherche_dichotomique(rechercher_nom):
#     try:
#         with open(Fichier, "r") as fichier:
#             produits = [ligne.strip() for ligne in fichier]
#             produits.sort()

#             debut = 0
#             fin = len(produits) - 1

#             while debut <= fin:
#                 milieu = (debut + fin) // 2
#                 nom, prix, quantite = produits[milieu].split(", ")
#                 if nom.lower() == rechercher_nom.lower():
#                     print(f"Produit trouvé : {nom} - Prix : {prix} $ - Quantité : {quantite}")
#                     return
#                 elif nom.lower() < rechercher_nom.lower():
#                     debut = milieu + 1
#                 else:
#                     fin = milieu - 1

#             print("Produit non trouvé.")
#     except Exception as e:
#         print(f"Erreur lors de la recherche dichotomique : {e}")

# def tri():
#     print("\nTri de produit :")
#     print("1. Tri par sélection")
#     print("2. Tri à bulles")
#     print("3. Tri à bulles")
#     print("4. Tri rapide")

#     choix = input("Faite votre choix :")
#     rechercher_nom = input("ezfzefez : ").strip()

#     if choix == "1":
#         tri_selection(liste)
#     elif choix == "2":
#         tri_bulles(rechercher_nom)
#     elif choix == "3":
#         tri_insertion(rechercher_nom)
#     elif choix == "4":
#         tri_rapide(rechercher_nom)
#     else:
#         print("Choix invalide.")

# def tri_selection(liste):
#     for i in range(len(liste)):
#         max_index = i
#         for j in range(i + 1, len(liste)):
#             if liste[j] > liste[max_index]:
#                 max_index = j
#         liste[i], liste[max_index] = liste[max_index], liste[i]
#     return liste


# def menu():
#     produits()
#     while True:
#         print("\nMenu de gestion des produits")
#         print("1. Afficher la liste des produits")
#         print("2. Ajouter un produit")
#         print("3. Rechercher un produit")
#         print("4. Faire un tri")
#         print("5. Quitter")

#         choix = input("Entre un numéro : ")
#         if choix == "1":
#             afficher()
#         elif choix == "2":
#             ajouter()
#         elif choix == "3":
#             recherche_produit()
#         elif choix == "4":
#             tri_selection()
#         elif choix == "5":
#             print("Merci pour ta visite !")
#             break
#         else:
#             print("Pas bon ! Réessaye ou conséquence.")

# if __name__ == "__main__":
#     menu()