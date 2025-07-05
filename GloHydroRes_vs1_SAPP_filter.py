import pandas as pd

# Percorso del file di input
input_csv_path = r"C:\Users\Davide\Downloads\custom_powerplants_GloHydroRes.csv"

# Percorso del file di output
output_filtered_csv_path = r"C:\Users\Davide\Downloads\SAPP_custom_ppls_GloHydroRes.csv"

# Paesi da filtrare
countries_to_keep = [
    "Angola",
    "Democratic Republic of the Congo",
    "Namibia",
    "Mozambique",
    "eSwatini",
    "Tanzania",
    "Zambia",
    "Malawi",
    "Zimbabwe",
    "South Africa"
]

# Dizionario per convertire i nomi in sigle a due lettere
country_to_code = {
    "Angola": "AO",
    "Democratic Republic of the Congo": "CD",
    "Namibia": "NA",
    "Mozambique": "MZ",
    "eSwatini": "SZ",
    "Tanzania": "TZ",
    "Zambia": "ZM",
    "Malawi": "MW",
    "Zimbabwe": "ZW",
    "South Africa": "ZA"
}

# Righe da rimuovere
names_to_remove = [
    "Zongo I & II", "Tedzani I", "Tedzani II",
    "Tedzani III", "Kariba North Bank", "Kariba North Bank Extension", "Kariba South Bank", "Kariba South Bank Extension"
]

# Nuove righe da aggiungere
new_rows = [
    [4103, "Tedzani 1-3", "Hydro", "Run-Of-River", "PP", "Malawi", 92.7, "", "", 4.63, 18.69, "", 1973, 1973, 2073, -15.55625, 34.78675979, "", "10631", ""],
    [7751, "Kariba North Bank", "Hydro", "Reservoir", "PP", "Zambia", 1080.0, "", "", 92500.0, 92.0, "", 1959, 1959, 2059, -16.52166184, 28.7616715, "", "10734", ""],
    [7765, "Kariba South Bank", "Hydro", "Reservoir", "PP", "Zimbabwe", 1050.0, "", "", 92500.0, 92.57, "", 1959, 1959, 2059, -16.52166184, 28.7616715, "", "10773", ""]
]
# le nuove centrali sono una centrale con la somma delle capacità delle precedenti, lo stesso serbatoio (eccezione Kariba) e altezza come media pesata delle altezze precedenti

# Leggere il file CSV di input
df = pd.read_csv(input_csv_path)

# Filtrare i paesi specificati
filtered_df = df[df["Country"].isin(countries_to_keep)]

# Rimuovere le righe specifiche in base al nome della centrale
filtered_df = filtered_df[~filtered_df["Name"].isin(names_to_remove)]

# Modificare la colonna 'Country' con i codici
filtered_df["Country"] = filtered_df["Country"].replace(country_to_code)

# Modifiche specifiche alla colonna 'Technology'
filtered_df.loc[filtered_df["Name"].isin(["Ruzizi I", "Ruzizi II", "Nkula A", "Nkula B", "Lunsemfwa", "Lusiwasi", "Edwaleni"]), "Technology"] = "Run-Of-River"
filtered_df.loc[filtered_df["Name"].isin(["Ruacana", "Lower Kafue Gorge", "Nzilo", "Nseke", "Cambambe", "M'Sha", "Ncora", "Sol Plaatje", "Lower Kihansi"]), "Technology"] = "Reservoir"

# Creare un DataFrame per le nuove righe con la stessa struttura del file originale
new_rows_df = pd.DataFrame(new_rows, columns=df.columns)

# Modificare i nuovi paesi con i codici
new_rows_df["Country"] = new_rows_df["Country"].replace(country_to_code)

# Aggiungere le nuove righe
updated_df = pd.concat([filtered_df, new_rows_df], ignore_index=True)

# Scrivere il file aggiornato
updated_df.to_csv(output_filtered_csv_path, index=False)

print(f"File aggiornato salvato in: {output_filtered_csv_path}")




