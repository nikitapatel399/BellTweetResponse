# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 16:22:16 2019

@author: Nikita
"""
def model(user, tweet): 
    # Imports
    import pandas as pd
    import os 
    # Read in file
    module_dir = os.path.abspath(os.path.dirname(__file__))
    data = pd.read_csv(os.path.join(module_dir,'bell.csv'), encoding='latin') 
    # Merge word frames
    import sentencecreator as sc
    data = pd.concat([data, sc.dictcompile()])
    data.to_csv('complaints.csv') 
    """
    ML
    """
    import numpy as np
    from nltk.corpus import stopwords
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.svm import LinearSVC
    from sklearn.pipeline import Pipeline
    from sklearn.model_selection import train_test_split
    from sklearn.feature_selection import SelectKBest, chi2
    stoppingwords = stopwords.words("english")
    stoppingwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your',
                     'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it',
                     "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this',
                     'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has',
                     'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until',
                     'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after',
                     'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once',
                     'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some',
                     'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don',
                     "don't", 'should', "should've", 'now', "aren't", 'couldn', "couldn't",
                     'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn',
                     "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't",
                     'won', "won't", 'wouldn', "wouldn't", 'someone']
    data['cleaned'] = data['message']
    X_train, X_test, y_train, y_test = train_test_split(data['cleaned'], data.label, test_size=0.2)
    pipeline = Pipeline([('vect', TfidfVectorizer(ngram_range=(1, 2), stop_words="english", sublinear_tf=True)),
                         ('chi',  SelectKBest(chi2, k=300)),
                         ('clf', LinearSVC(C=1.0, penalty='l1', max_iter=500, dual=False))])
    model = pipeline.fit(X_train, y_train)
    vectorizer = model.named_steps['vect']
    chi = model.named_steps['chi']
    clf = model.named_steps['clf']
    feature_names = vectorizer.get_feature_names()
    feature_names = [feature_names[i] for i in chi.get_support(indices=True)]
    feature_names = np.asarray(feature_names)
    target_names = ['billings', 'device', 'internet', 'service', 'support_complaint', 'technician', 'thanks', 'tv']
    print("top 10 keystoppingwords per class:")
    for i, label in enumerate(target_names):
        top10 = np.argsort(clf.coef_[i])[-10:]
        print("%s: %s" % (label, " ".join(feature_names[top10])))
    print("Train accuracy score: " + str(model.score(X_train, y_train)))
    print("Test accuracy score: " + str(model.score(X_test, y_test)))
    print("-------------------------------------------------------------------------------------------------")
    
    def predict(stringin):
        predictstring = stringin
        predictstring = predictstring.lower()
        return model.predict([predictstring])
    prediction_1 = predict(tweet)
    if prediction_1 == 'device':
        print("Thank you for your message ", user,". Please contact our Device support line directly at bell.ca/devices")
    elif prediction_1 == 'service':
        print("Thank you for your message ", user,". Please contact our Bell Service department directly at bell.ca/service for an update on outages")
    elif prediction_1 == 'internet':
        print("Thank you for your message ", user,". Please contact our Internet Support Services department directly at bell.ca/internet")   
    elif prediction_1 == 'billings':
        print("Thank you for your message ", user,". Please contact our Billings department directly at bell.ca/billing")  
    elif prediction_1 == 'technician':
        print("Thank you for your message ", user,". Please contact us at our Bell Technician Assistance number at 416-151-3371")
    elif prediction_1 == 'support_complaint':
        print("Thank you for your message ", user,". We are sorry we were not able to assist you as well as we hoped. Please send us a DM outlining your issue")
    elif prediction_1 == 'tv':
        print("Thank you for your message ", user,". Please contact our TV help department directly at bell.ca/tv")
    elif prediction_1 == 'thanks':
        print("Thank you for your message ", user,"! Happy to help. ")
        
    
        
