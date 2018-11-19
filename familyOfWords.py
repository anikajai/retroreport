label_word_lists = []
# with open('RetroReportSample-SupremeCourt-modified.txt', 'r',encoding="utf8") as file:
with open('for-synonyms.txt', 'r',encoding="utf8") as file:
    lines = file.readlines()
    for line in lines:
        label_word_lists.append(line[:len(line)])

import gensim
import re
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer

def get_WordNet_augmentation(word, appendText = ""):
    # Given a word, returns a list of hypernyms, synonyms, meronyms, and troponyms (not found in wordnet)

    returned_list = []
    #lancaster_stemmer =  LancasterStemmer()
    wordnet_lemmatizer = WordNetLemmatizer()
    #returned_list +=  lancaster_stemmer.stem(word)
    lemma = wordnet_lemmatizer.lemmatize(word)
    syns = wn.synsets(lemma)
    for syn in syns:
        # Add synonyms
        for l in syn.lemma_names():
            returned_list.append(l+ appendText)
        # returned_list += syn.lemma_names()
        hypers = syn.hypernyms()
        mero_parts = syn.part_meronyms()
        mero_subs = syn.substance_meronyms()
        for hyper in hypers:
            # Add hypernyms
            for l in hyper.lemma_names():
                returned_list.append(l + appendText)
            # returned_list +=
        for mero_part in mero_parts:
            # Add mero_parts
            # returned_list += mero_part.lemma_names()
            for l in mero_part.lemma_names():
                returned_list.append(l + appendText)
        for mero_sub in mero_subs:
            # Add mero_sub
            for l in mero_sub.lemma_names():
                returned_list.append(l + appendText)
            # returned_list += mero_sub.lemma_names()
    return list(set(returned_list))

# Load Google's pre-trained Word2Vec model.
GNews_SLIM_model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300-SLIM.bin', binary=True)

def get_w2v_augmented_list(word, appendText = "", topn=5):
    return [str(x[0].lower()+ str(appendText)) for x in GNews_SLIM_model.wv.most_similar(positive=[word], topn=topn)]

stops = set(stopwords.words("english"))
def clean_text(string):
    cleaned = re.sub(r'[^\w]', ' ', string.lower())
    cleaned = cleaned.replace("'",' ').replace(',',' ').replace('"',' ')\
        .replace("'","").replace('(',' ').replace(')',' ')\
        .replace(':',' ').replace('_',' ').replace('.',' ').replace('~',' ').\
        replace("narration:", "").replace("archival", "")
    return cleaned

def clean_word_list(string):
    # Create a clean list of words from a string with stopwords removed
    cleaned_words = clean_text(string).split()
    # print (str(cleaned_words))
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



label_w2v_lists = []
# label_wn_lists = []
# label_lda_lists = []
out_map = {}
for lineIndex, word_list in enumerate(clean_label_word_lists):
    w2v_augmentation = []#+word_list
    for wordIndex, word in enumerate(word_list):
        # appendText = "("+ str(lineIndex) + "," + str(wordIndex) + ")"

        # print ("word is: " + word + appendText)
        # if word in GNews_SLIM_model.wv.vocab:
        #     w2v_augmentation += get_w2v_augmented_list(word,appendText)
        # aug_lis = get_WordNet_augmentation(word)
        if word in GNews_SLIM_model.wv.vocab:
            aug_lis = get_w2v_augmented_list(word)
            # print (str(aug_lis))
            if aug_lis is not None and len(aug_lis) > 0:
                if word in out_map.keys():
                    out_map[word].update(set(aug_lis))
                else:
                    augs = set(aug_lis)
                    out_map[word] = augs
        # w2v_augmentation.append(word)
        # w2v_augmentation += get_WordNet_augmentation(word)
    # label_w2v_lists.append(list(set(w2v_augmentation)))
# counter = 0
# for word in out_map.keys():
#     label_w2v_lists.append(list(out_map[word]))
#     counter += 1

# with open('RetroReportSample-SupremeCourt-extended.txt','w') as file:

def breakParts(l, num):
    out = []
    while len(l) > num:
      out.append(l[0:num])
      l = l[num:len(l)]
    out.append(l)
    return out

with open('synonyms-extended.txt', 'w') as file:
    # for word_list in label_w2v_lists:
        # file.write(' '.join(word for word in word_list))
    file.write("index.batch_synonyms([")
    index = 0
    for word in out_map.keys():
        # out_map[word] = out_map[word].remove(word)
        if out_map[word] is not None  and len(out_map[word]) > 1:
            # out_map[word] = out_map[word].remove(word)
            if out_map[word] is not None:
                # print (str(out_map[word]))
                cur_list = list(out_map[word])
                parts = breakParts(cur_list, 19)
                for part in parts:
                    file.write('{"objectID": "sRR' + str(index) + '", "type": "synonym", "synonyms": ')
                    part.append(word)
                    file.write(str(part))
                    file.write('},')
                    index+=1
    file.write("\b],forward_to_replicas=True, replace_existing_synonyms=True)")
