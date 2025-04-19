import os
from openai import OpenAI
from dotenv import load_dotenv

# Load env key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load prompt
with open("prompt.txt", "r", encoding="utf-8") as f:
    base_prompt = f.read()

# Load sample input (you can also replace this with user input)
with open("sample_input.txt", "r", encoding="utf-8") as f:
    stakeholder_input = f.read()

# Inject input into prompt
final_prompt = base_prompt.format(stakeholder_input=stakeholder_input)

# Run GPT
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": final_prompt}],
    temperature=0.3
)

output = response.choices[0].message.content

# Save output
with open("requirements_output.md", "w", encoding="utf-8") as f:
    f.write(output)

print("✅ Done. Output saved to requirements_output.md") 