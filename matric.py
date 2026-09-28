import numpy as np

def main():

    m1 = int(input("Enter value for m1: "))
    k1 = int(input("Enter value for k1: "))
    k2 = int(input("Enter value for k2: "))


    i = k1 + k2 - m1 * (w**2)
    j = -k2
    k = k2
    l = k2 - (w**2)

    a = np.array([[i,j],
                  [k,l]])


    m = np.linalg.det(a)
    print(f"Determinant: {m}")



if __name__ == "__main__":
    main()

