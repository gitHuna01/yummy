import urllib.request
import json

# 테스트할 서버 주소
url = "http://localhost:8000/predict"

# 1. 명백한 스팸 텍스트
spam_text = "Free money! Congratulations! You've won a $1,000 Walmart gift card. Click here to claim your prize."

# 2. 일상적인 대화 (정상 텍스트)
ham_text = "Hey, are we still meeting for lunch at 12?"

def test_prediction(text_to_test):
    print(f"\n요청 텍스트: '{text_to_test}'")
    
    # 요청 데이터 준비 (JSON 형식)
    data = json.dumps({"text": text_to_test}).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})

    try:
        # 서버로 POST 요청 보내기
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            print(f"-> 예측 결과: {result['prediction']} (신뢰도: {result['confidence']*100:.2f}%)")
    except urllib.error.URLError as e:
        print(f"-> 서버 연결 실패 ({e.reason}). main.py 서버가 켜져있는지 확인해주세요!")
    except Exception as e:
        print(f"-> 기타 오류 발생: {e}")

print("FastAPI 서버에 테스트 요청을 보냅니다...")
test_prediction(spam_text)
test_prediction(ham_text)
