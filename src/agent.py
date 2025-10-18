from flask import Flask, jsonify
from langgraph.graph import StateGraph
from custom_types.custom_types import ExampleConfig
from agents.agents import indicator_agent, risk_agent, trend_agent, pattern_agent, end_node

app = Flask(__name__)

# Create a state graph
graph = StateGraph(ExampleConfig)

# Define a simple node function
def hello_node(state):
    print("Hello, World!")
    return state

# Add the node to the graph
graph.add_node("hello", hello_node)
graph.add_node("indicator", indicator_agent)
graph.add_node("risk", risk_agent)
graph.add_node("trend", trend_agent)
graph.add_node("pattern", pattern_agent)
graph.add_node("end", end_node)

# Set the entry point (starting node)
graph.set_entry_point("hello")
graph.add_edge("hello", "indicator")
graph.add_edge("hello", "risk")
graph.add_edge("hello", "trend")
graph.add_edge("hello", "pattern")
graph.add_edge("indicator", "end")
graph.add_edge("risk", "end")
graph.add_edge("trend", "end")
graph.add_edge("pattern", "end")



# Compile the workflow
workflow = graph.compile()

@app.route('/', methods=['GET'])
def run_workflow():
    result = workflow.invoke({})
    return jsonify({"status": "success", "message": "Workflow executed"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234, debug=True)