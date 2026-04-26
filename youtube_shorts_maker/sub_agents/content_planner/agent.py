from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from .prompt import CONTENT_PLANNER_DESCRIPTION, CONTENT_PLANNER_PROMPT
from pydantic import BaseModel, Field
from typing import List


class SceneOutput(BaseModel):
    id: int = Field(description="장면 ID 번호")
    narration: str = Field(description="장면의 내레이션 텍스트")
    visual_description: str = Field(description="이미지 생성을 위한 상세 설명")
    embedded_text: str = Field(
        description="이미지에 삽입할 텍스트 오버레이 (대/소문자 및 스타일 자유)"
    )
    embedded_text_location: str = Field(
        description="이미지 내 텍스트 위치 (예: 'top center', 'bottom left', 'middle right', 'center')"
    )
    duration: int = Field(description="장면 재생 시간 (초)")


class ContentPlanOutput(BaseModel):
    topic: str = Field(description="YouTube Short의 주제")
    total_duration: int = Field(description="총 영상 재생 시간 (초, 최대 20초)")
    scenes: List[SceneOutput] = Field(
        description="장면 목록 (장면 수는 에이전트가 결정)"
    )


MODEL = LiteLlm("openai/gpt-4o")

content_planner_agent = Agent(
    name="ContentPlannerAgent",
    model=MODEL,
    description=CONTENT_PLANNER_DESCRIPTION,
    instruction=CONTENT_PLANNER_PROMPT,
    output_schema=ContentPlanOutput,
    output_key="content_planner_output",
)
