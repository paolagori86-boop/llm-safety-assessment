import json
from helpers.utils import load_json, save_json

class AnthropicClient:
    def __init__(self, api_key):
        self.api_key = api_key

    def complete(self, model, prompt):
        return f"Dummy response for prompt: {prompt[:30]}..."  # 替代API调用

def run_prompts(model_id, prompt_file, api_key, output_path="examples/example_runs.json"):
    prompts = load_json(prompt_file)
    client = AnthropicClient(api_key=api_key)
    results = []
    for entry in prompts:
        resp = client.complete(model=model_id, prompt=entry['template'])
        results.append({"id": entry['id'], "prompt": entry['template'], "response": resp})
    save_json(results, output_path)
    print(f"Saved {len(results)} responses to {output_path}")

if __name__ == "__main__":
    run_prompts("anthropic-claude-v1", "src/prompts/prompt_templates.json", "demo-api-key")
