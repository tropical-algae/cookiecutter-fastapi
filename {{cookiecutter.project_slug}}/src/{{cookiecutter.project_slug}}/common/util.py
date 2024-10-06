import json
import os
import re

import yaml
from fastapi import HTTPException


def generate_filepath(filename: str, filepath: str) -> str:
    if not os.path.isdir(filepath):
        os.makedirs(filepath)
    return os.path.join(filepath, filename)


def load_yaml(yaml_path: str) -> dict:
    try:
        with open(yaml_path) as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as err:
        raise Exception(f"[YAML Reader] Error occured when read YAML from path '{yaml_path}'. Error: {err}") from err


def parse_text_2_json(text: str) -> tuple[dict[str, str], str]:
    text = text.replace("```json\n", "").replace("\n```", "").replace("\n", "")
    try:
        json_matches = re.compile(r"\{.*?\}").findall(text)
        for match in json_matches:
            text_json = json.loads(match)
            return text_json, "Successly parse text to json."
        raise HTTPException(status_code=500, detail="Exception: Can not parse text to json.")
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Exception: {err}") from err
