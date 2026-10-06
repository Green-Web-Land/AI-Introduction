# Maintaining this edition

[Course home](README.md)

Edition 0.2.1, published 6 October 2026. Markdown is the source for the lessons, workbook, glossary, map, source notes and reuse notice. The HTML and PDF are companion formats.

## Rebuild the reading edition

Use Python 3.10 or later with the dependency in requirements.txt. A virtual environment is suitable if you need to install it. From this course directory, run:

```sh
python3 build-reading.py
```

The builder reads the local course Markdown and preview.css, then writes reading/index.html and reading/build-manifest.json. It does not contact a service, start a server or install packages. The manifest records SHA-256 hashes for its source files, style, builder and generated HTML. It does not cover the PDF.

Open reading/index.html locally in a browser. The HTML contains its styles and print behaviour; it has no required external font, image, script or account. Supporting source links still need the internet, and editor-only links need the course folder.

## Regenerate the PDF

After rebuilding, open the HTML and use “Print the lessons.” Save as PDF using the supplied A4 page style and background graphics. Answers expand before printing and return to their previous state afterwards. Verify that all 17 answer explanations are present.

The supplied PDF was generated with Chromium 153.0.8010.12, A4 print styling and backgrounds, with page-number footers. It contains 44 pages. Fonts, browser versions and printer settings can change pagination and binary output; inspect the generated copy instead of assuming byte-for-byte reproduction. Save it as reading/living-working-ai.pdf.

## Check an update

Read the changed examples and answer reasoning. Recheck the sources behind changed factual claims, arithmetic, all affected lesson/worksheet links and the distinction between invented scenarios and observed results. Check the HTML at desktop and narrow phone widths, operate answer controls with a keyboard, and inspect printed tables and page breaks. Verify the source and rendered copies agree.

Author checks for this edition covered local references, eight lesson sequences, answer reveals, keyboard navigation, widths from 320 to 1440 CSS pixels and print answers. They do not establish learner effectiveness or full accessibility certification. Use the [facilitator guide](FACILITATOR-GUIDE.md) to plan meaningful reader feedback.

Keep the edition label and [source record](SOURCES.md) current. Preserve links where possible and retain the [reuse notice](LICENSE.md).
