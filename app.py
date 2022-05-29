

# A simple Movie Recommendation Engine based on Content based filtering
# The similarity is calculated using cosine similarity and the
# movies can also be searched based on name of the director.
# With this program we can get the details of a selected movie, and we can also
# get the recommended movies for a selected movie and get the details of the recommended movies.
# We can also get the movies of a given director


import streamlit as st
import pickle
import pandas as pd
import requests
from PIL import Image


# Function to get the url of movie's poster from the tmbs's website
def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(
            movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


# Function to get the list of recommended movie names and their respective posters.
# The similarity matrix depicts the cosine-similarity value of one movie with the other
def recommend(movie):
    # getting index of the movie from data through its title and
    # fetching the similar movies from similarity matrix

    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    # slicing the sorted list to get the top 8 recommended movies for a given movie
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:9]

    # storing the recommended movies and their respective posters in two lists
    recommended_movies = []
    recommended_movies_posters = []
    for elem in movies_list:
        movie_id = movies.iloc[elem[0]].id
        recommended_movies.append(movies.iloc[elem[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters


# Function for printing details of the movie namely director, top 3 cast and the genres
def print_movie_details(movie):
    # getting the index of the film in order to fetch its details
    movie_index = movies[movies['title'] == movie].index[0]
    director_name = director[movie_index]
    starring_list = starring[movie_index]
    genres_list = genres[movie_index]

    st.write('**Director** :     ', director_name[0])
    st.write("**Starring** :     ", starring_list[0], ', ', starring_list[1], ', ', starring_list[2])
    string = ""
    for elem in genres_list:
        string = string + elem + ", "
    st.write("**Genres** :   " + string)


# Function to convert a given list to a string
def list_to_string(l):
    return " ".join(l)


# Function to find the index of director to get that director's movies
def find_index_director(name):
    count = 0
    director_movies = []
    director_movies_posters = []

    for elem in director:
        if list_to_string(elem) == name:
            director_movie_id = movies.iloc[count].id
            director_movies.append(movies.iloc[count].title)
            director_movies_posters.append(fetch_poster(director_movie_id))
        count += 1

    return director_movies, director_movies_posters


# Getting all the required pre-processed data into this file using pickle library
movie_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))
director = pickle.load(open('director.pkl', 'rb'))
director_new = pickle.load(open('director2.pkl', 'rb'))
starring = pickle.load(open('starring.pkl', 'rb'))
genres = pickle.load(open('genres.pkl', 'rb'))

st.title('Movie Recommendation Engine')


# An expander to see the details of a movie and its poster
def new_expander(movie):
    with st.expander("See Details"):
        # st.write()
        print_movie_details(movie)
        movie_index = movies[movies['title'] == movie].index[0]
        movie_id = movies.iloc[movie_index].id
        poster_selected_movie = fetch_poster(movie_id)
        st.image(poster_selected_movie, caption=movie, width=200)


# An expander to see only the details of a movie
def new_expander_details(movie):
    with st.expander("See Details"):
        print_movie_details(movie)


# Function for printing name, poster and details of movies
def print_movies(n):
    st.text(names[n - 1])
    st.image(posters[n - 1])
    new_expander_details(names[n - 1])
    st.text(names[4 + (n - 1)])
    st.image(posters[4 + (n - 1)])
    new_expander_details(names[4 + (n - 1)])



# Creating a sidebar
sidebar_selectbox = st.sidebar.selectbox(
    "Chose your sorting mechanism",
    ('None(Default)', 'Search by director', 'Recommend movies')
)

if sidebar_selectbox == 'None(Default)':
    image = Image.open('./movies-poster-image.jpg')
    st.image(image, width=750)


elif sidebar_selectbox == 'Search by director':
    # converting list of lists to list of strings for easy processing
    director_string = []
    for i in director_new:
        director_string.append(list_to_string(i))
    selected_director_name = st.selectbox("Search below for a director", director_string)

    # getting names and their respective posters of the selected director's movies
    st.text("")
    director_movie_names, director_movie_posters = find_index_director(selected_director_name)

    if len(director_movie_names) >= 4:
        st.subheader('Few movies of ' + selected_director_name)
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.image(director_movie_posters[0], caption=director_movie_names[0])

        with col2:
            st.image(director_movie_posters[1], caption=director_movie_names[1])

        with col3:
            st.image(director_movie_posters[2], caption=director_movie_names[2])

        with col4:
            st.image(director_movie_posters[3], caption=director_movie_names[3])

    # printing blank lines
    st.text("")
    st.text("")

    # printing the complete list of movies of a director and their details
    st.write("The complete list of films of " + selected_director_name + " is as follows :point_down:")
    movie_name = st.radio('Select the film to see details', director_movie_names)
    print_movie_details(movie_name)


elif sidebar_selectbox == 'Recommend movies':
    selected_movie_name = st.selectbox("Search below for a movie", movies['title'].values)
    new_expander(selected_movie_name)

    st.subheader('Recommended movies of ' + selected_movie_name)
    names, posters = recommend(selected_movie_name)

    # printing the top 8 recommended movies of a selected movie
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        print_movies(1)

    with col2:
        print_movies(2)

    with col3:
        print_movies(3)

    with col4:
        print_movies(4)

