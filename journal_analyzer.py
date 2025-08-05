import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
client = OpenAI()

def analyze_journal(entry: str, depth: str = "brief") -> str:
    """Analyze mood and themes in a journal entry."""
    valid_depths = ["brief", "detailed"]
    if depth not in valid_depths:
        return f"Error: Invalid depth. Choose from {valid_depths}."
    if not entry.strip():
        return "Error: Empty journal entry provided."

    try:
        prompt = f"Analyze the mood and themes in this journal entry ({depth} analysis):\n\n{entry}"
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200 if depth == "brief" else 400
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error analyzing journal: {str(e)}"

# Example usage
if __name__ == "__main__":
    journal_entry = "I felt nervous before my presentation but relieved after."
    print("Brief Analysis:")
    print(analyze_journal(journal_entry, depth="brief"))
    print("\nDetailed Analysis:")
    print(analyze_journal(journal_entry, depth="detailed"))