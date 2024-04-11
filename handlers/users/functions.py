import requests
from data.config import GEMINI_API
import google.generativeai as genai



genai.configure(api_key=GEMINI_API)

# Set up the model
def gemini_ai(text):
    generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
    }
    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    ]
    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                generation_config=generation_config,
                                safety_settings=safety_settings)

    convo = model.start_chat(history=[
    ])
    convo.send_message(text)
    return convo.last.text



def count_time(number):
    barcha_xabarlar_uchun_vaqt = number * 0.8
    soatlar = barcha_xabarlar_uchun_vaqt // 3600
    qoldiq_sekundlar = barcha_xabarlar_uchun_vaqt % 3600
    daqiqalar = qoldiq_sekundlar // 60
    qoldiq_sekundlar = qoldiq_sekundlar % 60
    return int(soatlar), int(daqiqalar), int(qoldiq_sekundlar)
