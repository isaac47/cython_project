import time
import pandas as pd
from src.preprocessing.preprocessor import text_preprocessor

if __name__ == '__main__':
    data = pd.read_csv('data/sample.csv')[['text']]
    corpus = data['text'].to_list()
    # create a big corpus
    corpus = 5000*corpus

    # execute the task
    start_time = time.time()
    clean_corpus = text_preprocessor(corpus)
    print("--- %s seconds ---" % (time.time() - start_time))
