import numpy as np
import matplotlib.pyplot as plt


# Build the Matrices for M and K
def matrices(m1, m2, k1, k2, k3):
    M = np.array([[m1, 0],
                  [0, m2]])

    K = np.array([[k1 + k2, -k2],
                  [-k2, k2 + k3]])

    return M, K


# Get Natural frequencies and mode shape
def solveModes(M, K):

    # Compute M^(-1) K --> linalg is for matrix opperations, @ is for matrix multiplication
    MK = np.linalg.inv(M) @ K

    # eignvals - natural frequencies and eigvecs - mode shape
    eigvals, eigvecs = np.linalg.eig(MK)

    # rounding to make sure there are no errors
    eigvals = np.real_if_close(eigvals, tol=1e5)
    eigvecs = np.real_if_close(eigvecs, tol=1e5)

    # Natural frequencies is an array
    omega = np.sqrt(eigvals)

    # Sorts the omega array from lowest to highest frequency and reorders omega
    idx = np.argsort(omega)
    omega = omega[idx]
    eigvecs = eigvecs[:, idx]

    omega1, omega2 = omega

    # Normalize mode shapes
    phi1 = eigvecs[:, 0] / np.max(np.abs(eigvecs[:, 0]))
    phi2 = eigvecs[:, 1] / np.max(np.abs(eigvecs[:, 1]))

    return omega1, omega2, phi1, phi2


# ------------------------------------------------------------
# Function: functions(...)
# Purpose:  Compute modal amplitudes and full time response.
# ------------------------------------------------------------
def functions(omega1, omega2, phi1, phi2, x10, x20):

    # Initial displacement vector
    X0 = np.array([x10, x20])

    # Mode shape matrix
    Phi = np.column_stack((phi1, phi2))

    # Solve for amplitudes A1 and A2
    A1, A2 = np.linalg.solve(Phi, X0)

    # Time
    t = np.linspace(0, 50, 5000)


    # Displacement
    x1 = A1 * phi1[0] * np.cos(omega1 * t) + A2 * phi2[0] * np.cos(omega2 * t)
    x2 = A1 * phi1[1] * np.cos(omega1 * t) + A2 * phi2[1] * np.cos(omega2 * t)


    # Velocity
    v1 = -A1 * phi1[0] * omega1 * np.sin(omega1 * t) - A2 * phi2[0] * omega2 * np.sin(omega2 * t)
    v2 = -A1 * phi1[1] * omega1 * np.sin(omega1 * t) - A2 * phi2[1] * omega2 * np.sin(omega2 * t)


    # Acceleration
    a1 = -A1 * phi1[0] * omega1**2 * np.cos(omega1 * t) - A2 * phi2[0] * omega2**2 * np.cos(omega2 * t)
    a2 = -A1 * phi1[1] * omega1**2 * np.cos(omega1 * t) - A2 * phi2[1] * omega2**2 * np.cos(omega2 * t)

    return t, x1, x2, v1, v2, a1, a2



def graph(t, x1, x2, v1, v2, a1, a2):

    plt.figure(figsize=(12, 10))

    # Displacement of x1 and x2
    plt.subplot(3, 2, 1)
    plt.plot(t, x1)
    plt.title("Displacement x1(t)")
    plt.xlabel("Time")
    plt.ylabel("x1")
    plt.grid(True)

    plt.subplot(3, 2, 2)
    plt.plot(t, x2)
    plt.title("Displacement x2(t)")
    plt.xlabel("Time")
    plt.ylabel("x2")
    plt.grid(True)

    # Velocity of v1 and v2
    plt.subplot(3, 2, 3)
    plt.plot(t, v1)
    plt.title("Velocity v1(t)")
    plt.xlabel("Time")
    plt.ylabel("v1")
    plt.grid(True)

    plt.subplot(3, 2, 4)
    plt.plot(t, v2)
    plt.title("Velocity v2(t)")
    plt.xlabel("Time")
    plt.ylabel("v2")
    plt.grid(True)

    # Acceleration of a1 and a2
    plt.subplot(3, 2, 5)
    plt.plot(t, a1)
    plt.title("Acceleration a1(t)")
    plt.xlabel("Time")
    plt.ylabel("a1")
    plt.grid(True)

    plt.subplot(3, 2, 6)
    plt.plot(t, a2)
    plt.title("Acceleration a2(t)")
    plt.xlabel("Time")
    plt.ylabel("a2")
    plt.grid(True)

    plt.tight_layout()
    plt.show()



def main():
    print("\n 2 DOF FREE VIBRATION SYSTEM \n")

    # Mass inputs
    while True:
        try:
            m1 = float(input("Enter mass m1: "))
            if m1 <= 0:
                print("Mass must be positive.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a NUMBER.")

    while True:
        try:
            m2 = float(input("Enter mass m2: "))
            if m2 <= 0:
                print("Mass must be positive.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a NUMBER.")

    # Spring constants
    while True:
        try:
            k1 = float(input("Enter spring constant k1: "))
            if k1 <= 0:
                print("Spring constant must be positive.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a NUMBER.")

    while True:
        try:
            k2 = float(input("Enter spring constant k2: "))
            if k2 <= 0:
                print("Spring constant must be positive.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a NUMBER.")

    while True:
        try:
            k3 = float(input("Enter spring constant k3: "))
            if k3 <= 0:
                print("Spring constant must be positive.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a NUMBER.")

    # Initial displacements
    while True:
        try:
            x10 = float(input("Initial displacement x1(0): "))
            break
        except ValueError:
            print("Invalid input. Enter a NUMBER.")

    while True:
        try:
            x20 = float(input("Initial displacement x2(0): "))
            break
        except ValueError:
            print("Invalid input. Enter a NUMBER.")


    # Make matrices
    M, K = matrices(m1, m2, k1, k2, k3)

    # Solve modes
    omega1, omega2, phi1, phi2 = solveModes(M, K)

    print("\nNatural Frequencies:")
    print(f"omega1 (w1) = {round(omega1, 4)} rad/s")
    print(f"omega2 (w2) = {round(omega2, 4)} rad/s")

    print("\nMode Shapes:")
    print("Mode 1:", phi1)
    print("Mode 2:", phi2)

    # Create functions
    t, x1, x2, v1, v2, a1, a2 = functions(
        omega1, omega2, phi1, phi2, x10, x20
    )

    # Graph
    graph(t, x1, x2, v1, v2, a1, a2)


if __name__ == "__main__":
    main()
