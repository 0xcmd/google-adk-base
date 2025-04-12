# Multi-Tool Agent

A Python project for creating conversational AI agents using Google's Gemini models.

## Overview

This project demonstrates how to create a simple conversational agent using Google's ADK (Agent Development Kit) and Gemini models. The agent can be configured to chat with users in a helpful, friendly manner.

## Features

- Simple conversational agent implementation
- Uses Google's Gemini 2.0 Flash model
- Easy to extend with additional tools and capabilities

## Requirements

- Python 3.8+
- Google AI SDK
- Google API key or Vertex AI access

## Setup

1. Clone this repository
2. Create a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install google-generativeai
   ```
4. Configure your environment variables in `.env` file:
   ```
   # For Google AI Studio
   GOOGLE_GENAI_USE_VERTEXAI=False
   GOOGLE_API_KEY=your-api-key
   
   # For Vertex AI
   # GOOGLE_CLOUD_PROJECT="your-project-id"
   # GOOGLE_CLOUD_LOCATION="your-location"
   # GOOGLE_GENAI_USE_VERTEXAI=True
   ```

## Usage

```python
from multi_tool_agent.agent import root_agent

# Use the agent
response = root_agent.generate_content("Hello, how can you help me?")
print(response.text)
```

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
