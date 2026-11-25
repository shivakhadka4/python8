import importlib.util
import sys

PACKAGES = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready",
    "requests": "Network access ready",
}


def main():
    print("LOADING STATUS: Loading programs...")
    print()
    print("Checking dependencies:")

    missing = False
    for pkg, desc in PACKAGES.items():
        if importlib.util.find_spec(pkg):
            ver = getattr(__import__(pkg), "__version__", "unknown")
            print(f"[OK] {pkg} ({ver}) - {desc}")
        else:
            print(f"[MISSING] {pkg} - Not found")
            if pkg != "requests":
                missing = True

    if missing:
        print("\nWARNING: Core dependencies missing!")
        print("pip: pip install -r requirements.txt")
        print("Poetry: poetry install && poetry run python loading.py")
        sys.exit(1)

    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    print()
    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")
    df = pd.DataFrame(np.random.randn(1000, 2) * 10 + 50, columns=["X", "Y"])

    print("Generating visualization...")
    plt.plot(df["X"].values[:100], color="green")
    plt.title("Matrix Code Stream Analysis")
    plt.savefig("matrix_analysis.png")
    plt.close()
    print()
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
