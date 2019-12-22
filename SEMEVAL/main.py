from utilities import *
import re

def main():
    source="./it.test.data.txt"
    annotated_file = "./odierna_annotation101-200.txt"
    lines = read_file(annotated_file)
    results = open("results.txt","w", encoding="utf8")
    for couple, score in zip(lines["words"],lines["score"]):
        bn_id1 = get_bnid(couple[0])
        bn_id2 = get_bnid(couple[1])
        bn_vec1 = get_nasari_vectors(bn_id1)
        bn_vec2 = get_nasari_vectors(bn_id2)
        c1,c2 = get_max_similar(bn_vec1["vectors"],bn_vec2["vectors"])
        if("Not found" not in c1):
            best_bnid1 = get_id_from_vector(c1, bn_vec1)
            gloss1 = get_gloss(best_bnid1)
        else:
            best_bnid1 = c1
            gloss1 = c1
        if("Not found" not in c2):
            best_bnid2 = get_id_from_vector(c2, bn_vec2)
            gloss2 = get_gloss(best_bnid2)
        else:
            best_bnid2 = c2
            gloss2 = c2
        print("BEST BAEL SYNSETS for [{},{}] are [{},{}]".format(couple[0], couple[1], best_bnid1, best_bnid2))
        print("GLOSSES\n[{}: {}]\n[{}: {}]".format(couple[0], gloss1, couple[1],gloss2))
        print("ASSIGNED SCORE", score)
        print("\n")
        results.write("BEST BAEL SYNSETS for [{},{}] are [{},{}]".format(couple[0], couple[1], best_bnid1, best_bnid2))
        results.write("\n")
        results.write("GLOSSES\n[{}: {}]\n[{}: {}]".format(couple[0], gloss1, couple[1],gloss2))
        results.write("\n")
        results.write("ASSIGNED SCORE: {}".format(score))
        results.write("\n\n")
    results.close()



if __name__=="__main__":
    main()