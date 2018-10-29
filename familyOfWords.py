

label_word_lists = []
with open('RetroReportSample-SupremeCourt.txt', 'r',encoding="utf8") as file:
#with open('sample.txt', 'r',encoding="utf8") as file:
    lines = file.readlines()
    for line in lines:
        label_word_lists.append(line[:len(line)])

import gensim
import re
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer

def get_WordNet_augmentation(word):
    # Given a word, returns a list of hypernyms, synonyms, meronyms, and troponyms (not found in wordnet)

    returned_list = []
    #lancaster_stemmer =  LancasterStemmer()
    wordnet_lemmatizer = WordNetLemmatizer()
    #returned_list +=  lancaster_stemmer.stem(word)
    lemma = wordnet_lemmatizer.lemmatize(word)
    syns = wn.synsets(lemma)
    for syn in syns:
        # Add synonyms
        returned_list += syn.lemma_names()
        hypers = syn.hypernyms()
        mero_parts = syn.part_meronyms()
        mero_subs = syn.substance_meronyms()
        for hyper in hypers:
            # Add hypernyms
            returned_list += hyper.lemma_names()
        for mero_part in mero_parts:
            # Add mero_parts
            returned_list += mero_part.lemma_names()
        for mero_sub in mero_subs:
            # Add mero_sub
            returned_list += mero_sub.lemma_names()
    return list(set(returned_list))

# Load Google's pre-trained Word2Vec model.
GNews_SLIM_model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300-SLIM.bin', binary=True)

def get_w2v_augmented_list(word, topn=10):
    return [x[0].lower() for x in GNews_SLIM_model.wv.most_similar(positive=[word], topn=topn)]

stops = set(stopwords.words("english"))
def clean_text(string):
    cleaned = re.sub(r'[^\w]', ' ', string.lower())
    cleaned = cleaned.replace("'",' ').replace(',',' ').replace('"',' ').replace('+',' ').replace('(',' ').replace(')',' ').replace('of',' ').replace('_',' ').replace('.',' ').replace('~',' ').replace('-',' ')
    return cleaned

def clean_word_list(string):
    # Create a clean list of words from a string with stopwords removed
    cleaned_words = clean_text(string).split()
    returned = []
    for word in cleaned_words:
        if len(word) <= 1 or word == '(en)' or word in stops:
        #if len(word) <= 1 or word == '(en)':
            continue
        digit_flag = False
        for char in word:
            if char.isdigit():
                digit_flag = True
                break
        if digit_flag == True:
            continue
        else:
            returned.append(word)
    return list(set(returned))


clean_label_word_lists = []
for label in label_word_lists:
    clean_label_word_lists.append(clean_word_list(label))



counter = 0
label_w2v_lists = []
# label_wn_lists = []
# label_lda_lists = []
for word_list in clean_label_word_lists:
    w2v_augmentation = []+word_list
    for word in word_list:
        if word in GNews_SLIM_model.wv.vocab:
            w2v_augmentation += get_w2v_augmented_list(word)
            w2v_augmentation += get_WordNet_augmentation(word)
    label_w2v_lists.append(list(set(w2v_augmentation)))
    counter += 1

with open('RetroReportSample-SupremeCourt-extended.txt','w') as file:
    for word_list in label_w2v_lists:
        file.write(' '.join(word for word in word_list))
        file.write('\n')

