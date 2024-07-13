# CineMatch: Your Personalized Movie Guide

Welcome to **CineMatch**, a personalized movie recommendation system built using Streamlit and Natural Language Processing (NLP). This project leverages the TMDB movie metadata dataset from Kaggle and integrates with the TMDB API to fetch movie posters.

## Features

- **Personalized Recommendations**: Get movie suggestions based on your recent watch.
- **Natural Language Processing**: Implemented with PorterStemmer for text processing.
- **Streamlit Interface**: Simple and interactive UI for seamless user experience.
- **TMDB Integration**: Fetches movie posters directly from the TMDB API.

## Dataset

The dataset used in this project is from Kaggle:
[TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

## API

This project uses the TMDB API to fetch movie posters. You can get the API key by creating an account on [The Movie Database (TMDB)](https://www.themoviedb.org/).

## Installation

To install and run this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/CineMatch.git
    cd CineMatch
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

## Files

- `Movie-Recommender-Notebook.ipynb`: Jupyter notebook containing the data processing and model creation code.
- `app.py`: Streamlit app for the movie recommendation system.
- `requirements.txt`: List of dependencies required to run the project.
- `movies.pkl`, `movie_dict.pkl`, `similarity.pkl`: Pickle files storing processed data and similarity matrix.

## How It Works

1. **Data Preprocessing**: The dataset is processed to extract relevant features like genres, keywords, cast, crew, and overview.
2. **Text Processing**: NLP techniques including tokenization and stemming (using PorterStemmer) are applied.
3. **Vectorization**: CountVectorizer is used to convert text data into vectors.
4. **Similarity Calculation**: Cosine similarity is computed to find similar movies.
5. **Recommendation System**: Based on the similarity scores, top 5 movie recommendations are provided.
6. **Poster Fetching**: Movie posters are fetched using the TMDB API.

## Usage

1. Select a movie from the dropdown list.
2. Click on the "Recommend" button.
3. View the recommended movies along with their posters.

## Example

Here's how to use the app:

- Select a movie (e.g., Avatar) from the dropdown.
- Click on "Recommend".
- Get recommendations like "Avatar", "The Avengers", etc.

## Deployment

This app can be deployed for free on Streamlit Sharing, Heroku, or other cloud platforms. Follow the respective platform's deployment guide to get your app online.

## Acknowledgements

- [Kaggle](https://www.kaggle.com/) for the dataset.
- [TMDB](https://www.themoviedb.org/) for the API.

## Contributing

Feel free to open issues or submit pull requests if you have any improvements or suggestions.

## License

This project is licensed under the MIT License.

---

**Author**: Vinesh Ryapak https://www.linkedin.com/in/vinesh-ryapak-73693a227/
