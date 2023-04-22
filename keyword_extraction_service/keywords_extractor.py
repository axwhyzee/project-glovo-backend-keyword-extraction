import numpy as np
from keybert import KeyBERT
from keyphrase_vectorizers import KeyphraseCountVectorizer


def extract_keywords(content, heading, top_n):
    model = KeyBERT()
    vectorizer = KeyphraseCountVectorizer()
    
    heading_words = [heading_keyword[0] for heading_keyword in
                     model.extract_keywords(heading, min_df=1, stop_words="english", vectorizer=vectorizer)]
    
    try:
        keywords = list(map(lambda x:x[0],
                            model.extract_keywords(
                                content, 
                                stop_words="english", 
                                seed_keywords=heading_words, 
                                top_n=top_n,
                                nr_candidates=10, 
                                diversity=.8, 
                                vectorizer=vectorizer, 
                                use_maxsum=True
                            )
                        ))
        
        _, word_embeddings = model.extract_embeddings(docs=content, candidates=keywords, stop_words="english") # returns doc & word embeddings
        
        return list(zip(keywords, word_embeddings.tolist()))

    except ValueError:
        return []


def get_phrase_embedding(phrase, content_words, phrase_embeddings):
    try:
        index = content_words.index(phrase.split()[0])
    except ValueError:
        return None
    
    embedding = phrase_embeddings[index: index + len(phrase.split())].tolist()
    
    if len(embedding) == 0:
        return None
    
    avg_embedding = np.average(embedding, axis=0).tolist()

    return avg_embedding