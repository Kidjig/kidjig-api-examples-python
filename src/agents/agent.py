# KidJig API Sample Usage
# This file demonstrates how to interact with the KidJig API for managing agents and chat.

import httpx

# Base URL and headers
url = "https://api.kidjig.com/agents/api/v1"
headers = {
    "X-Api-Key": "your_api_key",  # Replace with your KidJig API key
    "Content-Type": "application/json",
}


# Create a new agent
def create_agent():
    try:
        response = httpx.post(
            f"{url}/",
            headers=headers,
            json={
                "name": "Deepak Agent",
                "description": "An agent that can answer based on user query",
                "agent_role": "You are a helpful assistant that can answer based on user query",
                "agent_instructions": "Help users with their query",
                "tools": ["Search", "Github"],
                "provider_id": "OpenAI",
                "model": "gpt-4o",
            },
        )
        response_data = response.json()
        print("Created Agent:", response_data)
    except Exception as error:
        print(f"Failed to create agent: {str(error)}")


# Get all agents
def get_agents():
    try:
        response = httpx.get(f"{url}/", headers=headers)
        response_data = response.json()
        print("All Agents:", response_data)
    except Exception as error:
        print(f"Failed to fetch agents: {str(error)}")


# Get a specific agent by ID
def get_agent_by_id(agent_id):
    try:
        response = httpx.get(f"{url}/{agent_id}", headers=headers)
        response_data = response.json()
        print("Agent Details:", response_data)
    except Exception as error:
        print(f"Failed to fetch agent {agent_id}: {str(error)}")


# Update an existing agent
def update_agent(agent_id, updated_data):
    try:
        response = httpx.put(f"{url}/{agent_id}", headers=headers, json=updated_data)
        response_data = response.json()
        print("Updated Agent:", response_data)
    except Exception as error:
        print(f"Failed to update agent {agent_id}: {str(error)}")


# Delete an agent by ID
def delete_agent(agent_id):
    try:
        response = httpx.delete(f"{url}/{agent_id}", headers=headers)
        response_data = response.json()
        print("Deleted Agent:", response_data)
    except Exception as error:
        print(f"Failed to delete agent {agent_id}: {str(error)}")


# Chat with an agent
def chat(agent_id, query):
    try:
        response = httpx.post(
            f"{url}/chat/{agent_id}", headers=headers, json={"query": query}
        )
        response_data = response.json()
        print("Chat Response:", response_data)
    except Exception as error:
        print(f"Failed to chat with agent {agent_id}: {str(error)}")


# Fetch available tools
def get_tools():
    try:
        response = httpx.get(f"{url}/tools", headers=headers)
        response_data = response.json()
        print("Available Tools:", response_data)
    except Exception as error:
        print(f"Failed to fetch tools: {str(error)}")


# Fetch chat history by agent ID
def get_chat_history_by_id(agent_id):
    try:
        response = httpx.get(f"{url}/chat-history/{agent_id}", headers=headers)
        response_data = response.json()
        print(f"Chat History for Agent {agent_id}:", response_data)
    except Exception as error:
        print(f"Failed to fetch chat history for agent {agent_id}: {str(error)}")


# Clone an agent by ID
def clone_agent(agent_id):
    try:
        response = httpx.post(f"{url}/clone/{agent_id}", headers=headers)
        response_data = response.json()
        print(f"Cloned Agent {agent_id}:", response_data)
    except Exception as error:
        print(f"Failed to clone agent {agent_id}: {str(error)}")


# Fetch agent logs
def get_logs():
    try:
        response = httpx.get(f"{url}/logs", headers=headers)
        response_data = response.json()
        print("Agent Logs:", response_data)
    except Exception as error:
        print(f"Failed to fetch logs: {str(error)}")


# Fetch logs by agent ID
def get_logs_by_id(agent_id):
    try:
        response = httpx.get(f"{url}/logs/{agent_id}", headers=headers)
        response_data = response.json()
        print(f"Logs for Agent {agent_id}:", response_data)
    except Exception as error:
        print(f"Failed to fetch logs for agent {agent_id}: {str(error)}")


# Example Usage
# Uncomment the following lines to test the functions:

create_agent()
# get_agents()
# get_agent_by_id("67cbbd7d80ba7f4b5da9c754")
# update_agent("67cbc00e80ba7f4b5da9c75f", {"tools": ["Search"]})
# delete_agent("67cbbd7d80ba7f4b5da9c754")
# chat("67cbbd7d80ba7f4b5da9c754", "Hello, how are you?")

# Uncomment to test the new functions
# get_tools()
# get_chat_history_by_id("67cbc00e80ba7f4b5da9c75f")
# clone_agent("67cbc00e80ba7f4b5da9c75f")
# get_logs()
# get_logs_by_id("67cbbd7d80ba7f4b5da9c754")
