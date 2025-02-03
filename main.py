from smolagents import tool, LiteLLMModel, CodeAgent

model = LiteLLMModel(model_id="ollama_chat/llama3.1", api_key="ollama")






agent = CodeAgent(
    tools=[retriever_tool], model=model, max_iterations=4, verbose=True
)

agent_output = agent.run("What happens after an over is completed in a cricket match?")

print("Final output:")
print(agent_output)