from transformers import pipeline

def llama3_llm():
    return pipeline(
        "text-generation",
        model="meta-llama/meta-Llama-3-8b-Instruct",
        tokenizer="meta-llama/meta-Llama-3-8b-Instruct",
        max_new_tokens=500,
        do_sample=True,
        temperature=0.5
    )
