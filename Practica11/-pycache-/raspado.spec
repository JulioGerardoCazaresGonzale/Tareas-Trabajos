# -*- modo: python ; codificación: utf-8 -*-


block_cipher = Ninguno


a = Análisis([«scraping.py»),
             pathex=[],
             binarios=[],
             datos=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excluye=[],
             win_no_prefer_redirects=Falso,
             win_private_assemblies=Falso,
             cifrado=block_cipher,
             noarchive=Falso)
pyz = PYZ(a . puro, a. zipped_data,
             cifrado=block_cipher)

exe = EXE(pyz,
          a. guiones, 
          [],
          exclude_binaries=Verdadero,
          nombre='raspado',
          debug=False,
          bootloader_ignore_signals=Falso,
          tira=Falso,
          upx=Verdadero,
          consola=Verdadero,
          disable_windowed_traceback=Falso,
          target_arch=Ninguno,
          codesign_identity=Ninguno,
          entitlements_file=Ninguno )
coll = COLLECT(exe,
               a. binarios,
               a. zipfiles,
               a. datos, 
               tira=Falso,
               upx=Verdadero,
               upx_exclude=[],
               nombre='raspado')
