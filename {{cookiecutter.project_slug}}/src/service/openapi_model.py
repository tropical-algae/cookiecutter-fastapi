import re
from functools import partial
from logging import Logger
from typing import Union

from openai import OpenAI

from app.core.config import Setting
from utils.util import load_yaml


class ChatGPT:
    def __init__(self, setting: Setting) -> None:
        self.setting: Setting = setting
        self.prompt: str = self._load_prompt()
        self.client = OpenAI(base_url=setting.GPT_BASE_URL, api_key=setting.GPT_API_KEY)

    def _load_prompt(self) -> str:
        return load_yaml(self.setting.GPT_PROMPT_TEMPLATE_PATH)["instruct"]

    def _set_prompt(self, input: Union[dict, str]) -> str:
        def replacer(match, params: dict):
            var_name = match.group(1)
            return params.get(var_name, match.group(0))

        def standardization(params: Union[dict, str]) -> dict:
            params = {"data": params} if isinstance(input, str) else input
            return {k: str(v) for k, v in params.items()}

        # def complete_params(params: dict):
        #     return {**self.setting["INPUT_DEFAULT_PARAMS"], **params}

        # params = complete_params({"input": input}) if isinstance(input, str) else complete_params(input)
        params = standardization(input)
        pattern = re.compile(r"\$\{(\w+)\}")
        return pattern.sub(partial(replacer, params=params), self.prompt)

    def _inference(self, input: str) -> str:
        messages = [
            {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
            {"role": "user", "content": input},
        ]
        response = self.client.chat.completions.create(
            messages=messages,  # type: ignore
            model=self.setting.GPT_MODEL,
            temperature=self.setting.GPT_TEMPERATURE,
            response_format=self.setting.GPT_RESPONSE_FORMAT,
        )
        return response.choices[0].message.content


class EventExtraGPT(ChatGPT):
    def __init__(self, setting: Setting, logger: Logger) -> None:
        super().__init__(setting)
        self.logger = logger

    def run(self, input: dict) -> str:
        self.logger.info(f"Loading prompt for input: {input}")
        prompt = self._set_prompt(input)

        self.logger.info("The GPT is processing data...")
        output = self._inference(prompt)

        self.logger.info(f"GPT output: {output}")
        return output
