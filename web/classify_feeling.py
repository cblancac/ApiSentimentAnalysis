from flask_restful import Resource
from flask import request, jsonify
from db_string import users
from helper import verify_credentials, generate_return_dictionary, count_tokens
import requests
import subprocess
import json
import numpy as np
from tensorflow.keras.models import load_model

from bert_keras import BertEmbedder


class ClassifyFeeling(Resource):
    def post(self):
        posted_data = request.get_json()

        user_name = posted_data["user_name"]
        password = posted_data["password"]
        text_input = posted_data["text"]
        MAX_SEQ_LENGTH = 32

        bert_embedder = BertEmbedder(False, # False if you don't have gpu, True in another case
                             spacy_nlp_model_name='en_core_web_lg',
                             max_seq_length=MAX_SEQ_LENGTH,
                             sentence_splitting=False,
                             padding='left')


        return_json, error = verify_credentials(user_name, password)
        print(return_json)
        if error:
            return return_json

        tokens = count_tokens(user_name)

        print("\n")
        print("\n")
        print(tokens)
        print("\n")


        if tokens <= 0:
            return generate_return_dictionary(303, "You are out of tokens, please refill! ")

        # Calculate the feeling of the sentence
        model = load_model('gru+cnn_10000.hdf5')

        text_input = text_input.split('|')
        text_input = [s.strip() for s in text_input]

        test_emb_arr_list = []
        for text in text_input:
            emb_arr = bert_embedder.get_bert_array(text)
            test_emb_arr_list.append(emb_arr)

        test_tensor = np.array(test_emb_arr_list)
        # feeling_value is a number between 0 and 1, the colser to one, the more positive is the feeling of the sentence
        feeling_value = model.predict(test_tensor)

        retJson = {
            "status": 200,
            "feeling": str(feeling_value[0][0]),
            "msg": "Feeling of the sentence calculated succesfully"
        }

        users.update_one({
            "user_name": user_name
        }, {
            "$set": {
                "token": tokens-1
            }
        })

        return jsonify(retJson)
