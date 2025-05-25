import pandas as pd
import random

states = ["Rajasthan", "Kerala", "West Bengal", "Tamil Nadu", "Odisha", "Bihar", "Maharashtra", "Telangana"]
arts = ["Madhubani", "Kathakali", "Warli", "Pattachitra", "Cheriyal Scroll"]

# Art Forms
art_data = []
for art in arts:
    art_data.append({
        "art_name": art,
        "state": random.choice(states),
        "description": f"A traditional folk art form from {random.choice(states)}",
        "origin_year": random.randint(1000, 1900),
        "is_unesco_listed": random.choice([True, False]),
        "image_url": f"https://example.com/images/ {art.lower().replace(' ', '_')}.jpg"
    })

pd.DataFrame(art_data).to_csv("data/art_forms.csv", index=False)

# Cultural Sites
sites = [
    ("Taj Mahal", "Uttar Pradesh", "UNESCO", 1983, 27.1767, 78.0422, 7000000),
    ("Konark Temple", "Odisha", "UNESCO", 1984, 19.8833, 86.1000, 1200000),
    ("Ajanta Caves", "Maharashtra", "UNESCO", 1983, 20.5526, 75.6820, 900000),
    ("Hampi", "Karnataka", "UNESCO", 1986, 15.3440, 76.4600, 1100000),
    ("Sun Temple", "Rajasthan", "Heritage", 0, 27.1767, 78.0422, 500000)
]

pd.DataFrame(sites, columns=["site_name", "state", "category", "year_included", "latitude", "longitude", "visitors_2023"]).to_csv("data/cultural_sites.csv", index=False)

print("🎨 Mock data generated successfully!")