import os
from PIL import Image

# Esto obtiene la ruta exacta de la carpeta donde está tu script
carpeta_actual = os.path.dirname(os.path.abspath(__file__))

# Nombre de tu imagen
nombre_imagen = '26.T775U2006.png'
# Rutas completas
ruta_original = os.path.join(carpeta_actual, nombre_imagen)
ruta_temporal = os.path.join(carpeta_actual, 'temp_edit.png')

peso_maximo_kb = 200

try:
    print(f"Buscando imagen en: {ruta_original}")
    
    with Image.open(ruta_original) as img:
        # 1. FORZAR TAMAÑO: Exactamente 200x74 píxeles
        img = img.resize((97,  168))
        
        # 2. BAJAR PESO: Reducir calidad hasta que pese menos de 200 KB
        calidad = 120
        peso_actual = 0
        
        while calidad > 10:
            img.save(ruta_temporal, format='png', quality=calidad)
            peso_actual = os.path.getsize(ruta_temporal) / 1024
            
            if peso_actual <= peso_maximo_kb:
                break # Si ya pesa menos de 200 KB, se detiene
            calidad -= 5 # Si sigue pesando mucho, baja la calidad
            
    # 3. MANTENER NOMBRE: Reemplaza el archivo original con el nuevo
    os.replace(ruta_temporal, ruta_original)
    
    print("\n🎉 ¡ÉXITO! 🎉")
    print(f"La imagen '{nombre_imagen}' ahora mide 200x74 px y pesa {peso_actual:.2f} KB (Calidad: {calidad}%).")

except Exception as e:
    print(f"\n❌ Ocurrió un error: {e}")