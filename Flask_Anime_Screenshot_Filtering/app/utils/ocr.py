import easyocr
import re
from google import genai
from app.config import GEMINI_API_KEY

client = genai.Client(api_key="")
reader = easyocr.Reader(['en'])

def extract_text(image_path):
    results = reader.readtext(image_path)
    
    # group chunks by Y position to merge same-line text
    lines = {}
    for (bbox, text, _) in results:
        y = int((bbox[0][1] + bbox[2][1]) / 2)  # vertical center of bbox
        matched_line = None
        for existing_y in lines:
            if abs(existing_y - y) < 15:  # within 15px = same line
                matched_line = existing_y
                break
        if matched_line is not None:
            lines[matched_line].append(text)
        else:
            lines[y] = [text]

    # join chunks on the same line
    merged = []
    for y in sorted(lines):
        line = " ".join(lines[y])
        merged.append(line)

    return merged

def clean_text(raw_text):
    cleaned = []
    for text in raw_text:
        text = re.sub(r'@\w+', '', text)
        text = re.sub(r'[^\x00-\x7F]+', '', text)
        text = re.sub(r'^\d+[\d:KkMm\.]*$', '', text)
        text = text.strip()
        if len(text) < 4:
            continue
        cleaned.append(text)
    return cleaned

def filter_with_gemini(chunks):
    if not chunks:
        return []
    
    chunk_list = "\n".join(f"- {c}" for c in chunks)
    prompt = f"""You are analyzing text extracted via OCR from a TikTok comment section screenshot.
Your job is to find ONLY actual anime titles in the text.

Strict rules:
- Only return something if you are CERTAIN it is an anime title
- Do NOT return questions, comments, usernames, or sentences
- Do NOT return phrases like "anime name", "anime name pls"
- Do NOT return UI text like "Reply", "Hide", "Add comment", timestamps
- If you are not sure, do NOT include it
- Return ONLY clean confirmed anime titles, one per line
- If none found, return nothing



Text chunks:
{chunk_list}"""

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-lite",
            contents=prompt
        )
        lines = response.text.strip().split("\n")
        print("Gemini returned:", lines)
        return [line.strip("- ").strip() for line in lines if line.strip()]
    except Exception as e:
        print("Gemini error:", e)
        return chunks