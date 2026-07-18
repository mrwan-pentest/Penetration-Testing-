# The Role of AI in Cybersecurity

In the past:

```
Attacker = Human
Defender = Human
Tools = Static Tools
```

Today:

```
Attacker + AI
Defender + AI
```

Both attackers and defenders are leveraging Artificial Intelligence.

---

# Before AI

Traditionally, penetration testers relied on:

- Scripts
- Bash scripts
- Python scripts
- Security tools
    - Nmap
    - Metasploit
    - Burp Suite
- Personal experience

The workflow looked like this:

```
Observe the results
        ↓
Analyze them manually
        ↓
Decide the next step
```

---

# The Problem

Imagine assessing a large organization with:

- 1,000 hosts
- 50,000 log entries
- Hundreds of pages of documentation

Reviewing all this information manually could take **hours or even days**.

---

# What Did AI Change?

Traditional security tools were mostly:

```
Rule-Based
```

AI introduced a new approach:

```
Data-Driven
```

Instead of relying only on predefined rules, AI learns from large datasets and identifies patterns automatically.

---

# Why Do Pentesters Use AI?

Modern environments have become much more complex.

## Cloud

Examples include:

- Amazon Web Services (AWS)
- Microsoft Azure

---

## APIs

Modern applications may expose dozens or even hundreds of APIs.

---

## Microservices

Instead of one large application, organizations now deploy:

- 50 services
- 100 services
- 200 services

Each service becomes another component to assess.

---

## Hybrid Networks

Many organizations combine:

- Cloud infrastructure
- On-Premises infrastructure
- VPN connections
- Remote workers

As a result, the attack surface becomes significantly larger.

---

# Practical AI Use Cases for Pentesters

## OSINT

Instead of reading hundreds of web pages manually, AI can summarize important information such as:

- Company details
- Employees
- Technologies in use
- Domains
- Email addresses

---

## Analyzing Nmap Results

Instead of reviewing thousands of lines of Nmap output manually, AI can highlight:

- Interesting open ports
- Important services
- Potential attack vectors

---

## Code Review

For example:

```php
$user = $_GET['id'];
```

AI can help explain the code and identify potentially vulnerable areas.

---

## Report Writing

Writing reports is one of the least enjoyable tasks for many penetration testers.

Instead of creating everything from scratch, AI can generate an initial draft containing:

- Executive Summary
- Risk Assessment
- Recommendations

The tester can then review and refine the report.

---

## Creating Phishing Campaigns

For example, you can ask AI:

> Write an email from the Human Resources department.

AI can quickly generate a realistic phishing email draft.

---

# Traditional Workflow vs AI-Assisted Workflow

## Traditional Workflow

```
Information Gathering
        ↓
Analysis
        ↓
Exploitation
        ↓
Reporting
```

Every stage is performed manually.

---

## AI-Assisted Workflow

```
Information Gathering
        ↓
AI summarizes data
        ↓
AI assists with analysis
        ↓
AI helps during exploitation
        ↓
AI assists with reporting
```

This significantly speeds up the assessment process.

---

# Can AI Perform Penetration Testing for You?

**No.**

This is one of the most important points.

---

# What AI Cannot Replace

## Creativity

For example:

Combining two unrelated vulnerabilities to achieve a greater level of access still requires human creativity and experience.

---

## Ethical Judgment

AI cannot decide questions such as:

- Is this action within the engagement scope?
- Is this activity legal?

Those decisions must always be made by the penetration tester.

---

## Decision Making

Examples include:

- Should I exploit this vulnerability?
- Should I stop the assessment?
- Should I immediately notify the client?

These decisions remain the responsibility of the security professional.

---

## Validating Results

If AI reports:

```
This is SQL Injection.
```

It does **not** automatically mean the application is vulnerable.

Every AI-generated finding must be verified manually before being trusted.