import socket
import json

def get_minecraft_server_status(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)  # タイムアウト時間を設定
            s.connect((host, port))
            s.send(b'\x00\x00\x00\x01\x00')  # プロトコルバージョンと状態リクエストを送信
            s.recv(1)  # 応答の先頭のバイトを読み取りますが、データは無視します
            data_length = ord(s.recv(1))  # 応答のデータ長を読み取り
            data = s.recv(data_length)  # データを受信
            json_data = json.loads(data.decode('utf-8'))  # JSONデータに変換
            return json_data
    except (socket.timeout, ConnectionRefusedError):
        return None

# Minecraftサーバーのホストとポートを指定
server_host = '122.208.16.184'
server_port = 25565

# サーバーのステータスを取得
status = get_minecraft_server_status(server_host, server_port)

if status:
    print("Minecraftサーバーがオンラインです。")
    print("プレイヤー数:", status['players']['online'])
else:
    print("Minecraftサーバーがオフラインか、接続に問題があります。")