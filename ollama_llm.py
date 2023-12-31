import os
from typing import Optional

from langchain.llms import Ollama

from embedchain.config import BaseLlmConfig
from embedchain.helper.json_serializable import register_deserializable
from embedchain.llm.base import BaseLlm


@register_deserializable
class OllamaLLm(BaseLlm):
    def __init__(self, config: Optional[BaseLlmConfig] = None):
       
        # Set default config values specific to this llm
        if not config:
            config = BaseLlmConfig()
            # Add variables to this block that have a default value in the parent class
            config.max_tokens = 500
            config.temperature = 0.75
        # Add variables that are `none` by default to this block.
        if not config.model:
            config.model = (
                "a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5"
            )

        super().__init__(config=config)

    def get_llm_model_answer(self, prompt):
        # TODO: Move the model and other inputs into config
        if self.config.system_prompt:
            raise ValueError("Llama2App does not support `system_prompt`")
        llm = Ollama(model="llama2")
        return llm._generate(prompt)
