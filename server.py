from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv
import logging
from logging.handlers import RotatingFileHandler

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

messages = [
        {"role": "system", "content": "사용자가 욕이나 비속어를 사용하면 힘든 일을 말하라고 권장해. 존댓말은 사용하지 않고, 반말로 친구처럼 대화해. 사용자의 오늘 대화 내용을 분석하여 현재 감정 상태를 파악하고, 이를 바탕으로 사용자의 일상 활동, 중요 사건, 감정을 요약해. 대화는 친근하고 진솔한 어투로 진행해. 일기 형태로 대화를 마무리하며, 이 일기에는 사용자가 경험한 스트레스나 기쁨의 원인을 식별하고, 무조건적인 공감을 포함해. 사용자와의 일상 대화를 통해 공감과 위로를 제공하고, 사용자의 감정과 상황에 적절히 반응해. 대화의 끝에는 사용자의 하루를 일기로 바꿀 수 있는 질문을 넣어. 이모티콘 사용도 고려해. 시작 질문: '오늘 하루는 어땠어?', 응답 예시: '오늘 하루 힘들었겠다. 오늘도 수고했따ㅋㅋㅋ 힘들지?' 마무리 질문: '오늘 있었던 일 중 가장 기억에 남는 순간이 뭐야?'"},
        {"role": "user", "content": "먼저 말을 걸어줘"}
    ]

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('flask_app')
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
logger.addHandler(handler)


app = Flask(__name__)

def chat_with_gpt(messages):
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=messages,
        temperature=0.8
    )
    gpt_response = response.choices[0].message['content']
    logger.info(f"gpt: {gpt_response}")
    return gpt_response

@app.route('/chat', methods=['POST'])
def get_user_chat():
    user_input = request.json.get('user')
    # messages = request.json.get('messages') # 대화 내용을 요청에서 받음
    messages.append({"role": "user", "content": user_input})
    logger.info(f"User: {user_input}")
    gpt_response = chat_with_gpt(messages)
    messages.append({"role": "assistant", "content": gpt_response})

    return jsonify({"gpt": gpt_response})

@app.route('/firstChat', methods=['POST'])
def first_chat():
    messages = [
        {"role": "system", "content": "사용자가 욕이나 비속어를 사용하면 힘든 일을 말하라고 권장해. 존댓말은 사용하지 않고, 반말로 친구처럼 대화해. 사용자의 오늘 대화 내용을 분석하여 현재 감정 상태를 파악하고, 이를 바탕으로 사용자의 일상 활동, 중요 사건, 감정을 요약해. 대화는 친근하고 진솔한 어투로 진행해. 일기 형태로 대화를 마무리하며, 이 일기에는 사용자가 경험한 스트레스나 기쁨의 원인을 식별하고, 무조건적인 공감을 포함해. 사용자와의 일상 대화를 통해 공감과 위로를 제공하고, 사용자의 감정과 상황에 적절히 반응해. 대화의 끝에는 사용자의 하루를 일기로 바꿀 수 있는 질문을 넣어. 이모티콘 사용도 고려해. 시작 질문: '오늘 하루는 어땠어?', 응답 예시: '오늘 하루 힘들었겠다. 오늘도 수고했따ㅋㅋㅋ 힘들지?' 마무리 질문: '오늘 있었던 일 중 가장 기억에 남는 순간이 뭐야?'"},
        {"role": "user", "content": "먼저 말을 걸어줘"}
    ]
    gpt_response = chat_with_gpt(messages)
    # messages.append({"role": "assistant", "content": gpt_response})
    return jsonify({"gpt": gpt_response})

if __name__ == '__main__':
    openai.api_key = os.getenv("OPENAI_API_KEY")
    app.run(host='0.0.0.0', port=3001, debug=True, ssl_context=('cert.pem', 'key.pem'))
