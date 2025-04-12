from google.adk.agents import Agent

# Create a simple conversational agent without tools
# This is the most basic form that will work with the Google model
root_agent = Agent(
    name="conversational_agent",
    model="gemini-2.0-flash-exp",  # Using Gemini 2.0 Flash model
    description="A conversational agent that can chat with users.",
    instruction=(
        "You are a helpful, friendly AI assistant. Respond to the user's questions "
        "and requests in a conversational manner. Be concise, accurate, and helpful."
    ),
    # No tools specified as we're focusing on just the conversational ability
)