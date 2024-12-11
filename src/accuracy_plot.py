import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from matplotlib.patches import Ellipse, Circle


def plot_1(ell_a_priori: float, ell_b_priori: float, ell_omega_priori: float, ell_a_posteriori: float, ell_b_posteriori: float, ell_omega_posteriori: float, sE: float, sN: float, FS_E: float = 0., FS_N: float = 0.) -> None:
    fig, ax = plt.subplots(figsize=(6, 6))

    # A-priori-Ellipse
    ellipse_priori = Ellipse(xy=(FS_E, FS_N), width=ell_a_priori / 1000, height=ell_b_priori / 1000,
                            angle=-ell_omega_priori * 0.9 + 90, fill=False, edgecolor='blue', label='A-priori Ellipse')
    ax.add_patch(ellipse_priori)

    # A-posteriori-Ellipse
    ellipse_posteriori = Ellipse(xy=(FS_E, FS_N), width=ell_a_posteriori / 1000 * 2, height=ell_b_posteriori / 1000 * 2,
                                angle=-ell_omega_posteriori * 0.9 + 90, fill=False, edgecolor='red', label='A-posteriori Ellipse')
    ax.add_patch(ellipse_posteriori)

    # Vertikale und horizontale Linien für die Standardabweichungen
    ax.axvline(x=FS_E - sE / 1000, color='green', linestyle='--')
    ax.axvline(x=FS_E + sE / 1000, color='green', linestyle='--')
    ax.axhline(y=FS_N - sN / 1000, color='green', linestyle='--')
    ax.axhline(y=FS_N + sN / 1000, color='green', linestyle='--')

    # Achsenbegrenzungen
    spacing = 2.5 * np.sqrt(sE**2 + sN**2) / 1000  # Abstand in Metern
    ax.set_xlim(FS_E - spacing, FS_E + spacing)
    ax.set_ylim(FS_N - spacing, FS_N + spacing)

    # Normalverteilung für Ost
    x_e = np.linspace(FS_E - 3 * sE / 1000, FS_E + 3 * sE / 1000, 500)  # Bereich für die Normalverteilung
    y_e = norm.pdf(x_e, FS_E, sE / 1000)  # Wahrscheinlichkeitsdichtefunktion (PDF) der Normalverteilung
    y_e = y_e / 2000000 + FS_N + sN / 1000 # Transformation in den Bildbereich

    # Normalverteilung Ost plotten
    ax.plot(x_e, y_e, 'purple', label='Normalverteilung Ost')

    # Normalverteilung für Nord
    y_n = np.linspace(FS_N - 3 * sN / 1000, FS_N + 3 * sN / 1000, 500)  # Bereich für die Normalverteilung
    x_n = norm.pdf(y_n, FS_N, sN / 1000)  # Wahrscheinlichkeitsdichtefunktion (PDF) der Normalverteilung
    x_n = x_n / 2000000 + FS_E + sE / 1000 # Transformation in den Bildbereich

    # Normalverteilung Nord plotten
    ax.plot(x_n, y_n, 'pink', label='Normalverteilung Nord')

    # Legenden hinzufügen
    ax.legend(loc='upper left')

    plt.show()
    
def plot_2(radius_priori: float, radius_posteriori: float, FS_E: float = 0., FS_N:float = 0.) -> None:
    # Darstellung
    fig, ax = plt.subplots(figsize=(6, 6))

    # A-priori-Kreis
    circle_priori = Circle((FS_E, FS_N), radius=radius_priori / 1000, fill=False, edgecolor='#00ccff', label='A-priori Kreis')
    ax.add_patch(circle_priori)

    # A-posteriori-Kreis
    circle_posteriori = Circle((FS_E, FS_N), radius=radius_posteriori / 1000, fill=False, edgecolor='#ff9999', label='A-posteriori Kreis')
    ax.add_patch(circle_posteriori)
    
    # Achsenbegrenzungen basierend auf dem größeren Radius
    max_radius = max(radius_priori, radius_posteriori) / 1000
    ax.set_xlim(FS_E - max_radius * 1.2, FS_E + max_radius * 1.2)
    ax.set_ylim(FS_N - max_radius * 1.2, FS_N + max_radius * 1.2)

    # Legende hinzufügen
    ax.legend()

    plt.gca().set_aspect('equal', adjustable='box')  # gleiche Achsenskalierung für Kreise
    plt.show()
    
def plot_3(ell_a_posteriori: float, ell_b_posteriori: float, ell_omega_posteriori: float, a95: float, b95: float, omega95: float, sE: float, sN: float, FS_E: float = 0., FS_N: float = 0.) -> None:
    fig, ax = plt.subplots(figsize=(6, 6))
    # A-posteriori-Ellipse
    ellipse_posteriori = Ellipse(xy=(FS_E, FS_N), width=ell_a_posteriori / 1000 * 2, height=ell_b_posteriori / 1000 * 2,
                                angle=-ell_omega_posteriori * 0.9 + 90, fill=False, edgecolor='red', label='A-posteriori Ellipse')
    ax.add_patch(ellipse_posteriori)

    # A-posteriori-Ellipse 95
    ellipse_posteriori95 = Ellipse(xy=(FS_E, FS_N), width=a95 / 1000 * 2, height=b95 / 1000 * 2,
                                angle=-omega95 * 0.9 + 90, fill=False, edgecolor='#cc0000', label='A-posteriori95 Ellipse')
    ax.add_patch(ellipse_posteriori95)


    # Achsenbegrenzungen
    spacing = 4 * np.sqrt(sE**2 + sN**2) / 1000  # Abstand in Metern
    ax.set_xlim(FS_E - spacing, FS_E + spacing)
    ax.set_ylim(FS_N - spacing, FS_N + spacing)

    ax.legend()
    plt.show()