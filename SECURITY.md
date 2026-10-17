# Security Policy

## Supported versions

Security fixes are considered for the current default branch. This starter kit is provided as-is; runtime safety depends on the installed Claude Code version, its permission settings, and the surrounding environment.

## Reporting a vulnerability

Please do not publish secrets, tokens, personal data, or exploitable details in a public issue. Use GitHub's private vulnerability reporting feature if it is enabled for this repository. If it is unavailable, contact the repository owner privately through an established channel.

Include the affected file/version, impact, reproducible steps that do not expose secrets, and a suggested mitigation when possible.

## Scope and limitations

- Static validation is not a security certification.
- Local Claude Code deny rules are defense-in-depth, not a security sandbox.
- GitHub branch protection, secret scanning, and push protection require separate repository-owner configuration.
- Never test against systems or credentials you do not own or have explicit permission to assess.
- See [Security Guardrails](docs/security-guardrails.md) for the threat model, known bypasses, and the runtime verification procedure.
