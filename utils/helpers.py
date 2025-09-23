def format_openai_output(text):
    """
    Convert raw OpenAI text into a clean, Streamlit-friendly format.
    Tries to break text into sections for better readability.
    """
    sections = text.strip().split("\n\n")
    formatted = ""
    for section in sections:
        if ":" in section:
            title, content = section.split(":", 1)
            formatted += f"**{title.strip()}**: {content.strip()}<br><br>"
        else:
            formatted += section + "<br><br>"
    return formatted


def extract_spoonacular_details(data):
    """
    Extract enhanced recipe details from Spoonacular response.
    """
    recipes = []
    for item in data:
        recipes.append({
            "title": item.get("title"),
            "image": item.get("image"),
            "id": item.get("id"),
            "likes": item.get("likes", 0),
            "usedIngredients": [i["name"] for i in item.get("usedIngredients", [])],
            "missedIngredients": [i["name"] for i in item.get("missedIngredients", [])]
        })
    return recipes
