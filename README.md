# 🔍 Engineering Blindspot

### Find what your code change might break before you merge.

Engineering Blindspot is an AI-powered code impact analysis tool that examines a Git repository and identifies potential downstream risks **before a change is merged**.

Instead of looking only at the changed file, Engineering Blindspot connects:

**Git diff → Code structure → Dependencies → Tests → Risk → AI reasoning**

---

## 🚨 The Problem

A code change can look small while affecting multiple parts of a software system.

For example:

```text
pricing.py
    ↓
calculate_total()
    ↓
checkout.py
order_service.py
```

A developer may modify `pricing.py`, run its unit tests, and assume everything is safe.

But the real question is:

> **"What else could this change break?"**

Engineering Blindspot is designed to answer that question.

---

## 💡 What Engineering Blindspot Does

Given a Git repository, the system:

1. Detects the latest commit.
2. Identifies changed files.
3. Extracts the actual Git diff.
4. Analyzes changed Python code using AST.
5. Finds production dependents.
6. Detects related tests.
7. Calculates an evidence-based risk level.
8. Sends the structured evidence to an AI model.
9. Produces a human-readable impact review.

---

## 🧠 How It Works

```text
                 Git Repository
                       │
                       ▼
                ┌─────────────┐
                │ Git Analyzer│
                └──────┬──────┘
                       │
                  Changed files
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
     ┌────────┐   ┌──────────┐  ┌──────────┐
     │  AST   │   │Dependency│  │   Test   │
     │Analyzer │   │ Analyzer │  │ Analyzer │
     └────┬───┘   └─────┬────┘  └────┬─────┘
          │             │             │
          └─────────────┼─────────────┘
                        ▼
                 ┌─────────────┐
                 │Impact Report│
                 └──────┬──────┘
                        │
                        ▼
                 ┌─────────────┐
                 │ AI Analyzer │
                 └──────┬──────┘
                        │
                        ▼
               Engineering Blindspot
                        │
                        ▼
                  Streamlit UI
```

---

## 🔍 Evidence-Based Risk Detection

Engineering Blindspot currently uses repository evidence such as:

* Number of production dependents
* Functions present in changed files
* Related test files
* Actual Git diff
* Missing test coverage

### Risk levels

| Risk      | Evidence                          |
| --------- | --------------------------------- |
| 🟢 LOW    | No detected production dependents |
| 🟡 MEDIUM | One production dependent          |
| 🔴 HIGH   | Two or more production dependents |

The AI layer does **not** determine the risk score. It receives the structured evidence and explains the potential engineering impact.

---

## 🤖 AI-Powered Blindspot Analysis

The AI receives structured evidence rather than the entire repository.

It is asked to identify:

1. What changed
2. The most important potential impact
3. What the developer might overlook
4. Recommended checks before merging

This makes the AI act as an **engineering reviewer**, rather than simply generating a generic code summary.

---

## 🧪 Demonstration Scenarios

### Scenario 1 — Pricing Change

```text
pricing.py
    ↓
checkout.py
order_service.py
```

A discount parameter is added to `calculate_total()`.

Engineering Blindspot identifies:

* 🔴 HIGH impact
* 2 production dependents
* Related pricing tests
* A behavioral change in the calculation
* Potential downstream pricing inconsistencies

---

### Scenario 2 — Payment Processing

```text
payment.py
    ↓
checkout.py
order_service.py
```

A 2% processing fee is introduced.

Engineering Blindspot identifies:

* 🔴 HIGH impact
* 2 production dependents
* No related tests
* Changed payment behavior
* Potential zero-value payment behavior
* Financial precision concerns

---

### Scenario 3 — Isolated Refactor

```text
formatter.py
```

A local refactor changes the implementation of `format_name()`.

Engineering Blindspot identifies:

* 🟢 LOW impact
* No detected production dependents
* No related tests

This demonstrates that the tool does not simply classify every change as risky.

---

## 🛠️ Tech Stack

**Frontend / UI**

* Streamlit

**Analysis**

* Python
* Python AST
* GitPython

**AI**

* Google Gemini API

**Version Control**

* Git

---

## 📁 Project Structure

```text
engineering-blindspot/
│
├── analyzer/
│   ├── ast_analyzer.py
│   ├── dependency_analyzer.py
│   ├── git_analyzer.py
│   ├── test_analyzer.py
│   ├── impact_analyzer.py
│   ├── report_analyzer.py
│   └── ai_analyzer.py
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/BushraTayyab/engineering-blindspot.git
cd engineering-blindspot
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows**

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the AI API key

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

**Never commit `.env` to Git.**

### 5. Start the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🎯 Why It Matters

Engineering Blindspot focuses on a common software-engineering problem:

> **The blast radius of a change is often larger than the changed file itself.**

Traditional code review can identify obvious problems, but developers can overlook:

* Downstream consumers
* Behavioral changes
* Missing tests
* Hidden assumptions
* Integration impact

Engineering Blindspot provides a fast pre-merge impact review using a combination of **static analysis, Git history, dependency evidence, test detection, and AI reasoning**.

---

## ⚠️ Limitations

Engineering Blindspot is currently focused on Python repositories and static evidence.

It may not detect:

* Dynamic imports
* Runtime-generated dependencies
* Reflection/metaprogramming
* External services
* Undocumented business rules
* Dependencies that cannot be inferred statically

The AI analysis is therefore explicitly based on the evidence discovered by the analyzers.

---

## 🔮 Future Improvements

Potential future improvements include:

* Multi-language AST analysis
* Deeper call-graph analysis
* GitHub/GitLab pull-request integration
* CI/CD integration
* Historical risk learning
* Dependency graph visualization
* Automatic test recommendations
* Confidence scoring
* Incremental repository indexing

---

## 🏆 Built For

A hackathon project focused on applying AI to practical software engineering workflows.

**Engineering Blindspot — find what your code change might break before you merge.**
