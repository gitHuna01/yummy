from fastapi import FastAPI, HTTPException
from schemas import SpamPredictionRequest, SpamPredictionResponse
from predictor import spam_predictor
import logging

app = FastAPI(
    title="Spam Classification API",
    description="Hugging Face 모델을 이용한 간단한 스팸 문자/메일 분류 API",
    version="1.0.0"
)

logger = logging.getLogger(__name__)

@app.get("/")
def read_root():
    return {"message": "Spam Classification API 서버가 정상적으로 동작 중입니다. /docs 에 접속하여 API를 테스트해보세요."}

@app.post("/predict", response_model=SpamPredictionResponse)
def predict_spam(request: SpamPredictionRequest):
    try:
        # 모델 추론
        result = spam_predictor.predict(request.text)
        
        # 응답 반환
        return SpamPredictionResponse(
            text=request.text,
            prediction=result['prediction'],
            confidence=result['confidence']
        )
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(status_code=500, detail="스팸 예측 중 내부 서버 오류가 발생했습니다.")

if __name__ == "__main__":
    import uvicorn
    # uvicorn 서버 실행
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
