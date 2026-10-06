"""Build an offline reading preview from the full course's Markdown sources.

Reads this course only. Writes reading/index.html and reading/build-manifest.json.
No network, server, package installation or remote repository operation.
"""
from pathlib import Path
from urllib.parse import urlsplit, unquote
from markdown_it import MarkdownIt
import hashlib
import html
import json
import re
import unicodedata

BASE = Path(__file__).resolve().parent
COURSE = BASE
OUT = COURSE / "reading"
PAGES = [
    [
        "COURSE-MAP.md",
        "course-map",
        "Your learning route"
    ],
    [
        "lessons/01-everyday-life.md",
        "lesson-1",
        "Lesson 01"
    ],
    [
        "lessons/02-working-with-ai.md",
        "lesson-2",
        "Lesson 02"
    ],
    [
        "lessons/03-evidence-and-trust.md",
        "lesson-3",
        "Lesson 03"
    ],
    [
        "lessons/04-changing-work.md",
        "lesson-4",
        "Lesson 04"
    ],
    [
        "lessons/05-ai-in-society.md",
        "lesson-5",
        "Lesson 05"
    ],
    [
        "lessons/06-skills-worth-developing.md",
        "lesson-6",
        "Lesson 06"
    ],
    [
        "lessons/07-responsibility-and-choice.md",
        "lesson-7",
        "Lesson 07"
    ],
    [
        "lessons/08-next-30-days.md",
        "lesson-8",
        "Lesson 08"
    ],
    [
        "WORKSHEETS.md",
        "workbook",
        "Your workbook"
    ],
    [
        "GLOSSARY.md",
        "glossary",
        "Words and meanings"
    ],
    [
        "SOURCES.md",
        "sources",
        "Sources and edition"
    ],
    [
        "LICENSE.md",
        "reuse",
        "Reuse"
    ]
]
LINKS = {(COURSE / p).resolve(): ident for p, ident, _ in PAGES}
LINKS[(COURSE / "README.md").resolve()] = "overview"

def slug(value):
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9 -]", "", value.lower()).replace(" ", "-")

def render(path, ident):
    md = MarkdownIt("commonmark", {"html": False}).enable("table")
    tokens = md.parse(path.read_text())
    counts = {}
    for i, token in enumerate(tokens):
        if token.type == "heading_open":
            key = slug(tokens[i + 1].content)
            count = counts.get(key, 0)
            counts[key] = count + 1
            token.attrSet("id", ident + "-" + key + (f"-{count}" if count else ""))
            if any(tokens[i+1].content.startswith(s) for s in ("Learn ", "Question ", "Decide ")):
                token.attrSet("class", "step-title")
        if token.type in ("heading_open", "heading_close"):
            token.tag = "h" + str(min(6, int(token.tag[1:]) + 1))
        if token.children:
            for child in token.children:
                if child.type != "link_open":
                    continue
                href = child.attrGet("href")
                u = urlsplit(href)
                if u.scheme or u.netloc:
                    continue
                target = (path.parent / unquote(u.path)).resolve() if u.path else path.resolve()
                if target in LINKS:
                    destination = LINKS[target]
                    child.attrSet("href", "#" + destination + ("-" + unquote(u.fragment) if u.fragment else ""))
                else:
                    # Editor-only documents remain local source links.
                    child.attrSet("href", "../" + target.relative_to(COURSE).as_posix())
    rendered = md.renderer.render(tokens, md.options, {})
    pattern = r'<h4 id="([^"]+)">Compare your reasoning</h4>\s*(.*?)(?=<h[234]\b|\Z)'
    rendered = re.sub(pattern, lambda m: '<details class="answer" id="' + m.group(1) + '"><summary>Compare your reasoning</summary><div class="answer-body">' + m.group(2) + '</div></details>\n', rendered, flags=re.S)
    # Retain table semantics while exposing column labels when rows stack on phones.
    def table_labels(match):
        table = match.group(0)
        labels = re.findall(r"<th[^>]*>(.*?)</th>", table, re.S)
        labels = [re.sub("<[^>]+>", "", x) for x in labels]
        def row_labels(row):
            cells = iter(labels)
            return re.sub(r"<td([^>]*)>", lambda c: '<td' + c.group(1) + ' data-label="' + html.escape(next(cells, ""), quote=True) + '">', row.group(0))
        return re.sub(r"<tr>.*?</tr>", row_labels, table, flags=re.S)
    return re.sub(r"<table>.*?</table>", table_labels, rendered, flags=re.S)

sections = []
for path, ident, tag in PAGES:
    sections.append('<section class="reading-section" id="' + ident + '"><div class="section-tag">' + tag + '</div>' + render(COURSE / path, ident) + '</section>')

css = (BASE / "preview.css").read_text()
document = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Eight lessons to understand AI, explore work and society, strengthen useful skills and choose your next step.">
<title>Your choices matter — Living and Working with AI</title>
<style>""" + css + """</style></head><body>
<a class="skip" href="#lesson-1">Skip to the first lesson</a>
<header class="masthead"><span class="brand">Green Web Land · Learning</span><span class="edition">Full course · Edition 0.2</span></header>
<main>
<section class="hero" id="overview" aria-labelledby="welcome">
 <div><p class="eyebrow">Living and Working with AI</p>
 <h1 id="welcome">Your choices<br>matter.</h1>
 <p class="lead">Understand a changing world.<br>Build useful skills.<br>Choose your next step.</p>
 <div class="hero-actions"><a class="cta" href="#lesson-1">Start learning <span aria-hidden="true">→</span></a><button class="print-button" type="button" id="print">Print the lessons</button></div>
 <p class="sub">Eight lessons · Adult beginners<br>Paper and conversation are enough.</p></div>
 <div><ol class="cycle" aria-label="Learn. Question. Decide.">
 <li><span class="number" aria-hidden="true">01</span><div><strong>Learn.</strong><p>What is happening?<br>What can I understand or practise?</p></div></li>
 <li><span class="number" aria-hidden="true">02</span><div><strong>Question.</strong><p>What supports this?<br>Who could be affected?</p></div></li>
 <li><span class="number" aria-hidden="true">03</span><div><strong>Decide.</strong><p>What will I do, and why?<br>What could change my mind?</p></div></li>
 </ol><p class="revisit">New evidence? Return to Learn.</p></div>
</section>
<section class="journey" aria-labelledby="journey-title">
 <h2 id="journey-title">Begin with something familiar.</h2>
 <p class="intro">Begin with a familiar task. Explore how work and society could change. Strengthen useful skills and make a plan that fits your life. Each lesson asks you to learn, question and explain a choice.</p>
 <div class="lesson-cards">
 <a class="lesson-card" href="#lesson-1"><span class="number">LESSON 01 · EVERYDAY LIFE</span><h3>A message that looks ready.</h3><p>Check what a convincing answer gets right and what needs your judgment.</p><span class="read">Read lesson 1 →</span></a>
 <a class="lesson-card" href="#lesson-2"><span class="number">LESSON 02 · WORKING WITH AI</span><h3>Give a useful idea a shape.</h3><p>Describe a task, examine a response and adapt it when the brief changes.</p><span class="read">Read lesson 2 →</span></a>
 <a class="lesson-card" href="#lesson-3"><span class="number">LESSON 03 · EVIDENCE AND TRUST</span><h3>Follow the claim back.</h3><p>Separate evidence, repetition, predictions and opinions.</p><span class="read">Read lesson 3 →</span></a>
 <a class="lesson-card" href="#lesson-4"><span class="number">LESSON 04 · CHANGING WORK</span><h3>A job is more than one task.</h3><p>Explore skills, opportunity and the decisions that shape a working day.</p><span class="read">Read lesson 4 →</span></a>
 <a class="lesson-card" href="#lesson-5"><span class="number">LESSON 05 · AI IN SOCIETY</span><h3>A faster service for whom?</h3><p>Consider benefits, missing perspectives and the choices around a system.</p><span class="read">Read lesson 5 →</span></a>
 <a class="lesson-card" href="#lesson-6"><span class="number">LESSON 06 · SKILLS WORTH DEVELOPING</span><h3>What can you explain?</h3><p>Use help with a purpose, then practise on a changed example.</p><span class="read">Read lesson 6 →</span></a>
 <a class="lesson-card" href="#lesson-7"><span class="number">LESSON 07 · RESPONSIBILITY AND CHOICE</span><h3>Make the boundary clear.</h3><p>Decide what information, review and correction fit the task.</p><span class="read">Read lesson 7 →</span></a>
 <a class="lesson-card" href="#lesson-8"><span class="number">LESSON 08 · YOUR NEXT 30 DAYS</span><h3>Choose a useful next step.</h3><p>Bring the ideas together and build a plan you can revise.</p><span class="read">Read lesson 8 →</span></a>
 </div>
 <p class="print-note">This edition includes the lesson answers and worksheets. All stories and practice records are invented.</p>
</section>
<div class="reading-layout">
 <nav class="rail" aria-label="Reading navigation"><p>Your learning route</p>
 <a href="#overview">Welcome</a><a href="#course-map">Course map</a><a href="#lesson-1">01 · Everyday life</a><a href="#lesson-2">02 · Working with AI</a><a href="#lesson-3">03 · Evidence and trust</a><a href="#lesson-4">04 · Changing work</a><a href="#lesson-5">05 · AI in society</a><a href="#lesson-6">06 · Skills worth developing</a><a href="#lesson-7">07 · Responsibility and choice</a><a href="#lesson-8">08 · Your next 30 days</a><a href="#workbook">Your workbook</a><a href="#glossary">Glossary</a><a href="#sources">Sources</a><a href="#reuse">Reuse</a></nav>
 <div class="content">""" + "".join(sections) + """</div>
</div></main>
<footer class="footer"><p><strong>Your choices matter. Learn. Question. Decide.</strong></p>
<p>Living and Working with AI · Massoud Fattahi / Green Web Land · Full adult course 0.2<br>
<a href="#reuse">CC BY 4.0 educational content and exceptions</a> · <a href="#sources">Sources and editorial notes</a></p>
<p>Published for learning and feedback. Learner effectiveness has not yet been tested.</p></footer>
<script>
(() => {
 const answers = [...document.querySelectorAll('details.answer')];
 let previous = null;
 const expand = () => { if (previous === null) previous = answers.map(x => x.open); answers.forEach(x => x.open = true); };
 const restore = () => { if (previous === null) return; answers.forEach((x,i) => x.open = previous[i]); previous = null; };
 document.getElementById('print').addEventListener('click', () => window.print());
 window.addEventListener('beforeprint', expand);
 window.addEventListener('afterprint', restore);
})();
</script></body></html>"""

OUT.mkdir(exist_ok=True)
(OUT / "index.html").write_text(document)
inputs = [*COURSE.rglob("*.md"), BASE / "preview.css", Path(__file__)]
manifest = {str(p.relative_to(BASE)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(inputs)}
manifest[str((OUT / "index.html").relative_to(BASE))] = hashlib.sha256(document.encode()).hexdigest()
(OUT / "build-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
print(json.dumps({"preview":str(OUT / "index.html"),"source_documents":len(list(COURSE.rglob("*.md"))),"embedded_sections":len(PAGES),"bytes":len(document.encode())}))
