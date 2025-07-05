READ_ME GloFAS-ERA5

Modified scripts are: build_renewable_profiles, add_electricity.
build_renewable_profiles has a flag (if/else) for the GloFAS method or the current PyPSA version alternative.
add_electricity has a flag that leads to using attach_hydro_GloFAS or attach_hydro (same as before) because inserting if/else inside the function (to avoid repeating it) is currently complicated.

Modifications are also necessary in the config (Config_SAPPGloFAS), which must be saved as config.yaml and Snakefile.

The custom_powerplants.csv was modified to already include GloHydroRes plants + PyPSA non-hydro plants. There are also Python scripts named 'GloHydroRes' used to convert the GloHydroRes Excel file into the custom-powerplants.csv format, followed by code that filters only SAPP plants (at that point, only non-hydro plants need to be added to obtain the final custom-powerplants.csv).