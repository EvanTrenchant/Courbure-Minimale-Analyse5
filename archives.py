import matplotlib.pyplot as plt
import numpy as np

# Fonction pour ajuster y afin d'atteindre la longueur cible
def ajuster_y_trois_points(x_1, y_1, y_2, y_3, longueur_cible):
    """
    Ajuste les valeurs de y_1, y_2, et y_3 pour atteindre la longueur de courbe cible.
    """
    A = [[-1, 0], [-x_1, y_1], [0, y_2], [x_1, y_3], [1, 0]]
    while (longueur_courbe_v2(A) <= longueur_cible - 0.001) or (longueur_courbe_v2(A) >= longueur_cible + 0.001):
        erreur = longueur_cible - longueur_courbe_v2(A)
        # Ajustement des trois points de contrôle
        y_1 += y_1 * erreur * 0.5
        y_2 += y_2 * erreur * 0.5
        y_3 += y_3 * erreur * 0.5
        A = [[-1, 0], [-x_1, y_1], [0, y_2], [x_1, y_3], [1, 0]]
    return A, y_1, y_2, y_3

# Fonction principale pour calculer K en fonction de x avec trois points de contrôle
def calculer_k_en_fonction_de_x_trois_points(longueur_cible):
    """
    Calcule K en fonction de x pour une longueur de courbe cible donnée,
    et trouve A correspondant au plus petit K avec trois points de contrôle.
    """
    x_1 = 0
    y_1, y_2, y_3 = 0.1, 0.1, 0.1
    A_opt = [[-1, 0], [-x_1, y_1], [0, y_2], [x_1, y_3], [1, 0]]
    K_opt = float('inf')  # Initialiser à une valeur très grande

    x_values = []  # Liste pour stocker les valeurs de x
    K_values = []  # Liste pour stocker les valeurs de K

    for i in range(50, 0, -1):
        # Décrément de x pour changer la courbure
        x_1 = i / 50
        A, y_1, y_2, y_3 = ajuster_y_trois_points(x_1, y_1, y_2, y_3, longueur_cible)

        # Calcul de la courbure actuelle
        K_current = K(A)
        x_values.append(x_1)
        K_values.append(K_current)

        # Mise à jour de la courbure optimale si K est plus petit
        if K_current < K_opt:
            K_opt = K_current
            A_opt = A

    return x_values, K_values, A_opt

# Fonction pour tracer les résultats
def tracer_resultats_trois_points(x_values, K_values, A_opt):
    """
    Trace les résultats de la courbe gamma et K(x) pour trois points de contrôle.
    """
    GAMMA1 = gamma(A_opt)
    GAMMA1 = np.array(GAMMA1)

    plt.figure(figsize=(10, 5))

    # Tracé de la courbe gamma
    plt.subplot(1, 2, 1)
    plt.plot(GAMMA1[:, 0], GAMMA1[:, 1], label='gamma')
    plt.title('Courbe gamma optimale')
    plt.xlabel('x')
    plt.ylabel('y')
    
    # points de controle
    points_controle = np.array(A_opt)
    plt.scatter(points_controle[:, 0], points_controle[:, 1], color='red', label='Points de contrôle')
    
    plt.legend()

    # Tracé de K(x)
    plt.subplot(1, 2, 2)
    plt.plot(x_values, K_values, label='K(x)')
    plt.title('Courbure K en fonction de x')
    plt.xlabel('x')
    plt.ylabel('K')
    plt.legend()

    plt.tight_layout()
    plt.show()

# Calcul et tracé des résultats
longueur_cible = 3.0  # Longueur de courbe souhaitée
x_values, K_values, A_opt = calculer_k_en_fonction_de_x_trois_points(longueur_cible)
tracer_resultats_trois_points(x_values, K_values, A_opt)

# Affichage des paramètres optimaux
print("A_opt correspondant au plus petit K :", A_opt)
print ("K minimum : ", K(A_opt))
