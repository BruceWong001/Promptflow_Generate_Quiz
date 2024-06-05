from promptflow import tool
import json

@tool
def my_python_tool(llmresponse: str, totalscore: float) -> str:
    response_json = json.loads(llmresponse)

    # 添加字段和值
    response_json['Comment'] = response_json.pop('OverallComment')
    total_score = sum(item['TotalScore'] for item in response_json['QuestionRubrics'])
    given_score = sum(item['GivenScore'] for item in response_json['QuestionRubrics'])
    num_rubrics = len(response_json['QuestionRubrics'])
    if totalscore != total_score:
        response_json['TotalScore'] = totalscore
        response_json['Score'] = totalscore * given_score / total_score
    else:
        response_json['TotalScore'] = total_score
        response_json['Score'] = given_score



    return response_json
