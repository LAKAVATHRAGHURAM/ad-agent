# agent.py
import openai
from graph_kg import get_justification_from_kg
from vector_store import get_best_practices


import openai

#openai.api_key = "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"
openai.api_key = "your open api key"
openai.api_base = "https://openrouter.ai/api/v1"

# Then use OpenAI as normal — but it will hit OpenRouter's backend instead


with open("prompts/rewrite_prompt.txt") as f:
    BASE_PROMPT = f.read()

def generate_rewritten_ad(ad_text, tone, platform):
    try:
        justification = get_justification_from_kg(tone, platform)
        best_practices = get_best_practices(tone, platform)

        prompt = BASE_PROMPT.format(
            ad_text=ad_text,
            tone=tone,
            platform=platform,
            justification=justification,
            best_practices=best_practices
        )

        response = openai.ChatCompletion.create(  
            model="anthropic/claude-3-haiku", 
            messages=[{"role": "user", "content": prompt}]
        )
        rewritten_text = response['choices'][0]['message']['content']
        return rewritten_text, justification

    except Exception as e:
        print(f"🔥 ERROR in generate_rewritten_ad(): {e}")
        raise
