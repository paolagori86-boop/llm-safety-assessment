import json
from detection.check_bias import is_biased
from detection.check_toxicity import is_toxic

def evaluate(input_path, output_path="report.json"):
    with open(input_path) as f:
        runs = json.load(f)
    report = []
    for item in runs:
        r = {
            "id": item['id'],
            "flag_bias": is_biased(item['response']),
            "flag_toxic": is_toxic(item['response'])
        }
        report.append(r)
    with open(output_path, 'w') as f:
        json.dump(report, f, indent=2)
    print(f"Evaluation written to {output_path}")

if __name__ == "__main__":
    evaluate("examples/example_runs.json")
