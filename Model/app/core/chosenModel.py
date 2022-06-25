
import joblib
import threading
import numpy as np
class ChosenModel(threading.Thread):

    def __init__(self):
        """[Constructor]
        """
        pass

    def predict(self,author,num_page,ratings_cout,text_review_count,publisher):
        joblib_model_reg = joblib.load('/modeldata/reg_1.sav')
        joblib_encoderAuthor = joblib.load('/modeldata/labelEncodeAuthor.joblib')
        joblib_encoderPublisher = joblib.load('/modeldata/labelEncodePublisher.joblib')
        author= joblib_encoderAuthor.transform([author])[0]
        publisher = joblib_encoderPublisher.transform([publisher])[0]

        #X=myarray.array('d',[num_page,ratings_cout,text_review_count,author,publisher]).reshape(-1, 1)
        X= np.array([num_page,ratings_cout,text_review_count,publisher,author])

        #X=[num_page,ratings_cout,text_review_count,author,publisher].reshape(-1, 1)



        a=joblib_model_reg.predict(X.reshape(1,-1))[0]

        return a



        return

