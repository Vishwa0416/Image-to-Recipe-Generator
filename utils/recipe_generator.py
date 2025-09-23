import requests
import openai
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SPOONACULAR_KEY = os.getenv("SPOONACULAR_KEY")

openai.api_key = OPENAI_API_KEY

def generate_recipe_openai(ingredients):
    """
    Generate creative recipes using OpenAI GPT.
    """
    prompt = f"Suggest 3 unique recipes using these ingredients: {', '.join(ingredients)}. " \
             f"Provide each recipe with a title, ingredients list, and step-by-step instructions."
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=600,
        temperature=0.7
    )
    return response.choices[0].text.strip()

def fetch_recipes_spoonacular(ingredients):
    """
    Fetch recipes from Spoonacular API based on detected ingredients.
    """
    url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={','.join(ingredients)}&number=3&apiKey={SPOONACULAR_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []
