import numpy as np

def main():

    m1 = float(input("Enter value for m1: "))
    m2 = float(input("Enter value for m2: "))
    k1 = float(input("Enter value for k1: "))
    k2 = float(input("Enter value for k2: "))

    # Print matrix
    print("\nMatrix:")
    print(f"[[{k1} + {k2} - {m1}w^2, {-k2}],")
    print(f" [-{k2}, {k2} - {m2}w^2]]")

    # Formula
    b = (k1 + k2) / m1 + k2 / m2
    c = (k1 * k2) / (m1 * m2)

    # Solve for w^2
    w_squared_1 = (b + np.sqrt(b**2 - 4*c)) / 2
    w_squared_2 = (b - np.sqrt(b**2 - 4*c)) / 2

    # Solve for w
    omega1 = np.sqrt(w_squared_1)
    omega2 = np.sqrt(w_squared_2)

    print(f"\nOmega 1 = {omega1:.2f} rad/sec")
    print(f"Omega 2 = {omega2:.2f} rad/sec")


if __name__ == "__main__":
    main()