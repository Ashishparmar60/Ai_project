import openai
openai.api_key = "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"

model = "davinci"
question = "how old was gandhi was when he died ?"

response = openai.Completion.create(
    engine=model,
    prompt=(f"Question: {question}\n"
            "Answer:"
            ),
    max_tokens=100,
    n=1,
    stop=None,
    temperature=0.5
)

answer =  str("Hi Ashish,") + response.choices[0].text.split('\n')[0] 
print(answer)