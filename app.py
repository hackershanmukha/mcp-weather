import asyncio
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPClient, MCPAgent

# Load environment variables (GROQ_API_KEY)
load_dotenv()

async def run_memory_chat():
    # Path to the MCP servers configuration file
    config_file = "browser_mcp.json"

    # Initialize the MCP client with the server configuration
    client = MCPClient(config_file)

    # Initialize the Groq LLM model with an active model on your account
    llm = ChatGroq(model_name="openai/gpt-oss-120b")

    # Create the MCP Agent with conversation memory enabled
    agent = MCPAgent(
        llm=llm,
        client=client,
        max_steps=15,
        memory_enabled=True,
    )

    print("--- MCP AI Assistant Initialized ---")
    
    # Interactive CLI conversation loop
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        # Run the agent with user prompt
        response = await agent.run(user_input)
        print(f"\nAssistant: {response}")

if __name__ == "__main__":
    asyncio.run(run_memory_chat())
