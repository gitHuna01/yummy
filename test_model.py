from predictor import spam_predictor

print("\n[AI 모델 테스트 진행]")
print("=============================")
test_text_1 = "Congratulations! You've won a $1,000 Walmart gift card. Click here to claim your prize."
result_1 = spam_predictor.predict(test_text_1)
print(f"문자내용: {test_text_1}\n결과: {result_1}\n")

test_text_2 = "Hey, are you coming to the party tonight?"
result_2 = spam_predictor.predict(test_text_2)
print(f"문자내용: {test_text_2}\n결과: {result_2}\n")

print("=============================")
print("모델이 성공적으로 로드되고 예측을 완료했습니다!")
