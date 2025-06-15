import os
from dotenv import load_dotenv
from graph.workflow_graph import build_graph

# Load environment variables
load_dotenv()

def main():
    print("🛒 Product Recommendation System (LangGraph + Tavily + OpenAI)")
    user_query = input("🔍 Enter your product query: ")

    initial_state = {
        "query": user_query,
        "amazon_results": [],
        "flipkart_results": [],
        "tatacliq_results": [],
        "recommendations": [],
        "summary": ""
    }

    graph = build_graph()
    result = graph.invoke(initial_state)

    print("\n✅ Final Summary:\n")
    print(result["summary"])

if __name__ == "__main__":
    main()