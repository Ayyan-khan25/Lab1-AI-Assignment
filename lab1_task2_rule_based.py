def rule_based(score, documents_complete, income_eligible, enrollment_verified):
    # All criteria and thresholds are synthetic lab assumptions.
    if (score >= 70 and documents_complete
            and income_eligible and enrollment_verified):
        return "Review"
    return "Hold"


test_cases = [
    {
        "name": "pass_all_conditions",
        "score": 82,
        "documents_complete": True,
        "income_eligible": True,
        "enrollment_verified": True,
        "expected": "Review",
        "reason": "All four conditions are satisfied."
    },
    {
        "name": "fail_income_condition",
        "score": 85,
        "documents_complete": True,
        "income_eligible": False,
        "enrollment_verified": True,
        "expected": "Hold",
        "reason": "Income eligibility is False, so the rule is not satisfied."
    },
    {
        "name": "fail_enrollment_condition",
        "score": 88,
        "documents_complete": True,
        "income_eligible": True,
        "enrollment_verified": False,
        "expected": "Hold",
        "reason": "Enrollment verification is False, so the rule is not satisfied."
    },
    {
        "name": "threshold_boundary",
        "score": 70,
        "documents_complete": True,
        "income_eligible": True,
        "enrollment_verified": True,
        "expected": "Review",
        "reason": "The score is exactly 70, and the condition is score >= 70."
    }
]

print("All score/eligibility thresholds are synthetic lab assumptions.")
print("case | input | expected | actual | pass | reason")

for case in test_cases:
    actual = rule_based(
        case["score"],
        case["documents_complete"],
        case["income_eligible"],
        case["enrollment_verified"]
    )
    inputs = (
        f'score={case["score"]}, '
        f'documents_complete={case["documents_complete"]}, '
        f'income_eligible={case["income_eligible"]}, '
        f'enrollment_verified={case["enrollment_verified"]}'
    )
    print(
        case["name"], inputs, case["expected"], actual,
        case["expected"] == actual, case["reason"], sep=" | "
    )
