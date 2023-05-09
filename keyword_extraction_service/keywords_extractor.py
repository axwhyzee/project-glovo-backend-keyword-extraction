from keybert import KeyBERT
from keyphrase_vectorizers import KeyphraseCountVectorizer
from huggingface_hub import login
import os


HF_TOKEN = os.environ.get("HF_TOKEN")
login(token=HF_TOKEN, add_to_git_credential=True)

model = KeyBERT()
vectorizer = KeyphraseCountVectorizer()

def extract_keywords(content, heading, top_n):
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