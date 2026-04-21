<!--
  This repository does not accept external pull requests.

  If you are outside Disuza Quantitative, please close this PR and open an
  issue instead. We will address documentation corrections or clarifications
  in subsequent internal commits.

  If you are inside Disuza Quantitative, thank you — please remove this
  comment and complete the template below.
-->

## Summary

<!-- What changed and why. One short paragraph. -->

## Consistency with facts.ts

- [ ] I have verified these docs are consistent with the FACTS_PUBLIC export
      in the website repo (`lib/facts.ts`).
- [ ] This PR does not introduce new facts that are not already in the site's
      published `llms.txt` / `llms-full.txt`.

## IP-safety grep

- [ ] I ran the IP-safety grep and it returns `✓ IP-safe`.

## Rendering check

- [ ] I previewed this PR on GitHub and confirmed Mermaid diagrams render
      correctly.
- [ ] Cross-references (links between doc pages) resolve.

## Version bump

If this PR materially changes the documentation surface:

- [ ] I have updated `CHANGELOG.md`.
- [ ] I have updated the `last_updated` HTML comments on every touched page.
- [ ] If this is a new version, I have updated the version marker in the
      root `README.md` and `CITATION.cff`.
