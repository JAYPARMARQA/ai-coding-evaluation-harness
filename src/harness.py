import argparse
import importlib
import json

CASES = [
    ('discount', 'functional', (100, 10), 90),
    ('discount', 'boundary', (100, 100), 0),
    ('discount', 'negative', (100, 101), ValueError),
    ('discount', 'negative', (-1, 10), ValueError),
    ('reserve', 'functional', (5, 2), 3),
    ('reserve', 'boundary', (5, 5), 0),
    ('reserve', 'robustness', (5, 6), ValueError),
    ('reserve', 'negative', (5, 0), ValueError),
    ('valid_email', 'functional', ('qa@example.com',), True),
    ('valid_email', 'negative', ('qa @example.com',), False),
    ('valid_email', 'boundary', ('qa@example',), False),
]

def evaluate(module_name: str) -> dict:
    candidate = importlib.import_module(module_name)
    results = []
    for name, category, args, expected in CASES:
        try:
            actual = getattr(candidate, name)(*args)
            passed = actual == expected if not isinstance(expected, type) else False
            detail = f'returned {actual!r}'
        except Exception as exc:
            passed = isinstance(exc, expected) if isinstance(expected, type) else False
            detail = f'raised {type(exc).__name__}: {exc}'
        results.append({'case': name, 'category': category, 'passed': passed, 'evidence': detail})
    passed = sum(item['passed'] for item in results)
    categories = {category: {'passed': sum(r['passed'] for r in results if r['category'] == category), 'total': sum(r['category'] == category for r in results)} for category in sorted({r['category'] for r in results})}
    return {'candidate': module_name, 'passed': passed, 'total': len(results), 'score_percent': round(100 * passed / len(results), 1), 'categories': categories, 'failures': [r for r in results if not r['passed']]}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--solution', choices=['correct', 'buggy'], required=True)
    args = parser.parse_args()
    print(json.dumps(evaluate(f'solutions.{args.solution}'), indent=2))
