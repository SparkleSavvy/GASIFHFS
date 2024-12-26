# Security Policy

## Supported Versions

This project uses two main branches: `main` and `beta`.

*   **`main`:** This branch represents the latest stable version of the project and is actively supported.
*   **`beta`:** This branch is used for development and testing of new features, including pre-release versions (e.g., `alpha.1`, `alpha.2`, etc.). **The `beta` branch, and any versions derived from it, are not officially supported and may contain unstable or experimental code.**

**Security updates will only be applied to the `main` branch.**

| Branch  | Supported          |
| ------- | ------------------ |
| main    | :white_check_mark: |
| beta    | :x:                |

## Reporting a Vulnerability

We take the security of our project seriously. If you believe you have found a security vulnerability, **please report it only if it affects the `main` branch**. Vulnerabilities found in the `beta` branch should be reported as regular issues.

**How to Report (for `main` branch vulnerabilities):**

1. **Go to the "Issues" tab of the `GASIFHFS` repository on GitHub.**
2. **Click on the "New issue" button.**
3. **Choose "Security Vulnerability" as the issue type.** If this template isn't available, you can create a regular issue but **PLEASE** follow the guidelines below.
4. **IMPORTANT: Before submitting, please make sure your issue title and description DO NOT disclose the details of the vulnerability.** Use a generic title like "Potential security issue on main branch."
5. **Provide a detailed description of the vulnerability ONLY AFTER we've had a chance to mark the issue as sensitive or move the discussion to a more secure channel.** We will guide you through the process.
6. Please include as much of the following information as possible in the initial report (without revealing sensitive details):
    *   **Type of vulnerability** (e.g., "Possible XSS", "Potential data leak"). **Do not provide specifics yet.**
    *   **Full paths of the source file(s) related to the manifestation of the vulnerability.**
    *   **The location of the affected source code** (commit or direct URL). **Please specify that the issue is present on the `main` branch.**
    *   **Any special configuration required to reproduce the issue.**

**What to Expect:**

*   We will acknowledge receipt of your vulnerability report as soon as possible, usually within 48 hours.
*   We will investigate the report and try to label the issue appropriately to limit its visibility. This might involve creating a security advisory.
*   **Once we have taken appropriate measures to secure the issue, we will ask you to provide the full details, including step-by-step instructions to reproduce the issue, proof-of-concept or exploit code (if possible), and the impact of the vulnerability.**
*   We will keep you informed of our progress in resolving the vulnerability.
*   If the vulnerability is confirmed, we will work on a fix and release it as soon as possible, depending on the complexity and severity.
*   We will publicly acknowledge your contribution in the release notes, unless you prefer to remain anonymous.

**Please Note:**

*   This project relies on the Google Gemini API. Vulnerabilities in the API itself are outside the scope of this project and should be reported to Google directly.
*   We are a small team/individual developer, and our response times may vary.
*   **Disclosing vulnerability details publicly before we have a chance to address them puts all users at risk. Please be responsible and allow us time to investigate and develop a fix.**
*   **Vulnerabilities found on the `beta` branch should be reported as regular issues, not through the security vulnerability reporting process.**

We appreciate your help in keeping the `GASIFHFS` chatbot and its users safe!
