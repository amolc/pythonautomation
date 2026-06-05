#!/usr/bin/env python3
import os
import re
import sys
from pathlib import Path
import markdown
from xhtml2pdf import pisa

BASE = Path(__file__).resolve().parent.parent
COURSE = BASE / "course"

CSS_STYLE = """
@page {
    size: a4 portrait;
    margin-top: 60pt;
    margin-bottom: 60pt;
    margin-left: 54pt;
    margin-right: 54pt;
    @frame header {
        -pdf-frame-content: header-content;
        top: 25pt;
        left: 54pt;
        right: 54pt;
        height: 20pt;
    }
    @frame footer {
        -pdf-frame-content: footer-content;
        bottom: 25pt;
        left: 54pt;
        right: 54pt;
        height: 20pt;
    }
}
@page cover {
    margin: 0;
    @frame header {
        -pdf-frame-content: none;
    }
    @frame footer {
        -pdf-frame-content: none;
    }
}

body {
    font-family: Helvetica, Arial, sans-serif;
    color: #1F2937;
    font-size: 10.5pt;
    line-height: 1.6;
}

h1, h2, h3, h4 {
    font-family: Helvetica, Arial, sans-serif;
    color: #1E3A8A;
    font-weight: bold;
}

h1 {
    font-size: 22pt;
    margin-top: 30pt;
    margin-bottom: 15pt;
    page-break-before: always;
}

h2 {
    font-size: 15pt;
    margin-top: 20pt;
    margin-bottom: 10pt;
    border-bottom: 1px solid #E5E7EB;
    padding-bottom: 4pt;
    page-break-inside: avoid;
}

h3 {
    font-size: 12pt;
    margin-top: 15pt;
    margin-bottom: 6pt;
    color: #D97706;
    page-break-inside: avoid;
}

p {
    margin-bottom: 10pt;
    text-align: justify;
}

ul, ol {
    margin-bottom: 10pt;
    padding-left: 20pt;
}

li {
    margin-bottom: 4pt;
}

pre {
    background-color: #F3F4F6;
    border: 1px solid #E5E7EB;
    padding: 10pt;
    margin-top: 8pt;
    margin-bottom: 12pt;
    page-break-inside: avoid;
}

code {
    font-family: Courier, monospace;
    font-size: 9.5pt;
    background-color: #F3F4F6;
    padding: 1px 3px;
}

pre code {
    display: block;
    line-height: 1.4;
    white-space: pre-wrap;
    background-color: transparent;
    padding: 0;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 10pt;
    margin-bottom: 15pt;
    page-break-inside: avoid;
}

th, td {
    border: 1px solid #E5E7EB;
    padding: 8pt;
    text-align: left;
}

th {
    background-color: #1E3A8A;
    color: white;
    font-weight: bold;
}

tr:nth-child(even) {
    background-color: #F9FAFB;
}

.cover {
    page-break-after: always;
    page: cover;
    background-color: #1E3A8A;
    color: white;
    padding: 180pt 54pt 54pt 54pt;
    height: 100%;
}

.cover h1 {
    font-size: 32pt;
    color: #FFFFFF;
    margin-bottom: 10pt;
    page-break-before: avoid;
    font-weight: bold;
    text-align: left;
}

.cover .subtitle {
    font-size: 18pt;
    color: #D97706;
    margin-bottom: 80pt;
    text-align: left;
}

.cover .meta {
    font-size: 11pt;
    color: #9CA3AF;
    margin-top: 120pt;
    border-top: 1px solid #374151;
    padding-top: 15pt;
    text-align: left;
}

.cover .meta-item {
    margin-bottom: 4pt;
}

.toc-title {
    font-size: 22pt;
    margin-bottom: 20pt;
    page-break-before: always;
}

.toc-list {
    padding-left: 0;
}

.toc-item {
    margin-bottom: 6pt;
    list-style-type: none;
}

.toc-module {
    font-weight: bold;
    color: #1E3A8A;
    font-size: 11pt;
    margin-top: 10pt;
}

.toc-chapter {
    padding-left: 15pt;
    color: #4B5563;
    font-size: 10pt;
}

#header-content {
    font-size: 8.5pt;
    color: #9CA3AF;
    border-bottom: 1px solid #E5E7EB;
    padding-bottom: 3pt;
    text-align: right;
}

#footer-content {
    font-size: 8.5pt;
    color: #9CA3AF;
    border-top: 1px solid #E5E7EB;
    padding-top: 3pt;
    text-align: center;
}
"""

def get_chapters_from_readme(readme_path):
    chapters = []
    if not readme_path.exists():
        return chapters
        
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Locate Chapters section
    lines = content.split('\n')
    in_chapters = False
    for line in lines:
        if "## Chapters" in line:
            in_chapters = True
            continue
        if in_chapters:
            # If we reach another header, we stop parsing
            if line.strip().startswith("##") and not "Chapters" in line:
                break
            # Find markdown links like [Text](./slug.md) or [Text](slug.md)
            match = re.search(r"\[(.*?)\]\(\.?\/?(.*?)\.md\)", line)
            if match:
                title, slug = match.groups()
                chapters.append((title, slug))
    return chapters

def clean_chapter_markdown(md_content):
    lines = md_content.split('\n')
    cleaned_lines = []
    skipped_header = False
    for line in lines:
        if "**Course:**" in line or "**Module" in line:
            continue
        if line.strip() == "---" and not skipped_header:
            skipped_header = True
            continue
        cleaned_lines.append(line)
    return '\n'.join(cleaned_lines)

def build_pdf():
    print("Starting PDF Book Generation...")
    
    # 1. Collect all modules
    module_dirs = sorted(
        [d for d in COURSE.iterdir() if d.is_dir() and d.name.startswith("module-")],
        key=lambda x: int(x.name.split("-")[1])
    )
    
    compilation_data = []
    toc_data = []
    
    for mod_dir in module_dirs:
        # Get module number and title
        match = re.match(r"module-(\d+)-(.*)", mod_dir.name)
        if not match:
            continue
        mod_num = int(match.group(1))
        mod_slug = match.group(2)
        
        # Read module title from README.md first line
        readme_path = mod_dir / "README.md"
        mod_title = mod_slug.replace("-", " ").title()
        if readme_path.exists():
            with open(readme_path, "r", encoding="utf-8") as f:
                first_line = f.readline().strip()
                if first_line.startswith("#"):
                    mod_title = first_line.lstrip("#").strip().replace(f"Module {mod_num}:", "").strip()
        
        print(f"Parsing Module {mod_num}: {mod_title}")
        
        chapters = get_chapters_from_readme(readme_path)
        
        mod_anchor = f"module-{mod_num}"
        toc_data.append({
            "type": "module",
            "title": f"Module {mod_num}: {mod_title}",
            "anchor": mod_anchor,
            "chapters": []
        })
        
        # We append a Module Cover/Header block
        compilation_data.append(f'<h1 id="{mod_anchor}">Module {mod_num}: {mod_title}</h1>\n')
        
        # Read chapters
        for ch_title, ch_slug in chapters:
            ch_file = mod_dir / f"{ch_slug}.md"
            if not ch_file.exists():
                print(f"  ⚠️ Warning: Chapter file {ch_file} not found!")
                continue
                
            ch_anchor = f"module-{mod_num}-{ch_slug}"
            toc_data[-1]["chapters"].append({
                "title": ch_title,
                "anchor": ch_anchor
            })
            
            with open(ch_file, "r", encoding="utf-8") as f:
                ch_content = f.read()
                
            # Clean up headers
            ch_content = clean_chapter_markdown(ch_content)
            
            # Convert to HTML
            ch_html = markdown.markdown(
                ch_content, 
                extensions=['extra', 'codehilite', 'tables']
            )
            
            # Ensure the main chapter heading has the proper anchor
            # Replace the first <h1> with a customized anchor
            ch_html = re.sub(
                r"<h1>(.*?)</h1>", 
                rf'<h2 id="{ch_anchor}">\1</h2>', 
                ch_html, 
                count=1
            )
            
            compilation_data.append(ch_html)
            compilation_data.append('<div style="page-break-after: always;"></div>\n')

    # 2. Build full HTML document
    html_out = []
    html_out.append('<!DOCTYPE html>\n<html>\n<head>\n<meta charset="utf-8">\n')
    html_out.append(f'<style>{CSS_STYLE}</style>\n</head>\n<body>\n')
    
    # Running header/footer content
    html_out.append('<div id="header-content">Automation using Python — Complete Course Book</div>\n')
    html_out.append('<div id="footer-content">Page <pdf:pagenumber/> of <pdf:pagecount/></div>\n')
    
    # Cover Page
    html_out.append('<div class="cover">\n')
    html_out.append('<h1>Automation using Python</h1>\n')
    html_out.append('<div class="subtitle">Complete Course Book (Modules 1 - 19)</div>\n')
    html_out.append('<div class="meta">\n')
    html_out.append('<div class="meta-item"><strong>Instructor:</strong> Amol Chawathe</div>\n')
    html_out.append('<div class="meta-item"><strong>Platform:</strong> Quantbots.co</div>\n')
    html_out.append('<div class="meta-item"><strong>Generated:</strong> June 2026</div>\n')
    html_out.append('</div>\n')
    html_out.append('</div>\n')
    
    # Table of Contents Page
    html_out.append('<div class="toc-title">Table of Contents</div>\n')
    html_out.append('<ul class="toc-list">\n')
    for mod in toc_data:
        html_out.append(f'<li class="toc-item toc-module"><a href="#{mod["anchor"]}">{mod["title"]}</a></li>\n')
        for ch in mod["chapters"]:
            html_out.append(f'<li class="toc-item toc-chapter"><a href="#{ch["anchor"]}">{ch["title"]}</a></li>\n')
    html_out.append('</ul>\n')
    html_out.append('<div style="page-break-after: always;"></div>\n')
    
    # Append Compiled Chapters
    html_out.extend(compilation_data)
    
    html_out.append('</body>\n</html>\n')
    
    full_html = "".join(html_out)
    
    # Save raw HTML for debugging/reference
    html_file = COURSE / "Python_Automation_Complete_Course.html"
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Saved compiled HTML structure: {html_file}")
    
    # Convert HTML to PDF
    pdf_file = COURSE / "Python_Automation_Complete_Course.pdf"
    print(f"Rendering PDF to: {pdf_file}...")
    with open(pdf_file, "wb") as f_pdf:
        pisa_status = pisa.CreatePDF(full_html, dest=f_pdf)
        
    if pisa_status.err:
        print("❌ Error: PDF Generation failed.")
        sys.exit(1)
    else:
        print(f"🎉 PDF Generation complete! Size: {os.path.getsize(pdf_file)} bytes")

if __name__ == "__main__":
    build_pdf()
