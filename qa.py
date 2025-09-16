import requests

OLLAMA_URL = "http://localhost:11434"  # Adjust if Ollama runs differently

def rule_based_lookup(question, summary):
    q = question.lower()
    if "revenue" in q:
        return "Revenue found in summary (placeholder)."
    if "profit" in q:
        return "Profit found in summary (placeholder)."
    return None

def call_ollama(prompt):
    payload = {"model": "llama2", "prompt": prompt}
    r = requests.post(f"{OLLAMA_URL}/api/generate", json=payload, timeout=30)
    r.raise_for_status()
    return r.json().get("output", "No response")

def answer_question(question, summary, chat_history):
    rb = rule_based_lookup(question, summary)
    if rb:
        return rb
    context = f"Summary: {summary}\n\nUser asked: {question}"
    try:
        return call_ollama(context)
    except Exception as e:
        return f"Error contacting Ollama: {e}"
