#!/usr/bin/env python3
"""Render docs/Vektor10-Blog-Guide.pdf — Todd's how-to for publishing blog posts."""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Preformatted, KeepTogether,
)

INK = HexColor('#141413')
TEAL = HexColor('#2E926C')
BONE = HexColor('#F0EEE5')
MUTED = HexColor('#6F6D66')

styles = getSampleStyleSheet()
H1 = ParagraphStyle('h1', parent=styles['Title'], fontName='Helvetica-Bold', fontSize=26, leading=31, textColor=INK, alignment=TA_LEFT, spaceAfter=4)
SUB = ParagraphStyle('sub', parent=styles['Normal'], fontName='Courier', fontSize=10.5, leading=15, textColor=TEAL, spaceAfter=18)
H2 = ParagraphStyle('h2', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=15, leading=19, textColor=INK, spaceBefore=18, spaceAfter=6)
BODY = ParagraphStyle('body', parent=styles['Normal'], fontName='Helvetica', fontSize=10.5, leading=15.5, textColor=INK, spaceAfter=8)
STEP = ParagraphStyle('step', parent=BODY, leftIndent=22, firstLineIndent=-22, spaceAfter=7)
NOTE = ParagraphStyle('note', parent=BODY, textColor=MUTED, fontSize=9.5, leading=13.5)
CODE = ParagraphStyle('code', parent=styles['Code'], fontName='Courier', fontSize=8.8, leading=12.4, textColor=INK, backColor=BONE, borderPadding=8, leftIndent=4, spaceBefore=4, spaceAfter=10)

t = lambda s: f'<font color="#2E926C"><b>{s}</b></font>'
mono = lambda s: f'<font face="Courier">{s}</font>'

doc = SimpleDocTemplate(
    'docs/Vektor10-Blog-Guide.pdf', pagesize=letter,
    leftMargin=0.95 * inch, rightMargin=0.95 * inch, topMargin=0.85 * inch, bottomMargin=0.85 * inch,
    title='Vektor10 — Publishing Blog Posts', author='Vektor10, Inc.',
)
S = []
A = S.append

A(Paragraph('Publishing Blog Posts on vektor10.com', H1))
A(Paragraph('&lt; A GUIDE FOR TODD &middot; NO CODE REQUIRED &gt;', SUB))

A(Paragraph('The big picture', H2))
A(Paragraph(
    'There is no blog dashboard and no CMS login — and that is on purpose. '
    f'Every blog post is just a <b>text file</b> that lives in our GitHub repository. When you add or edit one of these files, '
    f'the website {t("rebuilds and republishes itself automatically")} within about two minutes. '
    'The blog index page, the post page, the social-share previews, and the SEO markup are all generated for you from that one file.', BODY))
A(Paragraph(
    'So the entire job is: <b>1)</b> write your post in a file, <b>2)</b> put it in the right folder on GitHub, <b>3)</b> save. That\'s it.', BODY))

A(Paragraph('Where posts live', H2))
A(Preformatted(
    'github.com/treypreisel/Vektor10\n'
    '  └ src/content/blog/      ← one .md file per post (the words)\n'
    '  └ public/blog/           ← the images your posts use', CODE))
A(Paragraph(
    f'The file name becomes the web address. A file named {mono("why-feeds-matter.md")} '
    f'publishes at {mono("vektor10.com/blog/why-feeds-matter")}. '
    'Use lowercase words separated by hyphens, no spaces or punctuation.', BODY))

A(Paragraph('Step by step: adding a post from your browser', H2))
for i, step in enumerate([
    f'Go to <b>github.com/treypreisel/Vektor10</b> and log in.',
    f'Navigate into {mono("src/content/blog/")}.',
    f'Click {t("Add file → Create new file")} (top right).',
    f'Name it: your post\'s URL slug plus {mono(".md")} — e.g. {mono("the-new-shelf.md")}.',
    'Paste the template from the last page of this guide and replace its contents with your post.',
    f'Click {t("Commit changes…")} (green button), then {t("Commit changes")} again in the popup. '
    'Leave "Commit directly to the main branch" selected.',
    'Wait ~2 minutes, then check <b>vektor10.com/blog</b>. Your post is live.',
], 1):
    A(Paragraph(f'<b>{i}.</b>&nbsp;&nbsp;{step}', STEP))
A(Paragraph('Editing works the same way: open the file on GitHub, click the pencil icon, change the text, commit. '
            'The site republishes automatically every time.', BODY))

A(PageBreak())

A(Paragraph('Anatomy of a post file', H2))
A(Paragraph(
    'Every post has two parts: a <b>header block</b> between two '
    f'{mono("---")} lines (information <i>about</i> the post), followed by the <b>body</b> (the post itself, in plain text). '
    'Here is the header from your eMarketer post:', BODY))
A(Preformatted(
    '---\n'
    'title: "eMarketer says OpenAI misses its $100 billion ad target. I\'ll take that bet."\n'
    'description: "ChatGPT\'s first ad cards look weak - no price, no button, no\n'
    '  reviews. So did Amazon\'s. The floor is the story."\n'
    'date: 2026-06-09\n'
    'readTime: 9 min read\n'
    'heroImage: /blog/emarketer-chart.png\n'
    'heroAlt: "eMarketer\'s OpenAI ad revenue forecast, 2026-2030"\n'
    'canonical: https://www.linkedin.com/pulse/...\n'
    '---', CODE))

rows = [
    ['Field', 'Required?', 'What it does'],
    ['title', 'Yes', 'The headline. Shows on the blog page, the post, Google, and link previews.'],
    ['description', 'Yes', 'One or two sentences. This is what Google and iMessage/Slack previews show under the title - write it like a hook, not a summary.'],
    ['date', 'Yes', 'Publish date as YYYY-MM-DD. Controls ordering; newest post becomes the big featured card on the blog page.'],
    ['readTime', 'No', 'e.g. "7 min read". Rough rule: your word count / 250. Defaults to "5 min read".'],
    ['heroImage', 'No', 'The cover image - its address inside the site, e.g. /blog/my-chart.png. Used at the top of the post, on the blog index card, and as the link-preview image.'],
    ['heroAlt', 'No', 'One line describing the image. Doubles as the caption under it and helps SEO/accessibility.'],
    ['canonical', 'No', 'If the post first appeared on LinkedIn, paste that URL here. Tells Google "the original lives there" so we are not penalized for duplicate content.'],
    ['author / role', 'No', 'Already default to you. Only add these if someone else writes a post.'],
]
table = Table(rows, colWidths=[1.05 * inch, 0.8 * inch, 4.55 * inch])
cell = ParagraphStyle('cell', parent=BODY, fontSize=9, leading=12.5, spaceAfter=0)
cellb = ParagraphStyle('cellb', parent=cell, fontName='Courier-Bold')
head = ParagraphStyle('head', parent=cell, fontName='Helvetica-Bold', textColor=HexColor('#FFFFFF'))
data = [[Paragraph(c, head) for c in rows[0]]] + [
    [Paragraph(r[0], cellb), Paragraph(r[1], cell), Paragraph(r[2], cell)] for r in rows[1:]
]
table = Table(data, colWidths=[1.05 * inch, 0.8 * inch, 4.55 * inch], repeatRows=1)
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), INK),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [HexColor('#FFFFFF'), BONE]),
    ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#B5B2AB')),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('LEFTPADDING', (0, 0), (-1, -1), 6), ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ('TOPPADDING', (0, 0), (-1, -1), 5), ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
]))
A(table)
A(Spacer(1, 6))
A(Paragraph('Two gotchas: keep the quotes around title/description if they contain a colon or apostrophe '
            '(when in doubt, just always use quotes), and keep the date format exactly YYYY-MM-DD.', NOTE))

A(PageBreak())

A(Paragraph('Writing the body (formatting cheat sheet)', H2))
A(Paragraph(
    'The body is plain text with a few simple symbols, called Markdown. The site translates each one into our house style automatically — '
    'you never pick fonts, sizes, or colors. What you type on the left renders as described on the right:', BODY))
rows2 = [
    ['You type…', 'The site renders…'],
    ['A blank line between paragraphs', 'Normal paragraph spacing. (A single line break is NOT a new paragraph - leave an empty line.)'],
    ['## The New Shelf', 'A section heading in our display font. Use these to break up long posts. Always two # symbols.'],
    ['**bold words**', 'Bold, slightly darker ink - good for the punchline of a paragraph.'],
    ['*italic words*', 'Italics.'],
    ['> A line starting with >', 'A pull quote: large teal display text with a vertical rule - the signature look from your eMarketer post ("I read it the other way").'],
    ['- item one (each on its own line)', 'A bulleted list.'],
    ['[anchor text](https://example.com)', 'A link. The words in [brackets] are clickable; the address goes in (parentheses).'],
    ['![chart](/blog/my-chart.png)', 'An image, full column width, with the site\'s card border and shadow.'],
    ['*ChatGPT Ad Example*', 'SPECIAL: an italic line alone in its own paragraph right after an image becomes a small centered caption under it.'],
]
data2 = [[Paragraph(c, head) for c in rows2[0]]] + [
    [Paragraph(r[0].replace('<', '&lt;'), cellb), Paragraph(r[1], cell)] for r in rows2[1:]
]
table2 = Table(data2, colWidths=[2.35 * inch, 4.05 * inch], repeatRows=1)
table2.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), INK),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [HexColor('#FFFFFF'), BONE]),
    ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#B5B2AB')),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('LEFTPADDING', (0, 0), (-1, -1), 6), ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ('TOPPADDING', (0, 0), (-1, -1), 5), ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
]))
A(table2)

A(Paragraph('Images', H2))
for i, step in enumerate([
    f'On GitHub, go to {mono("public/blog/")} and click {t("Add file → Upload files")}. Drag your image in and commit.',
    f'Give it a simple lowercase name first, e.g. {mono("shelf-chart.png")} — the name is part of its address.',
    f'Reference it from your post as {mono("/blog/shelf-chart.png")} — either as the {mono("heroImage")} in the header, '
    f'or in the body with {mono("![description](/blog/shelf-chart.png)")}.',
    'For an in-body caption, put an italic line directly under the image (see the cheat sheet above).',
], 1):
    A(Paragraph(f'<b>{i}.</b>&nbsp;&nbsp;{step}', STEP))
A(Paragraph('Wide images look best (roughly 2:1, at least 1200px across) - the hero spans the full article width.', NOTE))

A(PageBreak())

A(Paragraph('If something looks wrong', H2))
for issue, fix in [
    ('Post isn\'t showing up after ~5 minutes',
     'Usually a header typo - a missing quote or a malformed date stops the whole site from rebuilding (your post will not half-publish; nothing changes until the file is valid). Open the file, compare against the template, fix, commit again.'),
    ('Image is a broken square',
     'The address doesn\'t match the file. Check the file is in public/blog/ and that the path in your post starts with /blog/ and matches the name exactly, including .png vs .jpg.'),
    ('Pull quote / heading isn\'t styled',
     'The > or ## needs to start its own paragraph - blank line before and after.'),
    ('Anything else',
     'Nothing you commit can break the layout or other pages - worst case the site simply keeps showing the previous version. Ping Trey and it\'s a quick fix.'),
]:
    A(Paragraph(f'<b>{issue}.</b> {fix}', BODY))

A(Paragraph('Copy-paste template for every new post', H2))
A(Preformatted(
    '---\n'
    'title: "Your headline here"\n'
    'description: "The one-sentence hook that shows up in Google and link previews."\n'
    'date: 2026-06-20\n'
    'readTime: 6 min read\n'
    'heroImage: /blog/your-cover-image.png\n'
    'heroAlt: "One line describing the cover image"\n'
    '---\n'
    '\n'
    'Your opening paragraph.\n'
    '\n'
    '## A Section Heading\n'
    '\n'
    'More paragraphs. **Bold the line that matters.**\n'
    '\n'
    '> A pull quote that deserves the big teal treatment.\n'
    '\n'
    '![A chart worth a thousand words](/blog/your-inline-image.png)\n'
    '\n'
    '*Caption for the image above*\n'
    '\n'
    'Closing paragraph.', CODE))
A(Paragraph('Vektor10, Inc. - internal guide - June 2026. The live reference copy lives in the repo at docs/Vektor10-Blog-Guide.pdf.', NOTE))

doc.build(S)
print('built docs/Vektor10-Blog-Guide.pdf')
