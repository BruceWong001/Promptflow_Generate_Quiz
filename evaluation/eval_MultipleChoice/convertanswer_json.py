
from promptflow import tool
import json

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def convertanswer_json(llm_answer: str) -> object:
    response_dict = {"answer": llm_answer}
    response_json = json.dumps(response_dict)
    return response_json








