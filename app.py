import streamlit as st
from PIL import Image
from models.ingredient_model import predict_ingredients
from utils.recipe_generator import generate_recipe_openai, fetch_recipes_spoonacular
from utils.helpers import format_openai_output, extract_spoonacular_details

st.set_page_config(page_title="Image-to-Recipe Generator", page_icon="🥗", layout="wide")

st.title("🥗 Image-to-Recipe Generator")
st.write("Upload an image of your ingredients and get delicious recipe ideas!")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

api_choice = st.radio("Recipe Source:", ["OpenAI (Creative AI Recipes)", "Spoonacular (Real Recipes)"])

if uploaded_file:
    # Force RGB to avoid shape mismatch (299,299,4) → (299,299,3)
    image = Image.open(uploaded_file).convert("RGB")  
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Generate Recipes"):
        with st.spinner("Detecting ingredients..."):
            ingredients = predict_ingredients(image)
            st.success(f"Detected ingredients: {', '.join(ingredients)}")

        with st.spinner("Generating recipes..."):
            if api_choice == "OpenAI (Creative AI Recipes)":
                recipes = generate_recipe_openai(ingredients)
                st.markdown(format_openai_output(recipes), unsafe_allow_html=True)
            else:
                data = fetch_recipes_spoonacular(ingredients)
                if data:
                    recipes = extract_spoonacular_details(data)
                    for r in recipes:
                        st.subheader(r["title"])
                        st.image(r["image"], use_container_width=True)
                else:
                    st.error("No recipes found. Try uploading a clearer image.")

