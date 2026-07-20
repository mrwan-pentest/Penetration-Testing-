# Pretexting

## What Is Pretexting?

**Pretexting** is a Social Engineering technique in which an attacker creates a false identity or fabricated scenario to convince a victim to trust them and voluntarily disclose sensitive information or perform specific actions.

Unlike directly requesting confidential information, the attacker builds a believable story that makes the request appear legitimate.

The objective is to manipulate the victim into willingly providing information or access.

---

# Pretexting vs. Phishing

## Phishing

Phishing typically relies on fraudulent emails, messages, or websites that encourage victims to click malicious links or open infected attachments.

Example:

> Click here to update your account.

The attack primarily depends on malicious content delivered through electronic communication.

---

## Pretexting

Pretexting revolves around a carefully crafted story rather than simply sending a malicious link.

The attacker impersonates a trusted individual or authority figure.

Example:

> Hello, I'm from the IT Support team. We need to verify your account before upgrading the system.

Instead of relying on a malicious link, the attacker creates an entire scenario to persuade the victim to cooperate.

---

# The Core Concept

The attacker attempts to place the victim in a familiar and believable situation.

Common impersonated roles include:

- IT Support staff.
- Bank representatives.
- Company managers.
- Shipping companies.
- Human Resources personnel.

The more familiar and realistic the scenario appears, the less likely the victim is to question its legitimacy.

---

# Characteristics of Pretexting

## False Pretense

The attacker creates a fabricated identity or story.

Example:

> I work in the IT department.

Even though the attacker has no affiliation with the organization.

---

## Establishing Trust

Before requesting sensitive information, the attacker focuses on building credibility.

They often appear:

- Professional.
- Confident.
- Knowledgeable about the organization.

This increases the victim's confidence in the attacker's legitimacy.

---

## Manipulating Emotions

Pretexting frequently relies on emotional manipulation.

Common psychological triggers include:

### Fear

Example:

> Your account has been compromised.

---

### Urgency

Example:

> This issue must be resolved within the next 10 minutes.

---

### Curiosity

Example:

> We have an exciting job opportunity for you.

---

### Sympathy

Example:

> I need your assistance with an urgent issue.

Emotional pressure often causes victims to make decisions without verifying the request.

---

## Information Gathering

Once trust has been established, the attacker begins collecting sensitive information.

Common targets include:

```
Username
Password
Email Address
VPN Access
Employee ID
```

---

## Maintaining Consistency

Throughout the interaction, the attacker must maintain a consistent and believable story.

If the victim asks additional questions, the responses must align with the fabricated scenario to avoid raising suspicion.

---

# Practical Examples

## Example 1 - Fake IT Support

An attacker contacts an employee claiming to be from the IT department.

Example:

> We have detected malware on your workstation.

The attacker then requests:

```
Remote Access
```

or asks the victim to install a specific application.

The victim believes the attacker is providing technical assistance.

---

## Example 2 - Fake Recruitment Opportunity

An attacker pretends to be a recruiter.

Example:

> We have an excellent job opportunity that matches your experience.

The attacker then requests personal information such as:

```
National ID
Home Address
Banking Information
```

under the pretense of completing the hiring process.

---

# Typical Pretexting Attack Workflow

A successful Pretexting attack generally follows these stages:

```
1. Reconnaissance
        ↓
2. Create a Believable Story
        ↓
3. Establish Trust
        ↓
4. Request Information or an Action
        ↓
5. Exploit the Collected Information
```

---

# Phase 1 - Reconnaissance

The attacker gathers information about the target organization and its employees.

Typical sources include:

- Social media.
- Company websites.
- Public directories.
- Data breaches.
- Professional networking platforms.

This information helps create a realistic pretext.

---

# Phase 2 - Create a Believable Story

Using the collected information, the attacker develops a convincing scenario.

The story should appear legitimate and match the victim's role, responsibilities, or current activities.

---

# Phase 3 - Establish Trust

The attacker builds rapport with the victim by appearing credible and professional.

This stage is critical because trust significantly increases the likelihood of compliance.

---

# Phase 4 - Request Information or an Action

Once sufficient trust has been established, the attacker requests:

- Sensitive information.
- Account credentials.
- Remote access.
- File downloads.
- Execution of specific commands.

The request is presented as a normal part of the fabricated scenario.

---

# Phase 5 - Exploitation

After obtaining the desired information or access, the attacker proceeds with the next stage of the attack.

Possible objectives include:

- Unauthorized system access.
- Credential theft.
- Data exfiltration.
- Malware deployment.
- Lateral movement within the organization.

---

# Pretext Library

A publicly available collection of phishing and pretext scenarios can be useful for understanding how realistic Social Engineering campaigns are designed and for building authorized security awareness exercises.

Repository:

```
https://github.com/L4bF0x/PhishingPretexts/tree/master
```

The repository contains a large collection of ready-made **Pretext** scenarios that can be adapted for authorized phishing simulations and security awareness assessments.

---

# Summary

Pretexting is a Social Engineering technique that relies on carefully crafted stories rather than technical exploits.

A successful Pretexting attack typically involves:

- Gathering information about the target.
- Creating a believable identity.
- Establishing trust.
- Exploiting human emotions.
- Requesting sensitive information or actions.
- Using the collected information to achieve the attacker's objectives.

Because it exploits human behavior instead of software vulnerabilities, Pretexting remains one of the most effective Social Engineering techniques used in modern cyber attacks.