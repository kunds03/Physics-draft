import matlab.engine

def main():

    print("Starting MATLAB...")
    eng = matlab.engine.start_matlab()

    # Get values from user
    m1 = float(input("Enter value for m1: "))
    m2 = float(input("Enter value for m2: "))
    k1 = float(input("Enter value for k1: "))
    k2 = float(input("Enter value for k2: "))

    # Send values to MATLAB
    eng.workspace["m1"] = m1
    eng.workspace["m2"] = m2
    eng.workspace["k1"] = k1
    eng.workspace["k2"] = k2

    # Create symbolic variable
    eng.eval("syms w", nargout=0)

    # Create matrix
    eng.eval("""
    A = [k1 + k2 - m1*w^2, -k2;
         -k2,                k2 - m2*w^2];
    """, nargout=0)

    print("\nMatrix:")
    eng.eval("disp(A)", nargout=0)

    # Determinant
    eng.eval("detA = det(A);", nargout=0)
    print("\nDeterminant:")
    eng.eval("disp(detA)", nargout=0)

    # Solve
    eng.eval("omega = solve(detA == 0, w);", nargout=0)
    print("\nOmega values:")
    eng.eval("disp(omega)", nargout=0)

    eng.quit()


if __name__ == "__main__":
    main()
