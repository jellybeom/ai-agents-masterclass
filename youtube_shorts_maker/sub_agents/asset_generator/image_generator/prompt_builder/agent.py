from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from .prompt import PROMPT_BUILDER_DESCRIPTION, PROMPT_BUILDER_PROMPT
from pydantic import BaseModel, Field
from typing import List


class OptimizedPrompt(BaseModel):
    scene_id: int = Field(description="원본 콘텐츠 플랜의 장면 ID")
    enhanced_prompt: str = Field(
        description="세로형 YouTube Shorts를 위한 기술 사양과 텍스트 오버레이 지침이 포함된 상세 프롬프트"
    )


class PromptBuilderOutput(BaseModel):
    optimized_prompts: List[OptimizedPrompt] = Field(
        description="세로형 YouTube Shorts를 위한 최적화된 이미지 생성 프롬프트 배열"
    )


MODEL = LiteLlm("openai/gpt-4o")

prompt_builder_agent = Agent(
    name="PromptBuilderAgent",
    model=MODEL,
    description=PROMPT_BUILDER_DESCRIPTION,
    instruction=PROMPT_BUILDER_PROMPT,
    output_schema=PromptBuilderOutput,
    output_key="prompt_builder_output",
)
