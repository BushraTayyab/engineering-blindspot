def generate_report(impact_data):
    reports = []

    for change in impact_data["changes"]:
        dependents = change["dependents"]
        tests = change["related_tests"]
        functions = change["code"]["functions"]

        risk_signals = []

        if dependents:
            risk_signals.append(
                f"{len(dependents)} dependent file(s) may be affected"
            )

        if not tests:
            risk_signals.append(
                "No related tests detected"
            )

        if functions:
            risk_signals.append(
                f"{len(functions)} function(s) found in changed file"
            )

        if len(dependents) >= 2:
            risk = "HIGH"
        elif dependents:
            risk = "MEDIUM"
        else:
            risk = "LOW"

        reports.append({
            "file": change["file"],
            "risk": risk,
            "functions": functions,
            "dependents": dependents,
            "related_tests": tests,
            "risk_signals": risk_signals
        })

    return {
        "commit": impact_data["commit"],
        "reports": reports
    }


if __name__ == "__main__":
    from analyzer.impact_analyzer import analyze_impact

    impact = analyze_impact("sample_repo")
    report = generate_report(impact)

    print(report)