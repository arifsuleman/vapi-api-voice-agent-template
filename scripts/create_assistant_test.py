import os
from src.base.voice_agent_providers.vapi import VapiAI
from src.prompts import VOICE_AGENT_PROMPT
from dotenv import load_dotenv

load_dotenv()

assistant_config = {
    "name": "Jorden",
    "transcriber": {
        "provider": "deepgram",  # Transcriber provider
        "language": "en"
    },
    "model": {
        "provider": "openai",  # Model provider
        "model": "gpt-4o",  # Model ID
        # "toolIds": tool_ids_list,
        "messages": [
            {
                "role": "system",
                "content": VOICE_AGENT_PROMPT
            }
        ]
    },
    "voice": {
        "provider": "openai",  # Voice provider
        "voiceId": "alloy"  # Voice ID
    },
    "first_message": "Hi, is this Chris{{firstName}}?",
    "end_call_message": "Thanks for your time.",
    "analysis_plan": {
        "summaryPlan": {
            "messages": [],
            "enabled": False,
        },
        "structuredDataPlan": {
            "messages": [],
            "enabled": False,
        },
        "successEvaluationPlan": {
            "rubric": "NumericScale",
            "messages": [],
            "enabled": False
        }
    },
   
}


vapi_client = VapiAI()

# Create a new assistant using the above config
output = vapi_client.create_agent(assistant_config)
# print(output)

# # Get the assistant id, copy it to .env
assistant_id = output["details"].id
print(assistant_id)


