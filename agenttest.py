from google.adk.agents import Agent
from vertexai.preview.reasoning_engines import AdkApp
import asyncio
import vertexai

def get_weather(city: str) -> str:
  """Gets the current weather for a specified city.

  Args:
    city: The name of the city (e.g., "Mountain View", "London").

  Returns:
    A string describing the weather in that city.
  """
  # In a real application, you would call a weather API here.
  # For this example, we'll just return a hardcoded, fake response.
  if "tokyo" in city.lower():
    return "The weather in Tokyo is 24°C and sunny."
  elif "paris" in city.lower():
    return "The weather in Paris is 18°C and cloudy."
  else:
    return f"I don't have weather information for {city} right now."

# TODO: Replace "your-project-id" with your Google Cloud project ID.
# You also need to be authenticated with Google Cloud.
# See https://cloud.google.com/docs/authentication/external/set-up-adc
vertexai.init(project="central-segment-470206-p3")

model = "gemini-2.5-flash"

agent = Agent(
    model=model,  # Required.
    name='weather_agent',  # Required.
    tools=[get_weather],  # Optional.
)

app = AdkApp(agent=agent)

async def main():
    print("Agent is ready. Testing with a hardcoded question.")
    user_input = "What is the weather in Tokyo?"
    print(f"You: {user_input}")

    async for event in app.async_stream_query(
        user_id="user_id",
        message=user_input,
    ):
        print(f"Agent: {event}")

if __name__ == "__main__":
    asyncio.run(main())
