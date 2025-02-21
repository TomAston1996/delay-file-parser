"""
build script

Author: Tom Aston
"""

import subprocess
import shutil
import os

# Configuration
APP_NAME = "DelayFileParser"
ENTRY_FILE = "DelayFileParser.py"
BUILD_DIR = "dist"


def clean() -> None:
    """Remove previous build artifacts."""
    if os.path.exists(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)
    for folder in ["build", "__pycache__"]:
        if os.path.exists(folder):
            shutil.rmtree(folder)
    for file in [f"{APP_NAME}.spec"]:
        if os.path.exists(file):
            os.remove(file)


def build() -> None:
    """Run PyInstaller to create an executable."""
    cmd = ["uv", "run", "pyinstaller", "--onefile", "-w", "--name", APP_NAME, ENTRY_FILE]
    subprocess.run(cmd, check=True)


def main() -> None:
    print("🚀 Cleaning previous builds...")
    clean()
    print("🔧 Building the executable...")
    build()
    print(f"✅ Build complete! Executable is in the '{BUILD_DIR}' folder.")


if __name__ == "__main__":
    main()
