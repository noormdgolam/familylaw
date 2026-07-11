import os
import json

def build_index():
    index = []
    
    # Index States
    states_dir = "states"
    if os.path.exists(states_dir):
        for state_slug in os.listdir(states_dir):
            if os.path.isdir(os.path.join(states_dir, state_slug)):
                state_name = state_slug.replace("-", " ").title()
                index.append({
                    "title": f"{state_name} Family Law Statute of Limitations Guide",
                    "url": f"/states/{state_slug}/",
                    "type": "State Guide",
                    "keywords": [state_name, "statute of limitations", "divorce", "alimony", "child custody", state_slug]
                })

    # Index Educational
    edu_dir = "educational"
    if os.path.exists(edu_dir):
        for edu_slug in os.listdir(edu_dir):
            if os.path.isdir(os.path.join(edu_dir, edu_slug)):
                edu_name = edu_slug.replace("-", " ").title()
                index.append({
                    "title": f"{edu_name} - Educational Explainer",
                    "url": f"/educational/{edu_slug}/",
                    "type": "Educational Guide",
                    "keywords": [edu_name, edu_slug, "guide", "explainer", "family law"]
                })

    # Index International
    intl_dir = "international"
    if os.path.exists(intl_dir):
        for intl_slug in os.listdir(intl_dir):
            if os.path.isdir(os.path.join(intl_dir, intl_slug)):
                intl_name = intl_slug.replace("-", " ").title()
                index.append({
                    "title": f"{intl_name} Family Law & Divorce Guide",
                    "url": f"/international/{intl_slug}/",
                    "type": "International Guide",
                    "keywords": [intl_name, intl_slug, "international", "family law", "divorce"]
                })

    with open("search-index.json", "w") as f:
        json.dump(index, f, indent=2)

    print(f"Built search index with {len(index)} entries.")

if __name__ == "__main__":
    build_index()
