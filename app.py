from flask import Flask, request, jsonify
from PromptBilder.promt_bilder import PromptBuilder

app = Flask(__name__)


# Пример обработчика для POST-запроса
@app.route('/criteria_json', methods=['POST'])
def process_json():
    # Получение JSON-объекта из запроса
    json_data = request.get_json()
    builder = PromptBuilder()
    prompt = builder.create_prompt_str(json_data)
    return prompt


if __name__ == '__main__':
    app.run(debug=True)
