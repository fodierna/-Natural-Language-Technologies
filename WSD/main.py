from utilities import *
import re
from sklearn.metrics import accuracy_score
def main():
    print("*"*10, "WSD of sentences", "*"*10)
    with open("./sentences.txt", "r") as sentences:
        for line in sentences:
            for w in line.split():
                if (w.startswith("**") or w.startswith("-**")):
                    polysemic = re.sub(r'[^\w\s]', '', w)
                    print("Ambigue word: ", polysemic)
                    line = line.replace(w,polysemic)
                    best_sense = lesk(polysemic,line)
                    print("Sentence:", line.replace(polysemic, str(best_sense.lemmas()[0])).replace("\n",""))
                    print("Best sense definition: ", best_sense.definition())
                    if(len(best_sense.lemmas())>1):
                        print("Sentece rewritten with synonyms:", line.replace(polysemic, str(best_sense.lemmas())).replace("\n",""))
                    print("\n")
    print("*"*100)
    print("\n")
    print("*"*10,"SemCor WSD","*"*10)
    print("\n")
    sentences, polysemics = get_semcor()
    target = [str(w.label().synset()) for w in polysemics]

    output = []

    for i in range(len(polysemics)):
        word = re.sub(r'[^\w\s]', '', polysemics[i][0][0])
        output.append(str(lesk(word, sentences[i])))

    for i in range(10):
        print("Expected: ", target[i])
        print("Obtained: ", output[i])
        print("Result: ", "OK" if target[i]==output[i] else "NOK")
        print("\n")

    print("="*100)
    print("WSD accuracy: {:.0f}%".format(accuracy_score(target,output)*100))
    print("*"*100)

if __name__=="__main__":
    main()