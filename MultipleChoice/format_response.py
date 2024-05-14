
from promptflow import tool
import json


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(llmresponse: str) -> str:
    response_json = json.loads(llmresponse)
    # answer_value = response_json['answer']
    # formatted_answer = json.dumps(answer_value, indent=4)
    return     response_json
