# Simple AI Agent - Tool Using Agent
# Built for learning Agentic AI concepts

def calculator(expression):
    """A simple calculator tool"""
    try:
        result = eval(expression)
        return f"The result is: {result}"
    except:
        return "Sorry, I could not calculate that."


def greet(name):
    """A simple greeting tool"""
    return f"Hello {name}! Nice to meet you."


def get_current_info():
    """Gives basic info about this agent"""
    return "I am a simple AI Agent created by Tanvi. I can use tools like calculator and greeting."


# List of available tools
tools = {
    "calculator": calculator,
    "greet": greet,
    "info": get_current_info
}


def simple_agent(user_input):
    """
    A very simple agent that decides which tool to use
    based on the user input.
    """
    user_input = user_input.lower().strip()

    # Decision making (this is the "agent" part)
    if any(word in user_input for word in ["calculate", "math", "add", "subtract", "multiply", "divide", "+", "-", "*", "/"]):
        # Extract the expression
        expression = user_input
        for word in ["calculate", "what is", "compute", "math"]:
            expression = expression.replace(word, "")
        expression = expression.strip()
        return tools["calculator"](expression)

    elif "hello" in user_input or "hi" in user_input or "greet" in user_input:
        # Try to extract name
        words = user_input.split()
        name = "friend"
        if len(words) > 1:
            name = words[-1].capitalize()
        return tools["greet"](name)

    elif "who are you" in user_input or "what can you do" in user_input or "info" in user_input:
        return tools["info"]()

    else:
        return "I am a simple agent. I can calculate math expressions or greet you. Try saying: 'calculate 25 * 4' or 'hello Tanvi'"


# Main program
print("=" * 50)
print("Simple AI Agent is ready!")
print("Type 'exit' to quit")
print("=" * 50)

while True:
    user_input = input("\nYou: ")
    
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Agent: Goodbye! Have a nice day.")
        break
    
    response = simple_agent(user_input)
    print("Agent:", response)
