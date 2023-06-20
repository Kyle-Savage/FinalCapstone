# Compulsory Task 2

import spacy
nlp = spacy.load("en_core_web_md")

# Function to return which movies a user would watch next from the provided list based on a description entered.
def next_movie(description):
    
    with open("movies.txt", "r") as file:
        movies = file.readlines()

    similarity_scores = []
    for movie in movies:
        movie_doc = nlp(description)
        input_doc = nlp(movie)
        similarity_scores.append(movie_doc.similarity(input_doc))

    most_similar_index = similarity_scores.index(max(similarity_scores))

    return movies[most_similar_index]

# Example based on provided description
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
most_similar_movie = next_movie(description)
print(f"Based on the following despcription: \n{description} \n\nYou should watch: \n{most_similar_movie}")
