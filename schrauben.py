## Nur Referenz wie das Datenset generiert ist.

import pandas as pd
import json
from random import randint

dates = pd.date_range(start='2023-06-01', end='2023-06-30')

data = []
for date in dates:
    for schraube, preis in [("Sechskantschraube", 1.50), ("Holzschraube", 1.20), ("Maschinenschraube", 2.00), ("Universalschraube", 1.75), ("Senkkopfschraube", 1.25)]:
        for hersteller in ["Wuerth", "HECO", "SWG"]:
            data.append({
                "Hersteller": hersteller,
                "Schraube": schraube,
                "Preis": preis,
                "VerkaufteMenge": randint(500,1500),  # VerkaufteMenge is random between 500 and 1500
                "Datum": str(date.date())
            })

# Write JSON data to file
with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
