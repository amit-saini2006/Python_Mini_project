import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

# Load dataset
df = pd.read_csv('books.csv')

# Handle missing values in 'description'
df['description'] = df['description'].fillna('')

# Create TF-IDF matrix
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['description'])

# Compute cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Map book titles to indices
indices = pd.Series(df.index, index=df['title']).drop_duplicates()

# Define recommendation function
def get_recommendations(title, df, cosine_sim, indices):
    # Handle missing titles
    if title not in indices:
        return pd.DataFrame({'Error': [f"'{title}' not found in the dataset. Please check spelling or try another title."]})

    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    book_indices = [i[0] for i in sim_scores]
    
    return df[['title', 'author', 'genre']].iloc[book_indices]

# Streamlit UI
st.title('📚 Book Recommendation Engine')
st.write("Enter a book title to get similar recommendations based on the description.")

select_book = st.text_input("Book Title")

if select_book:
    results = get_recommendations(select_book.strip(), df, cosine_sim, indices)
    st.table(results)
