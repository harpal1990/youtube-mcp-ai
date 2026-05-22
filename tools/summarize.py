import ollama
from tools.transcript import get_transcript

def summarize_video(url: str) -> str:
    text = get_transcript(url)

    # Fast mode
    text = text[:1500]

    response = ollama.chat(
        model='phi3',
        messages=[
            {
                'role': 'user',
                'content': f"""
Give a very short summary in 3 bullet points.

Content:
{text}
"""
            }
        ],
        options={
            "num_predict": 120
        }
    )

    return response['message']['content']