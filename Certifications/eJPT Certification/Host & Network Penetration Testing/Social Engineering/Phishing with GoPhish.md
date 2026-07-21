# GoPhish

## What Is GoPhish?

GoPhish is an open-source **phishing simulation framework** designed to help organizations assess and improve their security awareness programs.

Unlike malicious phishing tools, GoPhish is intended for authorized security testing and employee awareness training. It enables organizations to safely simulate phishing campaigns, measure user responses, and identify areas where additional security training may be needed.

---

# Why Do Organizations Use GoPhish?

Organizations use GoPhish to evaluate how employees respond to phishing attacks.

Typical objectives include determining:

- How many employees open phishing emails.
- How many users click phishing links.
- How many users submit their credentials.
- How many employees report the phishing email to the security team.
- Whether security awareness training is effective.

The collected metrics help organizations improve their security awareness programs and reduce the likelihood of successful phishing attacks.

---

# Core Features

## Campaign Creation

GoPhish allows administrators to create multiple phishing campaigns for different groups within an organization.

For example:

- HR Department.
- Finance Department.
- IT Department.

Each campaign can have its own:

- Email template.
- Landing page.
- Target group.
- Tracking configuration.

---

## Email Template Editor

GoPhish includes a built-in editor for creating realistic phishing emails.

Templates can be designed to resemble legitimate communications from:

- Microsoft
- Google
- Office 365
- Banks
- Internal corporate departments

This allows organizations to create realistic phishing simulations while maintaining full control over the campaign.

---

## Target Management

Target management enables administrators to organize recipients into groups.

For example, an organization with 100 employees may create groups such as:

```
IT
HR
Finance
Management
```

Different phishing campaigns can then be delivered to each department based on the organization's testing objectives.

---

## Landing Pages

Landing Pages are among the most important components of a phishing simulation.

A Landing Page is the webpage displayed after a user clicks the phishing link.

Example:

The employee receives an email containing:

```
Click here to update your password.
```

After clicking the link, the user is redirected to a page that closely resembles a legitimate login portal, such as:

- Microsoft Office 365
- Google Workspace
- Company Portal

During authorized security awareness testing, organizations evaluate whether users attempt to enter their credentials. The goal is to measure employee awareness rather than collect real credentials.

---

## Tracking and Reporting

GoPhish records every stage of the phishing campaign.

Typical tracked events include:

|Event|Status|
|---|---|
|Email Delivered|Yes|
|Email Opened|Yes|
|Link Clicked|Yes|
|Credentials Submitted|Yes|

After the campaign is complete, GoPhish automatically generates detailed reports that summarize user interactions and campaign statistics.

---

## Scheduling

Campaigns can be scheduled to execute automatically.

Examples include:

```
Monday at 9:00 AM
```

or

```
The first day of every month
```

This allows recurring phishing awareness campaigns without manual intervention.

---

# GoPhish Phishing Campaign Workflow

A typical phishing awareness campaign follows these steps:

```
Create an Email Template
        ↓
Create a Landing Page
        ↓
Import Target Users
        ↓
Create a Campaign
        ↓
Launch the Campaign
        ↓
Monitor User Activity
        ↓
Generate Reports
```

---

# Lab


Begin by logging into the GoPhish administrative dashboard.

![](../../../../Images/Pasted%20image%2020260609021116.png)

---


Review the main interface, which provides access to campaign management, templates, users, landing pages, and reports.

![](../../../../Images/Pasted%20image%2020260609021125.png)

![](../../../../Images/Pasted%20image%2020260609021142.png)

---


Navigate to the Email Templates section and create a phishing email template that will be used during the campaign.

![](../../../../Images/Pasted%20image%2020260609021218.png)

![](../../../../Images/Pasted%20image%2020260609021229.png)

![](../../../../Images/Pasted%20image%2020260609021238.png)

![](../../../../Images/Pasted%20image%2020260609021252.png)

![](../../../../Images/Pasted%20image%2020260609021308.png)

![](../../../../Images/Pasted%20image%2020260609021321.png)

---


Create the Landing Page that users will be redirected to after clicking the phishing link.

The page should closely resemble the legitimate service being simulated for the awareness exercise.

![](../../../../Images/Pasted%20image%2020260609021330.png)

![](../../../../Images/Pasted%20image%2020260609021339.png)

![](../../../../Images/Pasted%20image%2020260609021348.png)

![](../../../../Images/Pasted%20image%2020260609021406.png)

![](../../../../Images/Pasted%20image%2020260609021416.png)

![](../../../../Images/Pasted%20image%2020260609021434.png)

---



Create the sending profile that defines how phishing emails will be delivered.

This includes configuring the email server and sender information used during the simulation.

![](../../../../Images/Pasted%20image%2020260609021444.png)

![](../../../../Images/Pasted%20image%2020260609021456.png)

![](../../../../Images/Pasted%20image%2020260609021507.png)

![](../../../../Images/Pasted%20image%2020260609021516.png)

---


Add the users who will participate in the phishing simulation.

Targets may be imported individually or organized into groups based on departments or business units.

![](../../../../Images/Pasted%20image%2020260609021527.png)

![](../../../../Images/Pasted%20image%2020260609021544.png)

---


![](../../../../Images/Pasted%20image%2020260609021747.png)

![](../../../../Images/Pasted%20image%2020260609021800.png)

![](../../../../Images/Pasted%20image%2020260609021814.png)

![](../../../../Images/Pasted%20image%2020260609021824.png)

![](../../../../Images/Pasted%20image%2020260609021835.png)

![](../../../../Images/Pasted%20image%2020260609021846.png)

---


After verifying the configuration, launch the phishing campaign.

GoPhish begins delivering phishing emails to the selected recipients.

![](../../../../Images/Pasted%20image%2020260609021854.png)

![](../../../../Images/Pasted%20image%2020260609021906.png)

---


![](../../../../Images/Pasted%20image%2020260609021917.png)

![](../../../../Images/Pasted%20image%2020260609021928.png)

---


![](../../../../Images/Pasted%20image%2020260609021951.png)

![](../../../../Images/Pasted%20image%2020260609022002.png)

![](../../../../Images/Pasted%20image%2020260609022012.png)

---

# Additional Resources

## Official Website

```
https://getgophish.com/
```

---

## GitHub Repository

```
https://github.com/gophish/gophish
```

---

## Installation Guide

```
https://docs.getgophish.com/user-guide/installation
```

---

# Summary

GoPhish is a powerful open-source framework for conducting authorized phishing simulations and security awareness assessments.

Its primary capabilities include:

- Creating phishing campaigns.
- Designing realistic email templates.
- Building custom landing pages.
- Managing target users.
- Scheduling campaigns.
- Tracking user interactions.
- Generating comprehensive campaign reports.

By simulating real-world phishing attacks in a controlled environment, organizations can measure employee awareness and strengthen their overall security posture.