from src.harness import evaluate

def test_correct_candidate_achieves_full_score():
    report = evaluate('solutions.correct')
    assert report['score_percent'] == 100
    assert report['failures'] == []

def test_buggy_candidate_exposes_non_happy_path_failures():
    report = evaluate('solutions.buggy')
    assert report['score_percent'] < 100
    assert len(report['failures']) >= 4
    assert any(item['category'] in {'negative', 'boundary', 'robustness'} for item in report['failures'])
