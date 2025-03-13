import csv

def organizar_canciones(archivo_entrada, archivo_salida):
    canciones = []
    
    with open(archivo_entrada, 'r', encoding='utf-8') as file:
        lineas = file.readlines()
        
        for i in range(0, len(lineas), 4):  # Leer en bloques de 4 líneas
            if i + 3 < len(lineas):  # Asegura que haya 4 líneas disponibles
                titulo = lineas[i].strip()
                artista = lineas[i + 1].strip()
                album = lineas[i + 2].strip()
                duracion = lineas[i + 3].strip()
                canciones.append([titulo, artista, album, duracion])
    
    # Guardar en CSV
    with open(archivo_salida, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Título", "Artista", "Álbum", "Duración"])  # Encabezado
        writer.writerows(canciones)
    
    print(f"Archivo organizado y guardado en {archivo_salida}")

# Uso del script
archivo_entrada = "canciones"  # Reemplázalo con el nombre de tu archivo
archivo_salida = "canciones_organizadas.csv"
organizar_canciones(archivo_entrada, archivo_salida)
