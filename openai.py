from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message)
