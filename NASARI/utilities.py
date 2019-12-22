import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
from collections import defaultdict
import csv
import re

tokenizer = RegexpTokenizer(r'\w+')
lemmatizer = WordNetLemmatizer()
stop_words = stopwords.words('english')


def read_text(source):
    with open(source, encoding="utf8") as src:
        i=-1
        text = list()
        paragraph = defaultdict(list)
        original_paragraph = defaultdict(list)
        for line in src:
            line_processed = [w for w in tokenizer.tokenize(line) if w.lower() not in stop_words]
            if(i==-1):
                title = line_processed
                original_title = line
                i+=1
            else:
                if len(line_processed):
                    text+=line_processed
                    paragraph[i]+=line_processed
                    original_paragraph[i].append(line)
                else:
                    i+=1
        src.close()


    return title, original_title, text, paragraph, original_paragraph


def read_nasari(source):
    nasari_vectors= list()
    with open(source, encoding="utf8") as src:
        for line in csv.reader(src, dialect="excel-tab"):
            vector = [w.strip() for w in line[0].split(";")]
            bn_n = vector[0]
            lemma= [w.lower() for w in vector[1:] if "_" not in w]
            w_s = [w_s.split("_") for w_s in vector[1:] if "_" in w_s]
            nasari_vectors.append({
                "bn_n": bn_n,
                "lemma": lemma,
                "w_s": w_s
            })
        src.close()

    return nasari_vectors

# create context considering the
def get_context_topic(text, nasari_vectors):
    context = list()
    for word in text:
        # get all the vectors which have as lemma the word in the title
        for v in nasari_vectors:
            if word.lower() in v["lemma"]:
                if v["w_s"] not in context:
                    context+=v["w_s"]
    return context


#compute paragraph weight wrt common words between the paragraph and the context and the paragraph and the topic
def paragraph_weight(paragraph, context, topic):
    #contex is the set of relevant vectors extracted from NASARI using the whole text. Form: [["word_1", "score_1"],...,["word_n", "weight_n"]]
    #topic is the set of relevat vectors extracted from NASARI using the title. Form: [["word_1", "score_1"],...,["word_n", "weight_n"]]
    weight = 0

    for w_par in paragraph:
        for w_s in context:
            #compare word in paragraph to the word in context-
            if (w_par.lower() == w_s[0]):
                #print(w_s[0], w_s[1])
                #if match update the weight of the paragraph
                weight+= float(w_s[1])
        for w_s in topic:
            if(w_par.lower() == w_s[0]):
                #print(w_s[0], w_s[1])
                weight+= float(w_s[1])
    return weight

