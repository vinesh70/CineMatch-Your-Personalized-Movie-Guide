import pandas as pd
import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={tmdb_api_key}')
    data = response.json()
    if 'poster_path' in data and data['poster_path'] is not None:
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    else:
        return None  # Handle cases where no poster path is available


def recommend(movie):
    try:
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommend_movies = []
        recommended_movies_posters = []
        for i in movies_list:
            movie_id = movies.iloc[i[0]].movie_id
            recommend_movies.append(movies.iloc[i[0]].title)
            # Fetch poster from API
            poster_url = fetch_poster(movie_id)
            if poster_url:
                recommended_movies_posters.append(poster_url)
            else:
                recommended_movies_posters.append('https://via.placeholder.com/500x750.png?text=No+Poster+Available')
        return recommend_movies, recommended_movies_posters
    except IndexError:
        st.error("Movie not found in the database. Please select another movie.")

# Load data and similarity matrix
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

# Streamlit UI
st.set_page_config(
    page_title="CineMatch: Your Personalized Movie Guide",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="auto"
)

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Which movie did you watch recently?',
    movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    if names and posters:
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(names[0])
            st.image(posters[0])

        with col2:
            st.text(names[1])
            st.image(posters[1])

        with col3:
            st.text(names[2])
            st.image(posters[2])

        with col4:
            st.text(names[3])
            st.image(posters[3])

        with col5:
            st.text(names[4])
            st.image(posters[4])
