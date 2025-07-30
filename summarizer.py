from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

def summarize_text(text):
    model_name = "t5-small"
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)

    input_text = "summarize: " + text[:1000]  # limit input length
    inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
    summary_ids = model.generate(inputs, max_length=150, min_length=40, length_penalty=5., num_beams=2)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary
