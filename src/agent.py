from langgraph.graph import StateGraph
from custom_types import ExampleConfig
# Create a state graph
graph = StateGraph(ExampleConfig)

# Define a simple node function
def hello_node(state):
    print("Hello, World!")
    return state

# Add the node to the graph
graph.add_node("hello", hello_node)

# Set the entry point (starting node)
graph.set_entry_point("hello")

# Compile and run the workflow
workflow = graph.compile()
workflow.invoke({})