from src.integrations.gpt import manager
import os


gpt_manager = manager.GptIntegration(
    os.environ.get("OPENAI_KEY")
)
