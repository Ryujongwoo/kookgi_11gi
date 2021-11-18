from flask import Flask, render_template, request
# 추가로 필요한 라이브러리를 import 한다.
import datetime
# import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np

app = Flask(__name__)

# placeholder와 변수를 선언한다.
X = tf.placeholder(dtype = tf.float32, shape = [None, 4])
Y = tf.placeholder(dtype = tf.float32, shape = [None, 1])
a = tf.Variable(tf.random_normal([4, 1]), dtype = tf.float32)
b = tf.Variable(tf.random_normal([1]), dtype = tf.float32)

# 배추 가격을 예상하는 수식을 만든다.
y = tf.matmul(X, a) + b

# 학습된 모델을 불러올 객체를 초기화한다.
saver = tf.train.Saver()

# tensorflow 세션을 선언하고 변수를 초기화한다.
sess = tf.Session()
sess.run(tf.global_variables_initializer())

# 저장된 학습 모델을 restore() 함수를 사용해 읽어서 세션으로 불러온다.
saver.restore(sess, './model/saved.cpkt')

@app.route('/', methods=['GET', 'POST'])
def index():
    # 사용자가 GET 방식으로 접속하면 index.html 파일의 내용을 화면에 표시한다. => 처음 접속할 때
    if request.method == 'GET':
        return render_template('index.html')
    # 사용자가 POST 방식으로 접속하면 사용자가 입력한 데이터를 받는다. => submit 버튼을 눌러 호출하면
    if request.method == 'POST':
        avg_temp = float(request.form['avg_temp'])
        min_temp = float(request.form['min_temp'])
        max_temp = float(request.form['max_temp'])
        rain_fall = float(request.form['rain_fall'])
    
    # form에 입력된 데이터를 받아서 학습 모델에 대입할 데이터를 만든다.
    data = [[avg_temp, min_temp, max_temp, rain_fall], ]
    new_data = np.array(data, dtype = np.float32)
    result = sess.run(y, feed_dict = {X : new_data})
    # 예측된 배추 가격을 저장한다.
    price = result[0]

    # 예측된 배추 가격이 웹 문서에 출력될 수 있도록 웹 문서로 배추 가격을 넘긴다.
    return render_template('index.html', price = price)

if __name__ == '__main__':
    app.run(debug = True)












