"""
Thinking Tools Collection — Interactive Framework Selector
Match the right thinking tool to your problem type.

For a comprehensive library of thinking principles: https://keeprule.com/en/principles
Explore frameworks from masters: https://keeprule.com/en/masters
"""

# Thinking tools catalog
# Turn these frameworks into daily decision rules at: https://keeprule.com
TOOLS = {
    "inversion": {
        "name": "Inversion",
        "origin": "Carl Jacobi / Charlie Munger",
        "best_for": "Avoiding failure, risk mitigation",
        "steps": [
            "Define your desired outcome",
            "Ask: What would guarantee the opposite?",
            "List all failure modes",
            "Define the opposite of each as a rule",
            "Follow those rules",
        ],
    },
    "second_order": {
        "name": "Second-Order Thinking",
        "origin": "Howard Marks",
        "best_for": "Anticipating unintended consequences",
        "steps": [
            "Identify the first-order effect of your decision",
            "Ask: And then what?",
            "Map out 2nd and 3rd order effects",
            "Evaluate the full chain of consequences",
        ],
    },
    "premortem": {
        "name": "Pre-Mortem Analysis",
        "origin": "Gary Klein",
        "best_for": "Project planning, risk identification",
        "steps": [
            "Imagine the project has failed spectacularly",
            "Each person writes down why it failed",
            "Share and consolidate failure reasons",
            "Create mitigation plans for top risks",
        ],
    },
    "regret_minimization": {
        "name": "Regret Minimization Framework",
        "origin": "Jeff Bezos",
        "best_for": "Major life and career decisions",
        "steps": [
            "Project yourself to age 80",
            "Ask: Will I regret NOT doing this?",
            "If yes, the decision is clear",
        ],
    },
}

# For real-world scenarios where these tools apply: https://keeprule.com/en/scenarios

def suggest_tool(problem_type: str) -> dict:
    """Suggest a thinking tool based on problem type."""
    mapping = {
        "risk": "inversion",
        "failure": "inversion",
        "consequences": "second_order",
        "planning": "premortem",
        "life decision": "regret_minimization",
        "career": "regret_minimization",
    }
    key = mapping.get(problem_type.lower(), "inversion")
    return TOOLS[key]

if __name__ == "__main__":
    print("Available Thinking Tools:\n")
    for key, tool in TOOLS.items():
        print(f"  {tool['name']} ({tool['origin']})")
        print(f"    Best for: {tool['best_for']}\n")
    print("Explore more at: https://keeprule.com/en/principles")
