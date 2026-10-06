# Developer integration guide

[Home](README.md) · [Curriculum](CURRICULUM.md)

This repository contains educational Markdown, not a runtime subsystem. It is independently readable. Developers own application integration and its tests. No WebAI source or executable is included.

## Content contract

- Use the displayed curriculum order: 01, 09, 02, 03, 04, 05, 06, 07, 08. Stable lesson IDs are identifiers, not sorting instructions.
- README is the entry point; CURRICULUM is the index; lessons contain explanations and answer guidance; GLOSSARY and SOURCES are shared supporting pages.
- Preserve relative links, headings, example labels, uncertainty, source references and the distinction between proposed principles and existing obligations.
- Keep authored examples labelled as fictional; do not describe them as recorded AI outputs or evidence of learning effectiveness.

## Integrate a specific revision

1. Choose a published content revision and record its commit identifier so the source of your copy is clear.
2. Apply [CC BY 4.0 and the scope notice](LICENSE.md): retain required attribution/notices, link the licence and indicate changes. Third-party source terms remain separate; WebAI software is not licensed by this educational notice.
3. Copy the necessary pages and supporting source/notices from that pinned revision into your own project. Keep an origin/revision record there. Avoid a runtime dependency on a changing branch.
4. Adapt navigation and presentation while retaining meaning. Rewriting claims, removing safeguards, adding translations or changing examples requires affected editorial and assessment review.
5. Verify every internal link, table, heading, keyboard navigation and readable layout in your application. Test with the actual renderer and assistive technology appropriate to the product; a Markdown link check does not establish accessibility compliance.
6. If your edition must work offline, include the linked internal pages and explain that external references may need internet access. No offline source copies are included here.

## Maintain your copy

Review changes before updating your copy. Check affected examples, answer guidance, sources and links together. Pin the revision you distribute so a changing branch cannot silently alter the material readers receive.

## Report a correction

When reporting a correction, include the content revision, page and heading, the statement that needs attention, supporting evidence and a suggested correction. Use invented examples and leave out personal information, customer records and secrets.
