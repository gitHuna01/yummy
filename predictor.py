from transformers import pipeline

# 이 모델은 가볍고 SMS 스팸 분류에 최적화된 작은 BERT 모델입니다.
MODEL_NAME = "mrm8488/bert-tiny-finetuned-sms-spam-detection"

class SpamPredictor:
    def __init__(self):
        # 텍스트 분류를 위한 파이프라인 초기화
        self.classifier = pipeline("text-classification", model=MODEL_NAME)

    def predict(self, text: str) -> dict:
        # 단일 텍스트에 대한 추론 수행
        results = self.classifier(text)
        best_result = results[0]
        
        # 모델의 출력 라벨을 좀 더 읽기 쉬운 형태로 변환
        label = best_result['label'].lower()
        if label == 'label_0':
            label = 'ham (정상)'
        elif label == 'label_1':
            label = 'spam (스팸)'
            
        return {
            "prediction": label,
            "confidence": best_result['score']
        }

# 싱글톤으로 유지하여 여러 요청에서 모델을 재사용
spam_predictor = SpamPredictor()
