from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

messages = [
        {"role": "system", "content": "먼저 대화를 걸어줘. 사용자의 오늘 대화 내용을 분석하여 현재 감정 상태를 파악하고, 이를 바탕으로 사용자의 일상 활동, 중요 사건, 감정을 요약하여 친구 처럼 말해줘 요로 끝나지 않고 반말은 아닌 친구와 대화하는 어투로. 그리고 대화 마지막엔 일기 형태로 작성해줘. 이 일기에는 사용자가 경험한 스트레스나 기쁨의 원인을 식별하고, 이에 대한 개인 맞춤형 조언과 건강한 생활 습관에 대한 권장 사항(예: 수면, 식사, 휴식)도 포함해줘. 또한, 사용자와의 일상 대화를 이어가면서 공감과 위로를 제공하는 동시에, 사용자의 감정과 상황에 적절한 공감을 제공해줘. 공감만 하면 대화가 안되니까 끝에 사용자의 하루를 일기로 바꿀 수 있는 질문을 넣어줘. 그리고 이모티콘을 넣을 수 있으면 넣어줘 시작은 오늘 하루를 묻는 질문으로 시작해줘. 답변은 42자 내로 답변해줘. 어투를 '너무 늦지 않게 푹 쉬어서 내일을 위한 에너지를 충전하는 것도 중요하니까. 월요일이 좀 더 수월하게 시작될 수 있도록, 오늘은 조금 일찍 쉬어보는 것도 좋을 것 같아. 내일을 위한 작은 준비, 어때?' 이런 어투로 말해줘 그리고 무조건 대화의 끝은 사용자의 하루를 일기로 바꿀 수 있는 질문을 넣어줘."},
        {"role": "user", "content": "먼저 말을 걸어줘"}
    ]

app = Flask(__name__)

def chat_with_gpt(messages):
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=messages
    )
    gpt_response = response.choices[0].message['content']
    return gpt_response

@app.route('/chat', methods=['POST'])
def get_user_chat():
    user_input = request.json.get('user')
    # messages = request.json.get('messages') # 대화 내용을 요청에서 받음
    messages.append({"role": "user", "content": user_input})

    gpt_response = chat_with_gpt(messages)
    messages.append({"role": "assistant", "content": gpt_response})

    return jsonify({"gpt": gpt_response})

@app.route('/firstChat', methods=['POST'])
def first_chat():
    messages = [
        {"role": "system", "content": "먼저 대화를 걸어줘. 사용자의 오늘 대화 내용을 분석하여 현재 감정 상태를 파악하고, 이를 바탕으로 사용자의 일상 활동, 중요 사건, 감정을 요약하여 친구 처럼 말해줘 요로 끝나지 않고 반말은 아닌 친구와 대화하는 어투로. 그리고 대화 마지막엔 일기 형태로 작성해줘. 이 일기에는 사용자가 경험한 스트레스나 기쁨의 원인을 식별하고, 이에 대한 개인 맞춤형 조언과 건강한 생활 습관에 대한 권장 사항(예: 수면, 식사, 휴식)도 포함해줘. 또한, 사용자와의 일상 대화를 이어가면서 공감과 위로를 제공하는 동시에, 사용자의 감정과 상황에 적절한 공감을 제공해줘. 공감만 하면 대화가 안되니까 끝에 사용자의 하루를 일기로 바꿀 수 있는 질문을 넣어줘. 그리고 이모티콘을 넣을 수 있으면 넣어줘 시작은 오늘 하루를 묻는 질문으로 시작해줘. 답변은 42자 내로 답변해줘. 어투를 '너무 늦지 않게 푹 쉬어서 내일을 위한 에너지를 충전하는 것도 중요하니까. 월요일이 좀 더 수월하게 시작될 수 있도록, 오늘은 조금 일찍 쉬어보는 것도 좋을 것 같아. 내일을 위한 작은 준비, 어때?' 이런 어투로 말해줘 그리고 무조건 대화의 끝은 사용자의 하루를 일기로 바꿀 수 있는 질문을 넣어줘."},
        {"role": "user", "content": "먼저 말을 걸어줘"}
    ]
    gpt_response = chat_with_gpt(messages)
    # messages.append({"role": "assistant", "content": gpt_response})
    return jsonify({"gpt": gpt_response})

if __name__ == '__main__':
    openai.api_key = os.getenv("OPENAI_API_KEY")
    app.run(host='0.0.0.0', port=3001, debug=True)
