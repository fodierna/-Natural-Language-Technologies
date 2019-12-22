import csv
from math import log
import numpy as np
from numpy import cov, std
from scipy.stats import rankdata
import nltk
from nltk.corpus import wordnet as wn
import sys

# read a file containing two words and a similitary score associated to
def read(path):
    #nltk.download('wordnet')
    with open(path) as csv_file:
        w1 = []
        w2 = []
        target = []
        line_count = 0
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                w1.append(row[0])
                w2.append(row[1])
                target.append(float(row[2])/10)
                #print("Word 1: {} \t Word 2: {} \t Target: {}".format(row[0], row[1], row[2]))
                line_count += 1
        #print(f'Processed {line_count} lines.')
        return w1, w2, target


# wu palmer similarity
def wu_palmer_similarity(w1, w2):

    max_sim = 0
    # look for each word in synset associated to w1
    for s1 in wn.synsets(w1):
        # look for each word in synset associated to ww
        for s2 in wn.synsets(w2):
            #first common parent of s1 and s2
            for lcs in s1.lowest_common_hypernyms(s2):
                # wu-palmer sim: 2*depth(LCS) / depth(s1)+depth(s2)
                sim = 2*lcs.max_depth()/(s1.max_depth()+s2.max_depth())
                # to find the maximum similarity
                if(sim > max_sim):
                    max_sim = sim
    return max_sim

# shortest path similarity
def sp_similarity(w1, w2, depth_max = 30):
    min_len = sys.maxsize
    # look for each word in synset associated to w1
    for s1 in wn.synsets(w1):
        # look for each word in synset associated to w2
        for s2 in wn.synsets(w2):
            # find the shortest path distance between s1 and s2
            len = s1.shortest_path_distance(s2)

            if(len is None):
                len = 2 * depth_max
            # to find the shortest path
            if(len < min_len):
                min_len = len
            # normalized similarity
    return (2*depth_max - min_len) / (2*depth_max)

# leakcock & chodorow similarity
def lc_similarity(w1, w2, depth_max = 30):
    max_sim = 0
    # look for each word in synset associated to w1
    for s1 in wn.synsets(w1):
        # look for each word in synset associated to w2
        for s2 in wn.synsets(w2):
            # find the shortest path distance between s1 and s2
            len = s1.shortest_path_distance(s2)
            if(len is not None):
                if(len>0):
                    sim = -(log(len/(2*depth_max+1)))
                else:
                    sim = -(log(len+1/(2*depth_max+1)))
            else:
                sim = 0
            if(sim > max_sim):
                max_sim = sim
    return max_sim/log(2*depth_max+1)


#correlation indexes

def spearman_rank_correlation_coefficient(target, predicted):
    target = np.array(target).astype(np.float)
    predicted = np.array(predicted).astype(np.float)
    return cov(rankdata(target), rankdata(predicted))[0][1] / (std(rankdata(target)) * std(rankdata(predicted)))


def pearson_correlation(target, predicted):
    target = np.array(target).astype(np.float)
    predicted = np.array(predicted).astype(np.float)
    return cov(target, predicted)[0][1] / (std(target)*std(predicted))

