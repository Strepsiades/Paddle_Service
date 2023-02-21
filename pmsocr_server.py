# paddle脚本
import predict
import json

from flask import Flask, request, abort, Response
# 创建应用实例
app = Flask(__name__)
# 激活上下文
ctx = app.app_context()
ctx.push()
# 视图函数（路由）
@app.route('/pmsocr/stuff_info_table/', methods = ["POST"])
def stuff_info_table():
	try:
		data = request.get_data().decode()
		data_json = json.loads(data)['value']
		data1 = predict.perdict_stuff_info(data_json)
		res = Response(json.dumps(data1).encode('utf-8'), status = 200)
		res.headers['msg'] = 'success'
		return res
	except Exception as e:
		res = Response('request fail', status = 200)
		res.headers['msg'] = str(e)
		abort(res)

	
# 启动实施（只在当前模块运行）
if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = '8888')
