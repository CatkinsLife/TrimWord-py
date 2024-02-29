import ai
import openai
# Apply the API key


# Define the text prompt
prompt = "In a shocking turn of events, scientists have discovered that "

# Generate completions using the API
# completions = openai.ChatCompletion.create(
#     engine="text-davinci-002",
#     prompt=prompt,
#     max_tokens=100,
#     n=1,
#     stop=None,
#     temperature=0.5,
# )

# # Extract the message from the API response
# message = completions.choices[0].text
# print(message)

completions = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
message = completions.choices[0].text
print(message)