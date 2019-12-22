# Natural-Language-Technologies
Here you can find five mini-projects done for the course of Natural Language Technologies taught in the MSc in Computer Science of the University of Turin.

## Project 1: Concept Similarity (CONCEPT_SIMILARITY)
The goal of this project is to evaluate the similarity between pairs of words given in input. I implemented three similarity measures based on **WordNet: Wu & Palmer, Leakcock & Chodorow and Shotest Path**. For each implemented measure, the Spearman's and Pearson's correlation coefficients are computed.

## Project 2: Automatic Summarization with NASARI (NASARI)
The goal of this project is to produce an extracting summary of a given input document. To do this I computed the relevance of each paragraph contained in the document with the respect to the topic and the context. The topic is the set of relevat vectors extracted from NASARI using the title of the document. The contex is the set of relevant vectors extracted from NASARI using the body of the document. 

## Project 3: Semantic Evaluation (SEMEVAL)
The goal of the project is to evaluate the semantic of pairs of words given in input, furthermore we have to assign a similarity score to the pairs.

## Project 4: Word Sense Disambiguation (WSD)
The goal of the project is to disambiguate a polysemic word in a given sentence. I implemented the **Lesk algorithm** and disambiguate 63 polysemic word (one for each sentences). 50 out of 63 sentences are extracted from the SemCor corpus. 

## Project 5: Italian - Yoda-Italian translator (YODA)
The goal of this project is to build a translator to translate from Italian to Italian-Yodish, namely to translate an input sequence of the form **SVX** (Subject, Verb, Other) to an output sequence of the form **XSV** (Other, Subject, Verb). I implemented the **Cocke–Younger–Kasami algorithm (CKY)** and made a simple Context Free Grammar (CFG) in Chomsky Normal Form (CNF) to parse the input sequence to a tree representing its syntactic structure. The translation is made simply swapping the S subtree with the X one. The relation is available in italian only. Here some examples of translation.

|Italian             |  Italian-Yodish|
| :---         |     :---:      |
|![picture](https://github.com/fodierna/Natural-Language-Technologies/blob/master/YODA/results/it1.jpg)  |  ![picture](https://github.com/fodierna/Natural-Language-Technologies/blob/master/YODA/results/yo1.jpg)|  

|![picture](https://github.com/fodierna/Natural-Language-Technologies/blob/master/YODA/results/it2.jpg)  |  ![picture](https://github.com/fodierna/Natural-Language-Technologies/blob/master/YODA/results/yo2.jpg)|  

|![picture](https://github.com/fodierna/Natural-Language-Technologies/blob/master/YODA/results/it3.jpg)  |  ![picture](https://github.com/fodierna/Natural-Language-Technologies/blob/master/YODA/results/yo3.jpg)|


