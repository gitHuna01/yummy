# 1. 가볍고 최적화된 python 3.11 slim 버전 사용
FROM python:3.11-slim

# 2. 파이썬 및 캐시 환경변수 설정
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    HF_HOME=/app/.cache/huggingface

# 3. 컨테이너 내부 작업 디렉토리 설정
WORKDIR /app

# 4. 보안을 위한 내부 사용자 생성 (root 권한 피하기)
RUN groupadd -r appuser && useradd -r -g appuser appuser

# 5. 캐시 최적화를 위해 의존성 목록만 먼저 복사
COPY requirements.txt .

# 6. 의존성 설치 
# ⭐️ 중요 최적화: PyTorch CPU 전용 버전을 설치하여 이미지 크기를 3GB -> 수백 MB로 극적 감축
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu && \
    pip install --no-cache-dir -r requirements.txt

# 7. AI 모델 로딩 시간을 0초로 만들기 위한 빌드 타임 선행 다운로드
# (이 과정에서 모델 가중치가 Docker 이미지 안에 포함되어 구동이 즉시 이루어짐)
COPY predictor.py .
RUN python -c "from predictor import spam_predictor"

# 8. 나머지 소스 코드 전체 복사
COPY . .

# 9. appuser에게 권한 부여 및 사용자 전환
RUN chown -R appuser:appuser /app
USER appuser

# 10. 포트 노출
EXPOSE 8000

# 11. 서버 실행 명령어
CMD ["python", "main.py"]
