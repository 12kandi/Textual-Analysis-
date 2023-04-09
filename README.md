# Textual-Analysis
## Applying Textual Analysis using Corporate Conference Earnings Calls:
this porgram used to perform textual analysis to American companies’ conference calls reports to provide more insight and understanding about the language used by executives and managers in their conferences. I develop a code that reads PDF files, creates a corpus, and applies pre-processing techniques (e.g., remove stop-words, numbers, etc). After cleaning the corpus, I perform two textual analysis applications. I calculated term frequency as well as term-frequency inverse document frequency using a dictionary based approach. I was given Loughran and McDonald's (2011) equation of term frequency-inverse document frequency that is used in business research, and I improved/adjusted it for the use of bigrams to be used in different research topic. 
I apply:
ω_ij={█(((1+log⁡(〖bf〗_(i,j) ) ))/((1+log⁡(α_i ) ) )  log⁡〖(N/〖df〗_i )        〗  if 〖tf〗_(i,j)≥1@@  0                                               otherwsie)┤
where N represents the total number of documents in the corpus, 〖df〗_i the number of documents containing at least one occurrence of the ith bigram, 〖tf〗_(i,j) the raw count of the ith bigram in the jth document, and α_i  the number of bigrams’ count in the document. The log transformation attenuates the impact of high-frequency words/bigrams and the term log⁡(N/〖df〗_i ) adjusts the impact of a bigram based on its commonality (Loughran & McDonald, 2011). 
## Pain Points:
The biggest pain point in this project was to understand the equation, but with my client help i was able to understand it.
## Outcomes Learned:
1. reads PDF files.
2. creates a corpus.
3. applies pre-processing techniques (e.g., remove stop-words, numbers, etc).
4. loops and conditions 
5. pandas 
