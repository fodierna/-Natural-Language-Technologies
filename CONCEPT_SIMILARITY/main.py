from utilities import *
def main():
    output_wu_p = []
    output_sp = []
    output_lc = []
    w1, w2, target = read("./WordSim353/WordSim353.csv")

    for i in range(len(w1)):
        #Wu & Palmer similarity computation
        output_wu_p.append(wu_palmer_similarity(w1[i], w2[i]))
        # Shortest path similarity computation
        output_sp.append(sp_similarity(w1[i], w2[i]))
        # Leakock & Chodorow similarity computation
        output_lc.append(lc_similarity(w1[i], w2[i]))

    print("Spearman rank correlation coefficient for:")
    print("{}: {}".format("Wu & Palmer metric", spearman_rank_correlation_coefficient(output_wu_p, target)))
    print("{}: {}".format("Shortest path metric", spearman_rank_correlation_coefficient(output_sp, target)))
    print("{}: {}".format("Leakcock & Chodorow metric", spearman_rank_correlation_coefficient(output_lc, target)))

    print("\n\n")

    print("Pearson correlation for:")
    print("{}: {}".format("Wu & Palmer metric", pearson_correlation(output_wu_p, target)))
    print("{}: {}".format("Shortest path metric", pearson_correlation(output_sp, target)))
    print("{}: {}".format("Leakcock & Chodorow metric", pearson_correlation(output_lc, target)))

if __name__=="__main__":
    main()