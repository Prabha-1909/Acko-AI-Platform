from manager_ai.manager_assistant import ask_manager

questions = [
    "How many car claims are submitted?",
    "How many bike claims are submitted?",
    "How many claims are submitted?",
    "What is the average payout for bike claims?",
    "What is the average payout for car claims?",
    "How many quotations did we generate?",
    "What is the average premium?",
    "What are the top chatbot questions?",
    "Show me recent claims"
]

for q in questions:
    print("\nQ:", q)
    print("A:", ask_manager(q))