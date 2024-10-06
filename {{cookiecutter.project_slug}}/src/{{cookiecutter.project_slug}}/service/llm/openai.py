from typing import Optional

from {{cookiecutter.project_slug}}.common.logging import logger
from {{cookiecutter.project_slug}}.service.llm.base import OpenAIBase


class EventExtraGPT(OpenAIBase):
    async def run(self, input: dict, model: Optional[str] = None, **kwargs) -> str:
        logger.info(f"Loading prompt for input: {input}")
        content = self._set_prompt(input)

        logger.info("The GPT is processing data...")
        output = await self._async_inference(content=content, model=model, **kwargs)

        logger.info(f"GPT output: {output}")
        return output
