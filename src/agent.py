from flask import Flask, jsonify
from langgraph.graph import StateGraph
from custom_types.custom_types import ExampleConfig

app = Flask(__name__)

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

# Compile the workflow
workflow = graph.compile()

@app.route('/', methods=['GET'])
def run_workflow():
    result = workflow.invoke({})
    return jsonify({"status": "success", "message": "Workflow executed"})

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234, debug=True)