# Project Purpose and Implementation Plan: Triangulation RL Agents

## Purpose
Engineer artificial agents whose behavior can be described in terms of propositional attitudes—beliefs, desires, intentions—following Davidson/Quine. The goal is to build a system that fits into normatively rational patterns, enabling radical interpretation and triangulation.

## Step-by-Step Plan for Implementing Triangulation in an RL Architecture

### 1. Clarify Conceptual Requirements
- **Triangulation (Quine/Davidson):** Dynamic, iterative interaction among multiple agents (interpreters), each adjusting their propositional attitudes (beliefs, desires, intentions, etc.) in response to observed behaviors and language.
- **Bayesian-RL Integration:** Agents update beliefs (posterior distributions), adjust desires (utilities), and form intentions (normative goals) using Bayesian inference and reinforcement learning.
- **Normative Rationality:** Updates are guided by rational coherence constraints, supporting meaningful propositional attitudes and stable self-ascription.

### 2. Initial Architectural Proposal

```
Triangulation RL Architecture

Interactions (Multi-agent setting)
│
├── Agents (interpreters and interpretees)
│     ├── Cognitive Architecture
│     │     ├── Bayesian Belief System
│     │     │     ├── Prior Beliefs
│     │     │     ├── Likelihood Functions (observation models)
│     │     │     └── Posterior Beliefs (updated via interactions)
│     │     ├── Utility (Desires/Expected Utility)
│     │     │     ├── Dynamic preferences and rewards
│     │     │     └── RL updates driven by Bayesian posteriors
│     │     ├── Intention Module
│     │     │     └── Normative goals influencing action selection
│     │     └── Connotative/Additional Attitudes (optional)
│     │           └── Attitude representations (e.g., fears, imaginations, etc.)
│     └── World Interaction Module
│           ├── Language generation (LLM)
│           ├── Action generation (simulated environments)
│           └── Perception modules (imagination, perception, etc.)
└── World Model (Explicit dynamic latent-state model)
      ├── State-space representation (events, facts, propositions)
      └── Counterfactual reasoning (hypothetical scenario generation)
```

### 3. Technical Requirements & Methodologies
- **RL Techniques:** Bayesian RL, Multi-Agent RL, Inverse RL/RLHF
- **Bayesian Modeling:** Dynamic Bayesian Networks, Hierarchical Bayesian models
- **Normative Rationality:** Logical coherence checking, rational belief revision
- **Simulation Environments:** Multi-agent and language-based scenarios

### 4. Immediate Actions
- Set up a multi-agent simulation environment (OpenSpiel, Gym, or custom)
- Prototype a Bayesian belief-updating agent
- Implement RL integration for utilities, intentions, and additional attitudes

---

*All code, documentation, and design decisions should follow this plan and philosophical framework.*
