import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords, semcor
from nltk.corpus.reader.wordnet import Lemma
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
import random
#nltk.download('semcor')
#nltk.download('stopwords')
#nltk.download("wordnet")
#nltk.download('punkt')
tokenizer = RegexpTokenizer(r'\w+')
lemmatizer = WordNetLemmatizer()
stop_words = stopwords.words('english')
stop_words.append("etc")

#compute the best sense for a polysemous word given a sentence (context)
def lesk(word, sentence):

    best_sense = wn.synsets(word)[0]
    max_overlap = 0
    context = set(w for w in tokenizer.tokenize(sentence))

    for sense in wn.synsets(word):
        #gloss associated to the synset
        signature = set(tokenizer.tokenize(sense.definition()))

        if(len(sense.examples())):
            if (len(sense.examples())>1):
                #examples associated to the synset
                for e in sense.examples():
                    signature.union(tokenizer.tokenize(e))
            else:
                #single example
                signature.union(tokenizer.tokenize(sense.examples()[0]))

        signature = set(lemmatizer.lemmatize(w) for w in signature if not w in stop_words)

        #compute the overlap considering the common word between the context and the signature (gloss+example)
        overlap = len(signature.intersection(context))
        #to find the maximum overlap
        if(overlap > max_overlap):
            max_overlap = overlap
            best_sense = sense
    # the sense that maximize the overlap
    return best_sense


def get_semcor():
    sentences = []
    polysemics = []

    for i in range(0, 50):
        elem = list(filter(lambda sentence_tree:
                           isinstance(sentence_tree.label(), Lemma) and
                           sentence_tree[0].label() == "NN", semcor.tagged_sents(tag='both')[i]))

        if elem:
            polysemics.append(random.choice(elem))
            sentences.append(" ".join(semcor.sents()[i]))

    return sentences, polysemics

