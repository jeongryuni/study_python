# https://ocr.space/OCRAPI
# K84721216288957
# https://api.ocr.space/parse/imageurl?apikey=&url=
# https://api.ocr.space/parse/imageurl?apikey=&url=&language=&isOverlayRequired=true

import requests

url = 'https://api.ocr.space/parse/imageurl?apikey=K84721216288957&url=https://i.pinimg.com/474x/34/8b/c5/348bc51a10af4a96dea207318f88cc6b.jpg&language=kor&isOverlayRequired=true'
response = requests.get(url) #요청.요청방식() get은 요청방식, 브라우저 주소창이라고 생각하면 된다.
response.raise_for_status() # 요청이 성공적으로 이루어졌는지 확인하고, 만약에 오류가 있다면 예외를 발생

result = response.json() # <class 'dict' > API의 응답을 JSON 형식으로 파싱합니다.
print(type(result))
print(result['ParsedResults'][0]['ParsedText'])
# OCR.Space API에서 받아온 결과의 첫 번째(ParsedResults 배열의 첫 번째 요소)
# OCR 결과의 텍스트를 출력하는 부분