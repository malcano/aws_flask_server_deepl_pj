# from tensorflow.keras.models import load_model
# import app
#
# @app.route("/model", methods=["GET"])
# def model():
# 	if request.method == "GET":
#         # 1. url을 입력으로 받아서
# 		url = request.args.get('url')
# 		# 2. url을 이미지로 변환한 후
#         image = url_to_image(url)
#         # 3. Keras 모델의 input으로 사용
# 		result_file = test_model(image)
#         # 4. json 형태로 리턴
# 		result_dict = {
# 						'url' : url,
# 						'result' : encode_image(result_file)
# 					  }
#
# 		return json.dumps(result_dict)
