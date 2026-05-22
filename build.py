import os
import sys
import subprocess

def main():
    print("=======================================================")
    print("  CONSTRUCTOR DE EJECUTABLE: DETECTIVE CASOS NUMERICOS")
    print("=======================================================")
    
    # 1. Instalar dependencias necesarias
    print("\n[1/3] Verificando e instalando dependencias (Pillow, PyInstaller)...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "pillow", "pyinstaller"], check=True)
        print("[OK] Dependencias listas.")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Error instalando dependencias mediante pip: {e}")
        print("Intentando continuar con los paquetes existentes...")
        
    # 2. Convertir el icono de JPG/PNG a ICO
    print("\n[2/3] Generando el archivo de icono de Windows (.ico)...")
    imagen_origen = None
    for ext in [os.path.join("EQ8", "Assets", "iconos", "juego_icono.jpg"), os.path.join("EQ8", "Assets", "iconos", "juego_icono.png")]:
        if os.path.exists(ext):
            imagen_origen = ext
            break
            
    ico_path = os.path.join("EQ8", "Assets", "iconos", "juego_icono.ico")
    
    if imagen_origen:
        try:
            from PIL import Image
            img = Image.open(imagen_origen)
            # Guardamos con múltiples tamaños estándar para que se vea nítido en cualquier resolución de Windows
            img.save(ico_path, format='ICO', sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)])
            print(f"[OK] Icono personalizado generado con exito desde '{imagen_origen}' en: {ico_path}!")
        except Exception as e:
            print(f"[ERROR] Error al convertir el icono: {e}")
            print("Se continuara con la compilacion sin icono personalizado.")
    else:
        print("[WARN] Advertencia: No se encontro ningun archivo de imagen ('juego_icono.jpg' o 'juego_icono.png') en 'EQ8/Assets/iconos/'.")
        print("Se continuara con la compilacion sin icono personalizado.")

    # 3. Compilar usando PyInstaller
    print("\n[3/3] Compilando el ejecutable con PyInstaller...")
    try:
        cmd = [sys.executable, "-m", "PyInstaller", "--clean", "detective.spec"]
        subprocess.run(cmd, check=True)
        
        print("\n=======================================================")
        print("  ¡PROCESO COMPLETADO EXITOSAMENTE!")
        print("=======================================================")
        print("Tu juego empaquetado está listo en la carpeta 'dist':")
        print("Ruta: c:\\Users\\mauri\\EQ8-PROYECTO-METNUM-1\\dist\\Detective - Casos Numéricos.exe")
        print("\n¡Ya puedes ejecutarlo, probarlo y compartirlo con otros!")
        print("=======================================================")
    except subprocess.CalledProcessError as e:
        print(f"\n[ERROR] Error durante la compilacion con PyInstaller: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
