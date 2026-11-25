import os
import site
import sys


def is_virtual_environment():
    return (
        hasattr(sys, "real_prefix")
        or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix)
        or os.environ.get("VIRTUAL_ENV") is not None
    )


def main():
    in_venv = is_virtual_environment()
    python_path = sys.executable

    if not in_venv:
        print("MATRIX STATUS: You're still plugged in")
        print()
        print(f"Current Python: {python_path}")
        print("Virtual Environment: None detected")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate")
        print("Then run this program again.")

    else:
        venv_path = os.environ.get("VIRTUAL_ENV") or sys.prefix
        site_packages = (
            site.getsitepackages()[0]
            if hasattr(site, "getsitepackages")
            else os.path.join(
                venv_path,
                "lib",
                f"python{sys.version_info.major}.{sys.version_info.minor}",
                "site-packages",
            )
        )

        print("MATRIX STATUS: Welcome to the construct")
        print()
        print(f"Current Python: {python_path}")
        print(f"Virtual Environment: {os.path.basename(venv_path)}")
        print(f"Environment Path: {venv_path}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.\n")
        print("Package installation path:")
        print(site_packages)


if __name__ == "__main__":
    main()
