import json
import os

states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", 
    "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", 
    "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", 
    "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", 
    "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", 
    "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", 
    "Wisconsin", "Wyoming"
]

images = [
    "https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=200&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=200&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=200&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1598550874175-4d0ef436c909?q=80&w=200&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1556157382-97eda2d62296?q=80&w=200&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=200&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1577415124269-b9140d420bf3?q=80&w=200&auto=format&fit=crop"
]

# Generate realistic prominent firm names per state
attorneys = []
for idx, state in enumerate(states):
    # Attorney 1
    firm_name_1 = f"Law Offices of Smith & {state[:4].capitalize()}"
    attorneys.append({
        "name": f"James {state[:3].capitalize()}son",
        "firm": firm_name_1,
        "location": f"Capital City, {state}",
        "state": state,
        "rating": "4.9",
        "reviews": 150 + (idx * 7) % 300,
        "image": images[idx % len(images)],
        "specialties": ["Divorce", "Child Custody", "Alimony"],
        "verified": True,
        "email": f"consult@{firm_name_1.replace(' ', '').replace('&','').lower()}.com",
        "phone": f"(555) {100+idx}-0101",
        "bio": f"Dedicated family law practice in {state} with over 20 years of experience handling complex divorce and custody cases."
    })
    # Attorney 2
    firm_name_2 = f"{state} Family Legal Group"
    attorneys.append({
        "name": f"Sarah {state[-3:].capitalize()}man",
        "firm": firm_name_2,
        "location": f"Major City, {state}",
        "state": state,
        "rating": "4.7",
        "reviews": 85 + (idx * 13) % 250,
        "image": images[(idx + 3) % len(images)],
        "specialties": ["Mediation", "Property Division", "Paternity"],
        "verified": False,
        "email": f"info@{firm_name_2.replace(' ', '').lower()}.com",
        "phone": f"(555) {200+idx}-0202",
        "bio": f"Focusing on amicable dispute resolution and aggressive litigation when necessary for families in {state}."
    })

# Write to JS file
output_path = os.path.join("assets", "js", "attorneys.js")
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w", encoding="utf-8") as f:
    f.write("const attorneys = ")
    f.write(json.dumps(attorneys, indent=4))
    f.write(";")

print(f"Generated {len(attorneys)} attorneys in {output_path}")
