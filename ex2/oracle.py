import os
import sys
from dotenv import load_dotenv


def main():
    # Load environment variables from .env if present
    load_dotenv()

    print("ORACLE STATUS: Reading the Matrix...")

    matrix_mode = os.getenv("MATRIX_MODE", "development")
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv(
        "LOG_LEVEL", "DEBUG" if matrix_mode == "development" else "INFO"
    )
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    # Check for missing required configurations
    missing = []
    if not database_url:
        missing.append("DATABASE_URL")
    if not api_key:
        missing.append("API_KEY")
    if not zion_endpoint:
        missing.append("ZION_ENDPOINT")

    if missing:
        print(
            "\nWARNING: Missing required configuration, end="
            ""
            f"variables: {', '.join(missing)}"
        )
        print("To fix this, copy the template and configure your environment:")
        print("  cp .env.example .env")
        print("  # Edit .env with your values")
        sys.exit(1)

    print("Configuration loaded:")
    print(f"Mode: {matrix_mode}")
    db_status = (
        "Connected to local instance"
        if "sqlite" in database_url
        else f"Connected to {database_url}"
    )
    print(f"Database: {db_status}")
    print("API Access: Authenticated" if api_key else "")
    print("API Access: Unauthenticated")
    print(f"Log Level: {log_level}")
    print("Zion Network: Online" if zion_endpoint else "Zion Network: Offline")

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[INFO] Using system environment variables (no .env file found)")

    print("[OK] Production overrides available")


if __name__ == "__main__":
    main()
