# Developer integration guide

[Home](README.md) · [Curriculum](CURRICULUM.md)

This repository contains educational Markdown, not a runtime subsystem. It is independently readable. Developers own application integration and its tests. No WebAI source or executable is included.

## Content contract

- Use the displayed curriculum order: 01, 09, 02, 03, 04, 05, 06, 07, 08. Stable lesson IDs are identifiers, not sorting instructions.
- README is the entry point; CURRICULUM is the index; lessons contain explanations and answer guidance; GLOSSARY and SOURCES are shared supporting pages.
- Preserve relative links, headings, example labels, uncertainty, source references and the distinction between proposed principles and existing obligations.
- Avoid showing draft lessons as legally cleared or describing authored examples as recorded AI outputs.

## Our integration workflow

The steps below govern the project's own development and publication workflow. They are not extra conditions on third-party reuse under [CC BY 4.0](LICENSE.md).

## Consume a reviewed version

1. Identify the exact content revision and its review status. Private main is not automatically a public-release version.
2. Apply [CC BY 4.0 and the scope notice](LICENSE.md): retain required attribution/notices, link the licence and indicate changes. Third-party source terms remain separate; WebAI software is not licensed by this educational notice.
3. Copy the necessary pages and supporting source/notices from that pinned revision into your own project. Keep an origin/revision record there. Avoid a runtime dependency on a changing branch.
4. Adapt navigation and presentation while retaining meaning. Rewriting claims, removing safeguards, adding translations or changing examples requires affected editorial and assessment review.
5. Verify every internal link, table, heading, keyboard navigation and readable layout in your application. Test with the actual renderer and assistive technology appropriate to the product; a Markdown link check does not establish accessibility compliance.
6. If the approved content must work offline, include the linked internal pages and explain that external references may need internet access. No offline source copies are included here.

## Release boundary

Owner approval of the exact candidate/action/destination comes before the designated legal decision. Pending or declined review does not authorise our own publication. This workflow does not restrict other recipients' CC BY 4.0 rights. Product deployment has its own applicable acceptance requirements. Do not silently synchronise draft edits into production.

## Report a correction

Provide the pinned revision, page and heading, the incorrect or unclear statement, supporting evidence and proposed remedy through the project's authorised review channel. Use synthetic examples. Do not add customer records, secrets or internal legal discussion to the content tree or public history.
