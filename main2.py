# a friendly and healthy code that builds up intuition for the main.py :)
#coolprop is used to compute thermodynamic properties for a given fluid
#mollier diagram is a enthalp vs entropy
import numpy as np
import matplotlib.pyplot as plt
from CoolProp.CoolProp import PropsSI

# Function to calculate saturation lines
def calculate_saturation_lines(fluid):
    T_min = PropsSI("T_triple", fluid)  # Triple point temperature
    T_crit = PropsSI("T_critical", fluid)  # Critical temperature
    T_vals = np.linspace(T_min, T_crit, 500)  # Temperature range
    
    h_liquid = [PropsSI("H", "T", T, "Q", 0, fluid) / 1000 for T in T_vals]
    h_vapor = [PropsSI("H", "T", T, "Q", 1, fluid) / 1000 for T in T_vals]
    s_liquid = [PropsSI("S", "T", T, "Q", 0, fluid) / 1000 for T in T_vals]
    s_vapor = [PropsSI("S", "T", T, "Q", 1, fluid) / 1000 for T in T_vals]
    
    return T_vals, h_liquid, h_vapor, s_liquid, s_vapor

# Function to plot the Mollier diagram
def plot_mollier_diagram(fluid="Water"):
    # Calculate saturation curves
    T_vals, h_liquid, h_vapor, s_liquid, s_vapor = calculate_saturation_lines(fluid)
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    
    # Plot saturation lines
    plt.plot(s_liquid, h_liquid, label="Saturated Liquid", color="blue")
    plt.plot(s_vapor, h_vapor, label="Saturated Vapor", color="red")
    
    # Annotate the critical point
    T_crit = PropsSI("T_critical", fluid)
    h_crit = PropsSI("H", "T", T_crit, "Q", 1, fluid) / 1000
    s_crit = PropsSI("S", "T", T_crit, "Q", 1, fluid) / 1000
    plt.scatter(s_crit, h_crit, color="black", label="Critical Point")
    plt.text(s_crit, h_crit, "Critical Point", fontsize=10)
    
    # Add labels, legend, and grid
    plt.xlabel("Entropy, s [kJ/kg·K]")
    plt.ylabel("Enthalpy, h [kJ/kg]")
    plt.title(f"Mollier Diagram for {fluid}")
    plt.legend()
    plt.grid()
    
    # Show the plot
    plt.show()

# Plot the Mollier diagram for water
plot_mollier_diagram("Water")
