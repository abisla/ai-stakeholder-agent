# 🧠 AI Stakeholder-to-Requirements Agent

### Built by Amar Bisla — Business Analyst × AI Systems Builder

This AI agent converts messy stakeholder conversations into:
- ✅ High-level business requirements
- ✅ Functional & non-functional requirements
- ✅ User stories (JIRA-style)
- ✅ Acceptance criteria
- ✅ Risks, constraints, assumptions

What used to take hours in a BRD now takes under 1 minute.

---

## 🚀 Demo Flow

### 🗣️ Sample Input (Meeting Notes)
[Stakeholder: Sarah – Product Manager] Yeah, so we've had a lot of user complaints around the checkout experience. People are dropping off at the last step... [BA: Amar] Okay. So to recap: we're tackling abandonment, clarity, A/B testing needs, security upgrades...

### 📄 Output
Generated requirements are available in [`requirements_output.md`](./requirements_output.md)

---

## ⚙️ How It Works

- Uses GPT-4 via OpenAI API
- Prompt engineered for structured output
- Inputs: `sample_input.txt` (stakeholder notes)
- Outputs: `requirements_output.md` (ready-to-use format)
- Prompt stored in `prompt.txt`

### Run It Locally:

```bash
pip install openai python-dotenv
python main.py
```

You'll need to set your OpenAI key in a .env file:

```ini
OPENAI_API_KEY=sk-...
```

## 📄 Files

| File | Description |
|------|-------------|
| main.py | Runs the agent |
| prompt.txt | Prompt instructions |
| sample_input.txt | Messy stakeholder input |
| requirements_output.md | Final structured output |
| LICENSE | MIT License w/ credit |
| .env | Your API key (not committed) | 