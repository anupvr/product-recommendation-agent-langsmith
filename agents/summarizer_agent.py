import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.7)

def summarize_agent(state: dict) -> dict:
    print("[Summarizer Agent] 📝 Finalizing summary...")
    print("[Summarizer Agent] 📦 Incoming state:")
    print(state)

    query = state.get("query", "")
    top_product = state.get("top_product")
    reasoning = state.get("reasoning")

    if not top_product:
        print("[Summarizer Agent] ❌ No top product found.")
    if not reasoning:
        print("[Summarizer Agent] ❌ No reasoning found.")

    if not top_product or not reasoning:
        summary = "No recommendation could be made for your query."
    else:
        summary = (
            f"🎯 Based on your query '{query}', here's our top recommendation:\n\n"
            f"{reasoning}\n\n"
            f"🔗 Product Link: {top_product}"
        )

    print("[Summarizer Agent] ✅ Summary generated")
    return {**state, "summary": summary}