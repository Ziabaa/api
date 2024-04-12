from flask import Flask
from PromptBilder.promt_bilder import PromptBuilder
from PromptBilder.db import DataBase
import pymssql

app = Flask(__name__)


@app.route('/criteria_json/<string_param>', methods=['GET', 'POST'])  # string_param-> calls/chats
def process_json(string_param):
    try:
        conn = pymssql.connect(
            host='80.73.9.240',
            user='gonchar',
            password='8c22T3xGpK',
            database='Calls'
        )

        database = DataBase(conn)

        res = database.execute_query_json(string_param)

        json_res = database.formatting_to_json(res)

        return PromptBuilder().create_prompt_str(json_res)

    except Exception as e:
        return str(e), 500


if __name__ == '__main__':
    app.run(debug=True)

