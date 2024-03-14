import autogen

# Configuration for the local OLLAMA model
ollama_config = {
    "model_type": "ollama_local",
    "access_config": {
        "endpoint": "http://localhost:8085/run_codellama"
    }
}

# Configure the AssistantAgent with the OLLAMA model
assistant = autogen.AssistantAgent("assistant", llm_config=ollama_config)

# Configure the UserProxyAgent with the OLLAMA model and code execution settings
user_proxy = autogen.UserProxyAgent(
    "user_proxy",
    code_execution_config={"work_dir": "coding"},  # Code execution settings
    llm_config=ollama_config  # LLM configuration
)

# Initiate chat
user_proxy.initiate_chat(assistant, message="Plot a chart of NVDA and TESLA stock price change YTD.")
