from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from konlpy.tag import Okt
import re, pickle
import numpy as np


max_len = 50
stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']

first_model = load_model('MH-1.0.1.h5')
second_model = load_model('MH-2.0.1.h5')

with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

okt = Okt()
def sentiment_predict(new_sentence):
  new_sentence = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣 ]','', new_sentence)
  new_sentence = okt.morphs(new_sentence, stem=True) # 토큰화
  new_sentence = [word for word in new_sentence if not word in stopwords] # 불용어 제거
  encoded = tokenizer.texts_to_sequences([new_sentence]) # 정수 인코딩
  pad_new = pad_sequences(encoded, maxlen = max_len) # 패딩
  score = float(np.argmax(first_model.predict(pad_new), axis=-1)) # 예측
  if score == 0:
    return '불안'
  elif score == 1:
    return '분노'
  elif score == 2:
    return '상처'
  elif score == 3:
    return '슬픔'
  elif score == 4:
    return '기쁨'