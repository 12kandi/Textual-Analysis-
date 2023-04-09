import nltk
from nltk import word_tokenize
from nltk.util import ngrams
import math
from nltk.corpus import stopwords
import pandas as pd
import re

df = pd.read_feather()     ## insert the data-text 
library= ['abc analysis', 'abc classification', 'active Inventory', 'advanced shipping', 'aggregate inventory', 'allocated stock', 'anticipation stock', 'available stock', 'available promise', 'economic repair', 'bar code', 'batch number', 'bill material', 'buffer stock', 'build stock', 'build order', 'category management', 'central distribution', 'distribution centre', 'managed inventory', 'component part', 'composite delivery', 'composite distribution', 'consignment stock', 'consolidation centres', 'cost serve', 'cross docking', 'coupling stock', 'deduct point', 'demand forecast', 'demand driven', 'driven supply', 'demand satisfaction', 'satisfaction rate', 'denomination quantity', 'dependent demand', 'deterministic inventory', 'inventory control', 'direct store', 'store delivery', 'distribution requirement', 'distribution resource', 'resource planning', 'economic order', 'order interval', 'expression interest', 'order quantity', 'economic stock', 'effective stock', 'efficient consumer', 'consumer response', 'electronic commerce', 'electronic data', 'data interchange', 'enterprise requirement', 'european article', 
'article numbering', 'excess stock', 'factory gate', 'gate pricing', 'family group', 'fill rate', 'finished goods', 'goods stock', 'first in', 'first out', 'stock valuation', 'stock rotation', 'first pick', 'pick rate', 'coming soon', 'process goods', 'in process', 'inactive inventory', 'free carrier', 'alongside ship', 'free board', 'cost freight', 'cost insurance', 'insurance freight', 'carriage paid', 'carriage insurance', 'delivered frontier', 'delivered duty', 'duty unpaid', 'duty paid', 'integrated business', 'independent demand', 'intermediate product', 'intermediate stock', 'inventory control', 'inventory modeling', 'inventory policy', 'inventory process', 'inventory records', 'inventory shrinkage', 'inventory usage', 'issue list', 'based supply', 'chain development', 'issue tickets', 'issuing documents', 'item number', 'location checking', 'lost sales', 'material requirements', 
'manufacturing resource', 'make order', 'make stock', 'materials management', 'matrix bar', 'bar code', 'maximum stock', 'maximum order', 'minimum order', 'minimum stock', 'obsolete stock', 'obsolescent stock', 'shelf satisfaction', 'off shoring', 'opening stock', 'lead time', 'order picking', 'order point', 'inventory system', 'parent part', 'pareto principle', 'part number', 'perpetual inventory', 'periodic inventory', 'pick face', 'picking list', 'pipeline stocks', 'primary freight', 'primary transport', 'probabilistic inventory', 'product group', 'production lead', 'proof delivery', 'purchasing price', 'pull system', 'purchasing lead', 'purchase price', 'push system', 'quarantine stock', 'radio frequency', 'frequency identification', 'cycle counting', 'random sample', 'rapid acquisition', 'manufactured parts', 'raw material', 'redundant stock', 'regional distribution', 'repair turn', 'round time', 'repairable period', 'repairable item', 'repair period', 'replenishment order', 'reorder costs', 'replenish demand', 'buying alignment', 'reverse logistics', 'review interval', 'rounding order', 'safety stock', 'sales forecast', 'sample stability', 'seasonal stock', 'secondary transport', 'selective inventory', 'service differentiation', 'ready packaging', 'stock site', 'stock turn', 'stock turnover', 'stock types', 'strategic stock', 'supply chain', 'chain sustainability', 'time serve', 'acquisition cost', 'transit time', 'turn around', 'unit cost', 'unit measure', 'vendor hub', 'vendor managed', 'wiggle factor', 'yard management']
tf_list=[]
tf_idf_list=[]

gd_in_doc=0
stopwords_list=set(stopwords.words("english"))

how_many_para=0
for i in df.index:
    paragraph=df['paragraph'][i]
    paragraph=re.sub(r'[^\w\s]', ' ',paragraph)     #remove punctuations
    paragraph=re.sub(" \d+", " ", paragraph)        #remove digits
    paragraph=paragraph.lower()                     #lower case
    pattern = re.compile(r'\b(' + r'|'.join(stopwords.words('english')) + r')\b\s*')    #remove stop words
    paragraph= pattern.sub('', paragraph)         #remove stop words
    paragraph=paragraph.replace("-"," ")
    paragraph=paragraph.replace("_"," ")
    paragraph=paragraph.replace("\""," ")
    paragraph=re.sub(r'[^ \w\.]', ' ', paragraph)   #remove /n/r it means remove new line character hidden in html.
    paragraph=re.sub('(\\b[A-Za-z] \\b|\\b [A-Za-z]\\b)', '', paragraph)  #remove one letter left
    paragraph=re.sub(' +', ' ',paragraph)   #remove white spaces
    


    how_many_para=how_many_para+1 # it count how many docaments in the whole stata file.
    
    gd_words=0
    gd="false"
########################################################################### 
# tokenize paragraph to bigrams    
    paragraph_split_bigrams=[]
    token = word_tokenize(paragraph)
    bigrams = list(ngrams(token, 2))
    # one_word=paragraph.split()
    for bi in bigrams:
        bigram=" ".join(bi)
        paragraph_split_bigrams.append(bigram)
###############################################################################  
# check if there are match bigrams in each docament
# count matched bigrams for each docament  
    
    for bigram__ in paragraph_split_bigrams:
            for gd_ in library:
                if gd_ == bigram__:
                    gd="true"
                    gd_words=gd_words+1    #this is to count how many bigrams in each docaments "insider docaments"
    if gd=="true":
            gd_in_doc=gd_in_doc+1   #this is to count how many docaments in the whole stata file "outer file" that have at least one bigram.

    
    if gd_words>=1: # this is to check if there is at least one matched bigrams within docament "insider docament"
        #if there is, then it will do the calculation
        tf= ( 1 + math.log10 (gd_words))/(1 + math.log10(len(paragraph_split_bigrams) ))
        tf_list.append(tf)
    else:
         #if there is, then tf=0
        tf=0
        tf_list.append(tf)
       

idf=math.log10(how_many_para/gd_in_doc)
for tf in tf_list:
    

            tf_idf=tf*(idf)
            tf_idf_list.append(tf_idf)


df.insert(2,"tf_idf", tf_idf_list, True)
df.insert(3,"tf_list",  tf_list, True)
df=df.drop(columns=['paragraph'])


df.to_csv("df_2008_supplyChain_bigram_C.csv")
print("done done")