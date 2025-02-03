from smolagents import CodeAgent, LiteLLMModel, DuckDuckGoSearchTool
# import litellm

# litellm._turn_on_debug()

model = LiteLLMModel(
    model_id="ollama/qwen2.5:1.5b",
    api_base="http://localhost:11434",
    api_key="YOUR_API_KEY",
    num_ctx=8192,
    set_verbose=True
)

agent = CodeAgent(tools=[], model=model, add_base_tools=True)

agent.run("How many seconds would it take for a leopard at full speed to run through Pont des Arts?")



# from smolagents import tool, LiteLLMModel, CodeAgent

# model = LiteLLMModel(model_id="ollama_chat/llama3.2", api_key="ollama")

# agent = CodeAgent(
#     tools=[retriever_tool], model=model, max_iterations=4, verbose=True
# )

# agent_output = agent.run("What happens after an over is completed in a cricket match?")

# print("Final output:")
# print(agent_output)