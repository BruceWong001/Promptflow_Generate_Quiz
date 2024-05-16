from typing import Dict, Any, List
from promptflow import tool
import json
from jsonschema import validate, ValidationError


# 定义 answer 字段的 schema
answer_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "Question": {"type": "string"},
            "Options": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "option": {"type": "string"},
                        "isCorrect": {"type": "boolean"}
                    },
                    "required": ["option", "isCorrect"]
                }
            }
        },
        "required": ["Question", "Options"]
    }
}

@tool
def validate_response_format(response: str) -> bool:
    # 加载 JSON 内容
    data = json.loads(response)

    # 验证 answer 字段是否符合 schema
    try:
        validate(instance=data, schema=answer_schema)
        return True
    except ValidationError as e:
        print(e.message)
        return False

