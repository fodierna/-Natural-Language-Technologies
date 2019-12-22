from utilities import *
from math import floor
def main():
    nasari_source = "./utils/dd-small-nasari-15.txt"
    text_source = "./utils/Donald-Trump-vs-Barack-Obama-on-Nuclear-Weapons-in-East-Asia.txt"
    #text_source = "utils/People-Arent-Upgrading-Smartphones-as-Quickly-and-That-Is-Bad-for-Apple.txt"
    #text_source = "./utils/The-Last-Man-on-the-Moon--Eugene-Cernan-gives-a-compelling-account.txt"

    nasari_vectors = read_nasari(nasari_source)
    title, original_title, text, paragraphs, original_paragraphs = read_text(text_source)
    topic = get_context_topic(title, nasari_vectors)
    context = get_context_topic(text, nasari_vectors)
    weights = {k:0 for k in paragraphs}

    for key in paragraphs:
        weights[key] = paragraph_weight(paragraphs[key], context, topic)

    compression_rate = 0.2
    # number of paragraphs to insert in summarized text
    par_num = floor(len(paragraphs) - (len(paragraphs)*compression_rate))
    par = list()

    # take the most important paragraphs
    for i in range(par_num):
        maximum = max(weights, key=weights.get)
        par.append(maximum)
        weights.pop(maximum)

    par = sorted(par)

    with open("./result.txt", "w", encoding="utf8") as res:
        res.write("*"*30+"Summarized document"+"*"*30+"\n\n",)
        res.write(str(original_title)+"\n")
        for i in par:
            res.write("".join(original_paragraphs[i])+"\n")
        res.close()




if __name__=="__main__":
    main()
