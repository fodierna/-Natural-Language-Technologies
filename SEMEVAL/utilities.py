import numpy as np
import linecache
import re
from sklearn.metrics.pairwise import cosine_similarity
import urllib
import urllib3
import json
key = "eed30802-2cf7-4a0f-8082-78e51033a09f"

def annotate_file(source):
    f = open("odierna_annotation101-200.txt", "w")
    for i in range(101,201):
        line = linecache.getline(source, i)
        print(line)
        score =  input("Insert score [0-4]: ")
        f.write(line.replace("\n", "")+" "+score+"\n")
    print("Great work! You should take a break now! :)")

def read_file(source):
    lines = {"words": [],
             "score": []
             }
    with open(source) as src:
        for line in src:
            line = [*line.split("\t")]
            score = re.findall(r"\d*\.\d+|\d+", line[1])[0]
            line[1] = line[1].replace(score, "").replace("\n", "")
            lines["words"].append([line[0], line[1]])
            lines["score"].append(score)
        src.close()
    return lines

def get_nasari_vectors(bn_id_list):
    nasari = "./utils/SemEval17-Task2/mini_NASARI/mini_NASARI.tsv"
    nasari_vectors = dict.fromkeys(["bn_id","vectors"])
    with open(nasari, encoding="utf8") as src:
        for line in src:
            #get babelnet synset id
            bn_id = line.split("__")[0]
            # get only numerical attributes
            vector = line.replace("\n","").split("__")[1].split("\t")[1:]

            for id in bn_id_list:
                if(id == bn_id):
                    if(nasari_vectors["bn_id"] is None):
                        nasari_vectors["bn_id"] = bn_id
                    else:
                        nasari_vectors["bn_id"] = bn_id
                    if (nasari_vectors["vectors"] is None):
                        nasari_vectors["vectors"] = list()
                        nasari_vectors["vectors"].append(vector)
                    else:
                        nasari_vectors["vectors"].append(vector)


        src.close()
    return nasari_vectors


def get_bnid(w):
    src = "./utils/SemEval17-Task2/mini_NASARI/SemEval17_IT_senses2synsets.txt"
    w_bn = list()
    i=1
    w = w.strip()
    while(1):
        line = linecache.getline(src, i)
        if(line==""):
            #print("EOF")
            break
        if line.startswith("#"):
            lemma = line.replace("#", "").strip()
            if(w == lemma):
                j=i+1
                while(1):
                    line = linecache.getline(src, j)
                    j+=1
                    if(line.startswith("#")):
                        break
                    else:
                        w_bn.append(line.strip())
        i+=1
    return w_bn

def get_max_similar(concept1, concept2):
    max_sim = 0
    c1_max = ""
    c2_max = ""
    if(concept1 is None or concept2 is None):
        return "Not found", "Not found"
    for c1 in concept1:
        for c2 in concept2:
            c1 = np.array(c1).reshape(1, -1)
            c2 = np.array(c2).reshape(1, -1)
            sim = cosine_similarity(c1, c2)
            if(sim>max_sim):
                max_sim = sim
                c1_max = c1
                c2_max = c2
    return c1_max, c2_max

def get_id_from_vector(vector, bn_vec):
    for v1 in vector:
        for v2 in bn_vec["vectors"]:
            if(list(v1) == v2):
                if(bn_vec is not None):
                    return bn_vec["bn_id"]
    return "Not found"

def get_gloss(bn_id):


    bn_url = 'https://babelnet.io/v5/getSynset'
    params = {
        'id': bn_id,
        'key': key
    }

    url = bn_url + '?' + urllib.parse.urlencode(params)

    http = urllib3.PoolManager()
    response = http.request('GET', url)
    b_syn = json.loads(response.data.decode('utf-8'))

    return ['BABEL SYNSET NOT FOUND'] if 'message' in  b_syn else b_syn['glosses'][0]['gloss']
