# 파일명: server.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/gps', methods=['POST'])
def receive_gps():
    try:
        data = request.get_json()
        lat = data['lat']
        lng = data['lng']
        
        # Render 서버의 로그에 이 메시지가 출력됩니다.
        print(f"✅ GPS 좌표 수신 성공! 위도: {lat}, 경도: {lng}")
        
        return jsonify({"status": "success", "message": "Coordinates received by Render server."})
    
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        return jsonify({"status": "error", "message": str(e)}), 400

# 서버를 직접 실행할 때만 동작하는 부분 (Render에서는 사용되지 않음)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)