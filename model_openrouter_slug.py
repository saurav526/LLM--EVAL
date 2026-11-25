"""
The 5 models under test, as Groq model IDs.
Kept as a list of (display_name, model_id) so output tables show friendly names.
(File name kept as-is so existing imports keep working.)
"""
# IT main aim to bring the model slugs into one place, so if we want to add/remove models, we can do it here and not in main.py

MODELS = [
    ("GPT-OSS 120B",    "openai/gpt-oss-120b"),
    ("GPT-OSS 20B",     "openai/gpt-oss-20b"),
    ("Qwen3.8 27B",     "qwen/qwen3.8-27b"),
    ("Llama 3.3 70B",   "llama-3.3-70b-versatile"),
    ("Llama 3.1 8B",    "llama-3.1-8b-instant"),
]

if __name__ == "__main__":
    print(f"{len(MODELS)} models under test:")
    for name, slug in MODELS:
        print(f"  {name:18s} -> {slug}")
