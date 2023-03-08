from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from konlpy.tag import Okt
import re, pickle
import numpy as np

class model:
  def __init__(self):
    self.max_len = 50
    self.stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']
    self.first_model = load_model('MH-1.0.1.h5')
    self.second_model = load_model('MH-2.0.1.h5')
    with open('tokenizer.pickle', 'rb') as handle:
      self.tokenizer = pickle.load(handle)
    self.okt = Okt()



  def sentiment_predict(self, new_sentence):

    new_sentence = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣 ]','', new_sentence)
    new_sentence = self.okt.morphs(new_sentence, stem=True) # 토큰화
    new_sentence = [word for word in new_sentence if not word in self.stopwords] # 불용어 제거
    encoded = self.tokenizer.texts_to_sequences([new_sentence]) # 정수 인코딩
    pad_new = pad_sequences(encoded, maxlen = self.max_len) # 패딩
    score = float(np.argmax(self.first_model.predict(pad_new), axis=-1)) # 예측
    return score

  def circumstance_predict(self, new_sentence):
    new_sentence = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣 ]','', new_sentence)
    new_sentence = self.okt.morphs(new_sentence, stem=True) # 토큰화
    new_sentence = [word for word in new_sentence if not word in self.stopwords] # 불용어 제거
    encoded = self.tokenizer.texts_to_sequences([new_sentence]) # 정수 인코딩
    pad_new = pad_sequences(encoded, maxlen = self.max_len) # 패딩
    score = float(np.argmax(self.second_model.predict(pad_new), axis=-1)) # 예측
    return score