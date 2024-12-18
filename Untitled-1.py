# ORGANIZADOR DE ARCHIVOS
import os
import shutil

CATEGORIAS = {
    "Imágenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
    "Documentos": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Audios": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"],
    "Comprimidos": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Ejecutables": [".exe", ".msi", ".bat", ".sh", ".app"],
    "Códigos": [".py", ".js", ".java", ".html", ".css", ".cpp", ".c"],
    "Otros": []  
}

def organizar_archivos(directorio):
    for categoria in CATEGORIAS.keys():
        carpeta = os.path.join(directorio, categoria)
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

    for archivo in os.listdir(directorio):
        ruta_archivo = os.path.join(directorio, archivo)
        if os.path.isdir(ruta_archivo):
            continue
        _, extension = os.path.splitext(archivo)
        movido = False
        for categoria, extensiones in CATEGORIAS.items():
            if extension.lower() in extensiones:
                shutil.move(ruta_archivo, os.path.join(directorio, categoria, archivo))
                movido = True
                break

    if not movido:
        shutil.move(ruta_archivo, os.path.join(directorio, "Otros", archivo))

if __name__ == "__main__":
    carpeta_destino = input("Introduce la ruta de la carpeta que quieres organizar: ")
    if os.path.isdir(carpeta_destino):
        organizar_archivos(carpeta_destino)
        print(f"Archivos organizados en {carpeta_destino}")
    else:
        print("La ruta proporcionada no es válida.")