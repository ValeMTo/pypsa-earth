import pandas as pd

# Percorso del file di input
input_file_path = r"C:\Users\Davide\Downloads\GloHydroRes_vs1\GloHydroRes_vs1.csv"

# Percorso del file di output
output_csv_path = r"C:\Users\Davide\Downloads\custom_powerplants_GloHydroRes.csv"

# Leggere il file CSV di input
GloHydroRes = pd.read_csv(input_file_path)

GloHydroRes["name"] = GloHydroRes["name"].str.strip()

# Mappatura di "plant_type" per la colonna "Technology"
technology_mapping = {
    "ROR": "Run-Of-River",
    "STO": "Reservoir",
    "PS": "Pumped Storage",
    "Canal": "Run-Of-River"
}

# Preparazione delle righe per il file di output
rows = []
for index, row in GloHydroRes.iterrows():
    name = row["name"]
    fueltype = "Hydro"
    technology = technology_mapping.get(row["plant_type"], "") 
    set_type = "Store" if row["plant_type"] == "PS" else "PP"
    country = row["country"]
    capacity = row["capacity_mw"]
    efficiency = ""
    duration = ""
    volume_Mm3 = row["res_vol_km3"] * 1000
    dam_height_m = row["head_m"]
    storage_capacity_mwh = ""

    # Gestione delle date
    if pd.notna(row["year"]):  # Controlla se il valore è valido
        date_in = int(row["year"])
        date_retrofit = date_in
        date_out = date_in + 100
    else:
        date_in = ""
        date_retrofit = ""
        date_out = ""

    lat = row["plant_lat"]
    lon = row["plant_lon"]
    eic = ""
    project_id = row["plant_source_id"]
    bus = ""

    # Creazione della riga di output
    rows.append([
        index + 1, name, fueltype, technology, set_type, country, capacity,
        efficiency, duration, volume_Mm3, dam_height_m, storage_capacity_mwh,
        date_in, date_retrofit, date_out, lat, lon, eic, project_id, bus
    ])

# Colonne per il file di output
columns = [
    "", "Name", "Fueltype", "Technology", "Set", "Country", "Capacity",
    "Efficiency", "Duration", "Volume_Mm3", "DamHeight_m",
    "StorageCapacity_MWh", "DateIn", "DateRetrofit", "DateOut",
    "lat", "lon", "EIC", "projectID", "bus"
]

# Creazione del DataFrame di output
output_df = pd.DataFrame(rows, columns=columns)

# Scrittura del file CSV di output
output_df.to_csv(output_csv_path, index=False)


