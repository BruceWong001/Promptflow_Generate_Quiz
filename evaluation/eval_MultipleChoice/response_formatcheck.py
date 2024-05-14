
from promptflow import tool

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def response_formatcheck(validate_json: object) -> bool:
    return validate_func(validate_json,expected)

def validate_func(json_obj:object,expected_format)->bool:
    for key, value in json_obj.items():
        if key not in expected_format:
            return False
        if isinstance(expected_format[key], tuple) and expected_format[key][0] == list:
            if not isinstance(value, list):
                return False
            for item in value:
                if not validate_func(item, expected_format[key][1]):
                    return False
        elif isinstance(value, dict):
            if not validate_func(value, expected_format[key]):
                return False
        else:
            if not isinstance(value, expected_format[key]):
                return False
    return True

expected = {
    "answer": (list, {
        "Question": str,
        "Options": (list, {
            "option": str,
            "isCorrect": bool
        })
    })
}


