import numpy as np
import matplotlib.pyplot as plt

# Create data for a simplified Mollier (h-s) diagram for water/steam
s = np.linspace(0.5, 8, 500)  # Entropy values (kJ/kg·K)
h_sat_liq = 100 * np.sqrt(s)  # Saturation liquid line (approximation)
h_sat_vap = h_sat_liq + 2000  # Saturation vapor line (approximation)
critical_point = (6.4, 2800)  # Approximate critical point (s, h)

# Generate isentropic processes (lines of constant entropy)
isentropic_s = [2, 4, 6]  # Example constant entropy values
isentropic_h = [200 + 300 * np.log(1 + s_val / s) for s_val in isentropic_s]

# Simulating inlet area effect (stochastic overlay for uncertainty)
inlet_areas = np.linspace(50, 150, 5)  # Inlet areas in cm²
uncertainty_band = np.random.uniform(-50, 50, size=(len(inlet_areas), len(s)))

# Plotting the Mollier Diagram
plt.figure(figsize=(12, 8))
plt.plot(s, h_sat_liq, label="Saturation Line (Liquid)", color="blue")
plt.plot(s, h_sat_vap, label="Saturation Line (Vapor)", color="orange")
plt.scatter(*critical_point, color="red", label="Critical Point", zorder=5)

# Add isentropic lines
for i, (s_val, h_line) in enumerate(zip(isentropic_s, isentropic_h)):
    plt.plot(s, h_line, '--', label=f"Isentropic Process s={s_val} kJ/kg·K")

# Overlay stochastic uncertainty for inlet area effect
for i, A_in in enumerate(inlet_areas):
    h_adjusted = h_sat_liq + uncertainty_band[i]
    plt.fill_between(s, h_sat_liq, h_adjusted, alpha=0.2, label=f"A_in={A_in} cm² (uncertainty)" if i == 0 else "")

# Labels and legend
plt.title("Mollier Diagram (h-s) with Parametric and Stochastic Analysis", fontsize=16)
plt.xlabel("Entropy, s (kJ/kg·K)", fontsize=14)
plt.ylabel("Enthalpy, h (kJ/kg)", fontsize=14)
plt.legend(fontsize=10)
plt.grid(alpha=0.5)

# Annotate insights based on our discussion
plt.annotate("Critical Point\nPhase Transition", critical_point,
             xytext=(6, 3000), arrowprops=dict(arrowstyle="->", color="red"),
             fontsize=12, color="red")

plt.annotate("Parametric Effect\n(Inlet Area)", (4, 1500),
             xytext=(2, 2000), arrowprops=dict(arrowstyle="->", color="black"),
             fontsize=12)

plt.show()
