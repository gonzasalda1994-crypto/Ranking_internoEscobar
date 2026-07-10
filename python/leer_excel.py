from pathlib import Path
import pandas as pd

# Ruta del Excel
BASE = Path(__file__).resolve().parent
archivo = BASE.parent / "excel" / "Sistema_ELO_Club_Completo_Nuevo.xlsm"

# Abrir Excel
excel = pd.ExcelFile(archivo)

# Leer Ranking Clasico
df = pd.read_excel(excel, sheet_name="Ranking Clasico")

print(df)