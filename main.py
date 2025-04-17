import os
from dotenv import load_dotenv
from graph_flow import build_graph

load_dotenv()

if __name__ == "__main__":
    app = build_graph()
    print("🤖 AI Support Assistant is ready!")
    
    while True:
        msg = input("You: ")
        if msg.lower() in ["exit", "quit"]:
            print("Goodbye! 👋")
            break

        result = app.invoke({"message": msg})
        print("Bot:", result["response"])
