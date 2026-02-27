# Thinking Tools Collection

A curated and comprehensive collection of thinking tools, mental models, and cognitive frameworks implemented as an interactive software library. This project organizes over 100 mental models into practical, composable tools that help individuals and teams think more clearly and make better decisions.

## Overview

Mental models are simplified representations of how the world works. By building a diverse toolkit of these models, you can approach problems from multiple angles, avoid blind spots, and make more nuanced decisions. This collection transforms abstract thinking frameworks into concrete, programmable tools.

The tools in this collection draw from the wisdom of history's greatest thinkers. Explore the backgrounds and methods of [masters of strategic thought](https://keeprule.com/en/masters) whose frameworks form the foundation of this library, from Charlie Munger's latticework of mental models to Nassim Taleb's antifragility concepts.

## Features

- **100+ Mental Models**: Comprehensive library spanning multiple disciplines
- **Model Recommender**: AI-powered suggestions based on your problem description
- **Combination Engine**: Combine multiple models for deeper analysis
- **Interactive Worksheets**: Guided walkthroughs for each thinking tool
- **Problem-Model Matching**: Map problem types to the most effective models
- **Decision Journal Integration**: Track which models led to the best outcomes
- **Team Facilitation Mode**: Guide group discussions through structured frameworks
- **Export and Sharing**: Generate reports and share analyses with teammates
- **Spaced Repetition**: Practice and internalize models through regular review
- **Custom Model Builder**: Create and save your own thinking frameworks

## Installation

```bash
npm install thinking-tools-collection
```

## Quick Start

```javascript
const { ModelLibrary, ProblemAnalyzer } = require("thinking-tools-collection");

// Initialize the library
const library = new ModelLibrary();

// Browse models by category
const categories = library.getCategories();
// ["systems_thinking", "decision_making", "problem_solving", "creativity",
//  "economics", "psychology", "physics", "biology", "mathematics"]

// Get recommendations for a specific problem
const analyzer = new ProblemAnalyzer();
const recommendations = analyzer.recommend(
  "Our product growth has plateaued and we need to find new growth levers"
);

recommendations.forEach(rec => {
  console.log(`${rec.model.name} (relevance: ${rec.score.toFixed(2)})`);
  console.log(`  Category: ${rec.model.category}`);
  console.log(`  Why: ${rec.reasoning}`);
});
```

## Featured Mental Models

### Circle of Competence

Stay within areas where you have genuine expertise:

```javascript
const { CircleOfCompetence } = require("thinking-tools-collection");

const coc = new CircleOfCompetence();
coc.defineCompetencies({
  strong: ["software_engineering", "data_analysis", "product_design"],
  developing: ["marketing", "finance"],
  outside: ["legal", "manufacturing", "biotech"]
});

const assessment = coc.evaluate("Should I invest in a biotech startup?");
console.log(`Within circle: ${assessment.withinCircle}`);
console.log(`Risk level: ${assessment.riskLevel}`);
console.log(`Advice: ${assessment.recommendation}`);
```

### Margin of Safety

Build buffers into your estimates and plans. This is one of the most fundamental [principles of sound decision-making](https://keeprule.com/en/principles), ensuring that even when estimates are wrong, outcomes remain acceptable.

```javascript
const { MarginOfSafety } = require("thinking-tools-collection");

const mos = new MarginOfSafety();
const analysis = mos.apply({
  estimatedValue: 1000000,
  requiredMargin: 0.30,
  confidenceLevel: 0.75,
  factors: {
    market_uncertainty: "high",
    execution_risk: "moderate",
    competitive_threat: "low"
  }
});

console.log(`Safe entry point: $${analysis.safeValue.toLocaleString()}`);
console.log(`Required margin: ${analysis.adjustedMargin.toFixed(1)}%`);
console.log(`Risk factors: ${analysis.topRisks.join(", ")}`);
```

### Inversion

Approach problems backward by asking what you want to avoid:

```javascript
const { Inversion } = require("thinking-tools-collection");

const inv = new Inversion();
const result = inv.analyze({
  goal: "Build a successful remote team",
  context: "50-person engineering organization"
});

console.log("To guarantee failure, you would:");
result.failurePaths.forEach(path => {
  console.log(`  - ${path.action}`);
  console.log(`    Prevention: ${path.prevention}`);
});
```

### Second-Order Thinking

Think through the consequences of consequences:

```javascript
const { SecondOrderThinking } = require("thinking-tools-collection");

const sot = new SecondOrderThinking({ depth: 3 });
const effects = sot.analyze({
  action: "Implement a four-day work week",
  context: { industry: "tech", teamSize: 200 }
});

effects.byOrder.forEach((order, index) => {
  console.log(`\n${index + 1}st-order effects:`);
  order.forEach(effect => {
    console.log(`  [${effect.sentiment}] ${effect.description}`);
  });
});
```

## Model Categories

The library organizes models across disciplines, applicable to a wide range of [decision-making scenarios](https://keeprule.com/en/scenarios):

| Category | Models | Example |
|----------|--------|---------|
| Systems Thinking | 15 | Feedback Loops, Emergence, Bottleneck Analysis |
| Decision Making | 18 | Expected Value, Regret Minimization, Reversibility |
| Problem Solving | 14 | First Principles, Root Cause, Decomposition |
| Creativity | 10 | Lateral Thinking, SCAMPER, Random Input |
| Economics | 12 | Opportunity Cost, Marginal Analysis, Game Theory |
| Psychology | 16 | Cognitive Biases, Incentives, Social Proof |
| Physics | 8 | Entropy, Critical Mass, Leverage |
| Biology | 7 | Evolution, Ecosystems, Adaptation |
| Mathematics | 6 | Bayesian Updating, Power Laws, Regression to Mean |

## Combination Engine

The real power comes from combining multiple models:

```javascript
const { CombinationEngine } = require("thinking-tools-collection");

const engine = new CombinationEngine();
engine.addModel("first_principles", { weight: 0.3 });
engine.addModel("inversion", { weight: 0.25 });
engine.addModel("margin_of_safety", { weight: 0.25 });
engine.addModel("circle_of_competence", { weight: 0.2 });

const combined = engine.analyze({
  decision: "Launch a new product line",
  context: productContext
});

console.log(combined.synthesis);
console.log(`Confidence: ${combined.confidence.toFixed(2)}`);
console.log(`Key insight: ${combined.keyInsight}`);
```

For guided templates that walk you through applying these models to specific situations, check out the [decision prompts library](https://keeprule.com/en/prompts) with ready-to-use worksheets for each framework.

## Contributing

We welcome new mental model contributions! Please:

1. Fork the repository
2. Create a feature branch
3. Implement the model following our model template
4. Include tests and usage examples
5. Submit a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by Charlie Munger's concept of a latticework of mental models
- Built to make structured thinking accessible to everyone
- Contributions from the decision science and cognitive psychology communities
