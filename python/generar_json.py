from pathlib import Path
import pandas as pd
import json

# Carpetas del proyecto
BASE = Path(__file__).resolve().parent
EXCEL = BASE.parent / "excel" / "Sistema_ELO_Club_Completo_Nuevo.xlsm"
DATA = BASE.parent / "data"

# Crear carpeta data si no existe
DATA.mkdir(exist_ok=True)

# Abrir Excel
excel = pd.ExcelFile(EXCEL)

# Función para exportar un ranking
def exportar(hoja, archivo_json):
    df = pd.read_excel(excel, sheet_name=hoja)

    # Eliminar filas vacías
    df = df.dropna()

    # Convertir a lista de diccionarios
    datos = df.to_dict(orient="records")

    # Guardar JSON
    with open(DATA / archivo_json, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)

    print(f"✅ {archivo_json} generado ({len(datos)} jugadores)")

exportar("Ranking Clasico", "clasico.json")
exportar("Ranking Blitz", "blitz.json")
exportar("Ranking Rapid", "rapid.json")

print("\nProceso terminado.")