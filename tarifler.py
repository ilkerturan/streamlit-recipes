import streamlit as st
import requests


def get_recipes(page=1):
    url = f"https://dummyjson.com/recipes?limit=9&skip={(page - 1) * 9}"
    response = requests.get(url)
    recipes = []
    if response.status_code == 200:
        recipes = response.json()['recipes']
        print("Count:", len(recipes))
    return recipes


def start():
    st.set_page_config(page_title="Yemek Tarifleri", page_icon=":fork_and_knife:")
    st.title("Yemek Tarifleri")
    st.divider()
    data = get_recipes()
    for recipe in data:
        with st.container(border=True):
            st.title(recipe['name'])

            col1, col3 = st.columns([1, 3])

            with col3:
                st.write(f"**Hazırlık Süresi:** {recipe['prepTimeMinutes']} dk")
                st.write(f"**Pişirme Süresi:** {recipe['cookTimeMinutes']} dk")
                st.write(f"**Porsiyon:** {recipe['servings']} kişilik")
                st.write(f"**Zorluk:** {recipe['difficulty']}")
                st.write(f"**Kalori:** {recipe['caloriesPerServing']} kcal")
                st.write(f"**Mutfak:** {recipe['cuisine']}")
                st.write(f"**Öğün Türü:** {', '.join(recipe['mealType'])}")
                st.write(f"**Etiketler:** {', '.join(recipe['tags'])}")

                with st.expander("Malzemeler"):
                    for ingredient in recipe['ingredients']:
                        st.write(f"- {ingredient}")
                with st.expander("Yapım Aşamaları"):
                    for idx, step in enumerate(recipe['instructions'], start=1):
                        st.write(f"{idx}. {step}")
            with col1:
                rating_stars = int(recipe['rating'])
                fractional_part = recipe['rating'] - rating_stars
                stars_display = '⭐' * rating_stars
                if fractional_part >= 0.5:
                    stars_display += '⭐'

                st.image(recipe['image'], caption=f"{stars_display} ({recipe['reviewCount']})",
                         use_container_width=True)


if __name__ == "__main__":
    start()
