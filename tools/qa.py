import ollama
from tools.transcript import get_transcript

def ask_video(url: str, question: str) -> str:
    text = get_transcript(url)

    text = text[:2000]

    response = ollama.chat(
        model='phi3',
        messages=[
            {
                'role': 'user',
                'content': f"""
Answer the question from the video.

Question:
{question}

Transcript:
{text}
"""
            }
        ],
        options={
            "num_predict": 150
        }
    )

    return response['message']['content']