# 输入命令：python simple_server.py  ——————建立一个端口是8888的服务器
# 输入命令：python client.py  ———— 测试请求


getdata = {'result': 'this is a test'}


from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import time
import predict

class Resquest(BaseHTTPRequestHandler):
    def do_POST(self):
        print(self.headers)
        print(self.command)
        req_datas = self.rfile.read(int(self.headers['content-length'])) 
        print("--------------------接受client发送的数据----------------")
        res1 = req_datas.decode('utf-8')
        res_data = json.loads(res1)
        print(res_data)
        print("--------------------接受client发送的数据------------------")
        try:
            data1 = predict.perdict_stuff_info(res_data['value'])
            data = json.dumps(data1)
            print(data)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(data.encode('utf-8'))
        except:
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(getdata).encode())
        
if __name__ == '__main__':
    host = ('0.0.0.0', 8888)
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()

