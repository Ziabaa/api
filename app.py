from flask import Flask
from PromptBilder.promt_bilder import PromptBuilder
from PromptBilder.db import DataBase
import pymssql

app = Flask(__name__)


@app.route('/criteria_json/<string_param>', methods=['GET', 'POST'])
def process_json(string_param):
    try:
        conn = pymssql.connect(
            host='80.73.9.240',
            user='gonchar',
            password='8c22T3xGpK',
            database='Calls'
        )

        database = DataBase(conn)

        if string_param == "calls":
            check_group_value = 4
        elif string_param == "chats":
            check_group_value = 3
        else:
            return "Invalid Parameter"

        query = """SELECT cl.Code, cl.Promt
        FROM CheckGroupLists cgl
        JOIN CheckLists cl ON cgl.CheckList = cl.id
        WHERE cgl.CheckGroup = {}
        FOR JSON PATH;""".format(check_group_value)

        rows = database.execute_query_json(query)

        res = database.formatting_to_json(rows)

        conn.close()

        return PromptBuilder().create_prompt_str(res)

    except Exception as e:
        return str(e), 500


if __name__ == '__main__':
    app.run(debug=True)
