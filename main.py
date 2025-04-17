from dotenv import load_dotenv
load_dotenv()

from graph_flow import build_graph

if __name__ == "__main__":
    app = build_graph()
    print("🤖 AI Support Assistant is ready! Type your query below:")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye! 👋")
            break
        result = app.invoke({"message": user_input})
        print("Bot:", result["response"])
