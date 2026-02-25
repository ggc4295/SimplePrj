# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec file for SimplePrj
# Build command: pyinstaller simpleprj.spec

import os

block_cipher = None

a = Analysis(
    ['src/main.py'],          # Entry point
    pathex=['src'],            # Add src/ to sys.path so imports work
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='simpleprj',           # Output executable name
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,                   # Use UPX compression if available
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,               # Console (CLI) application
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,                  # Set to an .ico file path if you have an icon
)
