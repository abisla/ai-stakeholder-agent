# 🧠 AI Stakeholder-to-Requirements Agent
![Python](https://img.shields.io/badge/Python-3.11-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-purple)
![License](https://img.shields.io/badge/License-MIT-green)

### Built by Amar Bisla — Business Analyst × AI Systems Builder

This AI agent converts messy stakeholder conversations into:
- ✅ High-level business requirements
- ✅ Functional & non-functional requirements
- ✅ User stories (JIRA-style)
- ✅ Acceptance criteria
- ✅ Risks, constraints, assumptions

What used to take hours in a BRD now takes under 1 minute.

## 💡 Why This Matters

Most Business Analysts waste hours translating messy emails, voice notes, or meetings into clean, structured requirements.  
This agent automates that step — turning chaos into Jira-ready user stories, acceptance criteria, and BRD-style docs in minutes.
---

## 🚀 Demo Flow

### 🗣️ Sample Input (Meeting Notes)
[Stakeholder: Sarah – Product Manager] Yeah, so we've had a lot of user complaints around the checkout experience. People are dropping off at the last step... [BA: Amar] Okay. So to recap: we're tackling abandonment, clarity, A/B testing needs, security upgrades...

## 📄 Sample Output

```markdown
**User Story:**  
As a customer, I want to update my payment method after placing an order so I can fix mistakes before the order is shipped.

**Acceptance Criteria:**  
- Given an order has been placed, when the customer clicks "Edit Payment Method", then they are allowed to update their payment info  
- All changes are logged with a timestamp and user ID  
---

## ⚙️ How It Works

- Uses GPT-4 via OpenAI API
- Prompt engineered for structured output
- Inputs: `sample_input.txt` (stakeholder notes)
- Outputs: `requirements_output.md` (ready-to-use format)
- Prompt stored in `prompt.txt`

## 🛠️ Tech Stack

- 🧠 **GPT-4 via OpenAI API** – core of the language understanding + generation
- 🐍 **Python 3.11** – lightweight scripting for logic and I/O
- 📁 **dotenv** – secure storage of your API key
- 💬 **CLI interface** – fast, no-dependency setup to run in terminal
- 📄 **File I/O structure** – uses `.txt` files for easy integration, versioning, and debugging

### Run It Locally:

## 1. Install Dependencies ##
pip install openai python-dotenv
python main.py

## 2. Create .env file ## 
You'll need to set your OpenAI key in a .env file:

OPENAI_API_KEY=sk-...
## 3. Check the input files ## 
prompt.txt → the instructions sent to GPT

sample_input.txt → raw stakeholder input
## 4. Run the main.py file ## 
python main.py

## 5. Check the output ##
### Business Requirements:
1. Improve the user-friendliness of the payment screen.
2. Speed up the payment process.
3. Reduce the number of steps required to complete a transaction.
4. Implement a feature to save payment information for returning customers.
5. Enable easy access to payment history for mobile app users.
6. Speed up receipt generation.

### Functional Requirements:
1. The system should allow users to save their payment information for future transactions.
2. The system should provide an option for users to view their payment history.
...

### Non-Functional Requirements:
1. The system should be user-friendly and intuitive.
2. The system should be able to handle high traffic during peak hours without compromising on speed or performance.
...

### User Stories:
1. As a user, I want to save my payment information, so that I can complete transactions faster in the future.
2. As a mobile app user, I want to easily view my payment history, so that I can keep track of my purchases.
...

### Acceptance Criteria:
1. When a user completes a transaction, they should have the option to save their payment information for future use.
2. Mobile app users should be able to access their payment history from the main menu.
...

### Risks, Constraints, Assumptions:
- Risks: There is a risk of security breaches as we're dealing with sensitive payment information. There's also a risk of system failure during peak hours if the system can't handle high traffic.
- Constraints: The system's performance during peak hours and the speed of receipt generation may be constrained by our current server capacity.
- Assumptions: We assume that adding multiple payment methods will satisfy user requests and that saving payment information will make the transaction process faster and more convenient for returning customers.
requirements_output.md

## 🚀 Let's Talk

I built this because I was tired of rewording stakeholder chaos into clean documentation by hand.

This agent is what I wish I had as a Business Analyst on Day 1.

📩 Want a custom version for your team? Or curious how this could fit into your workflow?  
**DM me on LinkedIn or fork the repo and let's connect.**

## 📄 Files

| File | Description |
|------|-------------|
| main.py | Runs the agent |
| prompt.txt | Prompt instructions |
| sample_input.txt | Messy stakeholder input |
| requirements_output.md | Final structured output |
| LICENSE | MIT License w/ credit |
| .env | Your API key (not committed) | 
