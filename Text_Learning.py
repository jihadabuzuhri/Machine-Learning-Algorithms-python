
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
string1 = "hi Katie the self driving car will be late Best Sebastian"
string2 = "Hi Sebastian the machine learning class will be great great great Best Katie"
string3 = "Hi Katie the machine learning class will be most excellent"
email_list = [string1, string2, string3]
bag_of_words = vectorizer(email_list)
bag_of_words = vectorizer.fit(email_list)
bag_of_words = vectorizer.transform(email_list) 

###############################################

"""
import nltk
nltk.download('stopwords')
"""


from nltk.corpus import stopwords

SW = stopwords.words ("english")

print(len(SW))

for x in SW:
    print(x)






##########################################


from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")

stemmer.stem("responsiveness")


###################################################



from sklearn.feature_extraction.
 import TfidfVectorizer

vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words="english")

features_train = vectorizer.fit_transform(word_data) #.toarray()

#print(vectorizer.get_feature_names_out())


