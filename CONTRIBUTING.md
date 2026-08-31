# Contributing

Thank you for your interest in the Disuza Quantitative Public Technical
Reference.

## Repository purpose

This repository documents a private, pre-deployment quantitative R&D
initiative. It is a public documentation surface, not a live trading system,
investment product, performance record, or source-code distribution.

[`PUBLIC_FACTS.yml`](PUBLIC_FACTS.yml) is the canonical machine-readable source
for public positioning and status definitions.

## External pull requests

We do not accept unsolicited external pull requests. Public descriptions must
be reconciled against information that is not publicly observable, so an
external contributor cannot independently establish that a proposed capability
statement is safe and accurate.

Documentation clarifications and corrections to publicly observable facts are
welcome as issues.

## Acceptable issues

- Broken links, rendering defects, spelling errors, or ambiguous wording.
- A mismatch between a document and `PUBLIC_FACTS.yml`.
- A missing or incorrect **CURRENT**, **IN PROGRESS**, or **TARGET** label.
- A statement that appears to imply deployment, performance, investment
  activity, legal registration, or regulatory authorization.
- A security concern submitted through the process in
  [`.github/SECURITY.md`](.github/SECURITY.md).

Do not post credentials, private identifiers, unpublished research, security
details, or other sensitive material in a public issue.

## Maintainer publication rules

Every proposed documentation change must satisfy all of the following:

1. **Status-qualified** — capability statements use **CURRENT**,
   **IN PROGRESS**, or **TARGET** with the meanings in `PUBLIC_FACTS.yml`.
2. **Evidence-bounded** — wording does not extend beyond publicly supportable
   facts.
3. **Pre-deployment** — target designs are not presented as integrated,
   deployed, connected to capital, or operating in markets.
4. **Claim-safe** — no returns, alpha, track-record, managed-account, custody,
   investment-service, legal-registration, licensing, approval, or
   authorization claim is introduced.
5. **Disclosure-safe** — no secrets, private IDs, detailed thresholds,
   infrastructure coordinates, proprietary algorithms, or unpublished results
   are included.
6. **Metadata-consistent** — a release updates `README.md`,
   `PUBLIC_FACTS.yml`, `CHANGELOG.md`, `CITATION.cff`, and the organization
   profile to the same version and date.
7. **Licence-consistent** — current public documentation remains CC BY 4.0,
   while historical grants remain described accurately in `NOTICE.md`.

## Style

- Use plain English and define specialized terms.
- Separate facts from intended future state.
- Prefer the narrowest claim that the available evidence supports.
- Use repository-relative links for repository files.
- Do not use promotional, predictive, or performance-oriented language.

## Licence of accepted material

Material intentionally accepted into the current public documentation is
published under [CC BY 4.0](LICENSE), unless a file explicitly states
otherwise. By submitting material for inclusion, an authorized contributor
must have the right to provide it on those terms.

Historical material remains subject to the notice shipped with its exact
version. See [`NOTICE.md`](NOTICE.md).

## Contact

General inquiries: [contact@disuza.com](mailto:contact@disuza.com).

---

Disuza Quantitative Public Technical Reference · v4.0.0 candidate · Unreleased · Last verified 2026-09-01
