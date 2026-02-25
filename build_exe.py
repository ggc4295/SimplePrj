"""
Build script for creating SimplePrj executable with PyInstaller.

Usage:
    python build_exe.py            # Standard build
    python build_exe.py --clean    # Clean previous build artifacts first
"""

import os
import shutil
import subprocess
import sys


def clean_build_dirs():
    """Remove previous build artifacts."""
    dirs_to_clean = ["build", "dist"]
    for d in dirs_to_clean:
        if os.path.exists(d):
            print(f"Removing {d}/...")
            shutil.rmtree(d)


def build_exe():
    """Run PyInstaller to build the executable."""
    print("Building SimplePrj executable with PyInstaller...")
    print("-" * 50)

    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--clean",           # Remove cached files before building
        "simpleprj.spec",    # Use the spec file
    ]

    result = subprocess.run(cmd, check=False)

    if result.returncode == 0:
        exe_path = os.path.join("dist", "simpleprj.exe")
        if os.path.exists(exe_path):
            size_mb = os.path.getsize(exe_path) / (1024 * 1024)
            print("-" * 50)
            print(f"Build successful!")
            print(f"Executable: {exe_path} ({size_mb:.1f} MB)")
        else:
            # On non-Windows platforms the binary has no extension
            print("Build successful! Check the dist/ directory.")
    else:
        print("-" * 50)
        print(f"Build FAILED with exit code {result.returncode}")
        sys.exit(result.returncode)


if __name__ == "__main__":
    if "--clean" in sys.argv:
        clean_build_dirs()

    build_exe()
