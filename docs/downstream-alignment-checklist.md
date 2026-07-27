# Downstream Alignment Checklist

> **Version 4.0.0 · Prepared 2026-07-27**

This checklist is a separate follow-up scope. Version 4.0.0 changes none of the
surfaces below.

The canonical input for every later alignment is
[`PUBLIC_FACTS.yml`](../PUBLIC_FACTS.yml). No downstream surface may be updated
by copying unsupported claims from an older public page.

## TARGET — release boundary

- [ ] Confirm the public repository v4.0.0 has been squash-merged and released.
- [ ] Record the actual merge date and final public wording as the alignment
      baseline.
- [ ] Keep website, social, and machine-readable changes in separate reviewed
      change sets.
- [ ] Remove live, production, performance, investment-service, legal-status,
      and regulatory-readiness claims unless separately evidenced and approved.
- [ ] Preserve **CURRENT**, **IN PROGRESS**, and **TARGET** distinctions.

## TARGET — website and guest surface

- [ ] Align `disuza.com` identity, lifecycle, markets, horizon, methodology,
      capabilities, non-claims, contact, version, and date.
- [ ] Keep target architecture visibly labelled **TARGET — not deployed**.
- [ ] Remove or disable `/guest` promotion until its content and data contract
      pass the same factual, privacy, legal, and link review.
- [ ] Verify navigation, Open Graph metadata, structured data, and legal footer.

## TARGET — machine-readable website files

- [ ] Align `llms.txt` with the exact canonical positioning and explicit
      non-claims.
- [ ] Align `llms-full.txt` with the same status vocabulary and remove
      superseded v3 claims.
- [ ] Confirm neither file exposes internal identifiers, results, datasets,
      thresholds, infrastructure coordinates, counterparties, or private
      repository information.

## TARGET — external identity surfaces

- [ ] Align this repository's GitHub **About** description, homepage preview,
      and topics; remove stale cloud, production, legal-status, and
      regulatory-readiness markers before claiming cross-surface alignment.
- [ ] Open a separate reviewed PR in the organization-level public `.github`
      repository to synchronize its `profile/README.md` from the approved
      `.github/profile/README.md` mirror in this release.
- [ ] Verify the public organization Overview after that profile PR merges.
- [ ] Align the LinkedIn organization description, location wording, website
      preview, and capability claims.
- [ ] Review Wikidata statements independently; correct only facts supported by
      reliable public sources and platform policy.
- [ ] Align page titles, descriptions, Open Graph fields, social cards,
      canonical URLs, robots metadata, and structured SEO data.

## TARGET — independent acceptance

- [ ] The non-author founder approves biography, contact, and licence wording.
- [ ] Every surface is checked against `PUBLIC_FACTS.yml`.
- [ ] Links, previews, and machine-readable metadata are verified after
      publication.
- [ ] No downstream alignment is represented as part of repository v4.0.0.

---

*Disuza Quantitative — downstream follow-up scope · Version 4.0.0 ·
2026-07-27*
