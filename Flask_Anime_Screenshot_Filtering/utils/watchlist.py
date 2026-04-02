import re

def parse_watchlist(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    entries = []
    # Match numbered entry, name can span multiple lines, ends at rating
    pattern = re.compile(r"^\d+\.\s+([\s\S]+?)\s*\((\d+(?:\.\d+)?\/5)\)", re.MULTILINE)

    matches = pattern.finditer(content)
    for match in matches:
        name = match.group(1).replace("\n", " ").strip()
        rating = match.group(2).strip()
        entries.append({
            "name": name,
            "rating": rating
        })

    return entries


if __name__ == "__main__":
    import os
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    entries = parse_watchlist(os.path.join(base, "Anime_Watchlist.txt"))
    print(f"Total parsed: {len(entries)}")
    for e in entries[:5]:
        print(e)