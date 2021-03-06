from flask import Flask, jsonify, request, make_response, abort
import os

app = Flask(__name__)

MY_URL = '/everything/api/v1/'
hello = '今天天气真好呀'
not_hello = '为什么今天天气不好呀'

# get


@app.route(MY_URL + 'tasks/get/', methods=['GET'])
def get_task():
    if not 'abc' in request.args.to_dict():
        abort(404)
    print(request.args.to_dict())  #
    return str(request.args.to_dict())

# post


@app.route(MY_URL + 'tasks/post/', methods=['POST'])
def post_task():
    print(request.json)
    if not request.json:
        abort(404)
    print('222222222')
    global hello
    hello = hello + str(request.json)
    return hello

# 404处理


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


# if __name__ == '__main__':
#     app.run()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8086)))
