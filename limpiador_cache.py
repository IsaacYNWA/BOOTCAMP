import os
import shutil
import subprocess 
import time #Realizar pausas

# Limpiar contenido de una carpeta, lo primero para ejecutar en las diferentes funciones del limpiador.
def limpiar_carpeta(nombre_carpeta, ruta_carpeta):
    print(f"\n--- Limpiando {nombre_carpeta}... ---")
    if not os.path.exists(ruta_carpeta):
        print(f"La carpeta {nombre_carpeta} no existe")
        return

    archivos_eliminados = 0
    carpetas_eliminadas = 0

    for raiz, dirs, ficheros in os.walk(ruta_carpeta, topdown=False):
        for fichero in ficheros:
           ruta_fichero = os.path.join(raiz, fichero)
            try:
               os.remove(ruta_fichero)
               archivos_eliminados += 1
               print(f"Archivo eliminado: {ruta_fichero}")
            except PermissionError:
               print(f"Permiso denegado para eliminar el archivo: {ruta_fichero} (probablemente en uso).")
            except Exception as e:
               print(f"Error eliminando el archivo {ruta_fichero}: {e}")
        for dir in dirs:
           ruta_dir = os.path.join(raiz, dir)
            try:
               os.rmdir(ruta_dir)
               carpetas_eliminadas += 1
            except OSError as e:
               print(f"No se pudo eliminar la carpeta {ruta_dir}: {e}")
            except Exception as e:
               print(f"Error eliminando la carpeta {ruta_dir}: {e} ")

    print(f"Limpieza de {nombre_carpeta} completada.")
    print(f"Resultados: {archivos_eliminados} archivos y {carpetas_eliminadas} carpetas eliminadas.")


           