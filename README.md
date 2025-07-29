# Markdown Exporter - Generate files from Markdown

**Author:** [bowenliang123](https://github.com/bowenliang123)

**Github Repository:** https://github.com/bowenliang123/md_exporter

**Dify Marketplace:** https://marketplace.dify.ai/plugins/bowenliang123/md_exporter

## Description

This Dify plugin `md_exporter` provides tools to export Markdown text to DOCX, PPTX, XLSX, PDF, HTML, MD, CSV, JSON, XML, LaTex, RST files, and extract code blocks to snippet files as `.py`, `.sh` , `.js`, `.xml` file, and etc.

<table>
  <tr>
    <th>Tool</th>
    <th>
    	Input
    	<p>(Syntax)</p>
    </th>
    <th>Output</th>
  </tr>
  <tr>
    <td><code>md_to_docx</code></td>
    <td rowspan="9">
      <a href="https://daringfireball.net/projects/markdown/syntax">Markdown text</a>
    </td>
    <td>Word file (.docx)</td>
  </tr>
  <tr>
    <td><code>md_to_html</code></td>
    <td>HTML file (.html)</td>
  </tr>
  <tr>
    <td><code>md_to_html_text</code></td>
    <td>HTML text</td>
  </tr>
  <tr>
    <td><code>md_to_pdf</code></td>
    <td>PDF file (.pdf)</td>
  </tr>
  <tr>
    <td><code>md_to_png</code></td>
    <td>
      <div>PNG image (.png) of generated PDF pages.</div>
      Or a ZIP file of image files.
    </td>
  </tr>
  <tr>
    <td><code>md_to_md</code></td>
    <td>Markdown file (.md)</td>
  </tr>
  <tr>
    <td><code>md_to_epub</code></td>
    <td>Epub file (.epub)</td>
  </tr>
  <tr>
    <td><code>md_to_xml</code></td>
    <td>XML file (.xml)</td>
  </tr>
  <tr>
    <td><code>md_to_rst</code></td>
    <td>
      <p>reStructuredText file (.rst)</p>
      [with basic syntax support]
    </td>
  </tr>
  <tr>
    <td><code>md_to_pptx</code></td>
    <td>
      <div>
        Markdown slides
      </div>
      <div>
      with <a href="https://github.com/MartinPacker/md2pptx/blob/master/docs/user-guide.md#creating-slides"> md2pptx </a> style
      </div>
    </td>
    <td>PowerPoint file (.pptx)</td>
  </tr>
  <tr>
    <td><code>md_to_codeblock</code></td>
    <td>
      <div>
      <a href="https://www.markdownguide.org/extended-syntax/#fenced-code-blocks">
        Code Blocks
      </a>
      </div>
      <div>
         in Markdown text
      </div>
    </td>
    <td>
      Generating files by language:
      <ul>
          <li>python → .py file</li>
          <li>javascript → .js file</li>
          <li>html → .html file</li>
          <li>bash → .sh file</li>
          <li>json → .json file</li>
          <li>xml → .xml file</li>
          <li>svg → .svg file</li>
          <li>css → .css file</li>
          <li>yaml → .yaml file</li>
          <li>ruby → .rb file</li>
          <li>java → .java file</li>
          <li>php → .php file</li>
          <li>markdown → .md file</li>
      </ul>
      <div>
      Or a ZIP file of codeblock files.
      </div>
    </td>
  </tr>
  <tr>
    <td><code>md_to_linked_image</code></td>
    <td>
      <div>
      <a href="https://www.markdownguide.org/basic-syntax/#linking-images">
        Linked images
      </a>
      </div>
      <div>
         in Markdown text
      </div>
    </td>
    <td>
      <div>
      Images files from the linked image URLs.
      </div>
      <div>
      Only http or https URLs are supported.
      </div>
    </td>
  </tr>
  <tr>
    <td><code>md_to_xlsx</code></td>
    <td rowspan="5">
      <a href="https://www.markdownguide.org/extended-syntax/#tables">Markdown tables</a>
  </td>
    <td>Excel file (.xlsx)</td>
  </tr>
  <tr>
    <td><code>md_to_csv</code></td>
    <td>CSV file (.csv)</td>
  </tr>
  <tr>
    <td><code>md_to_json</code></td>
    <td>JSON file (.json)</td>
  </tr>
  <tr>
    <td><code>md_to_latex</code></td>
    <td>LaTeX file (.tex)</td>
  </tr>
</table>

## Usage
![](_assets/usage_md_to_docx.png)


## Tools

### Markdown → DOCX
![](_assets/md_to_docx_1.png)

---

### Markdown → XLSX

Input Markdown text:

```
| Name    | Age | City        |
|---------|-----|-------------|
| Alice   | 30  | New York    |
| Bowen   | 25  | Guangzhou   |
| Charlie | 35  | Tokyo       |
| David   | 40  | Miami       |
```


output XLSX file:

![](_assets/md_to_xlsx_1.png)

---

### Markdown → PPTX
The input Markdown text of slides must follows the syle rules of [md2pptx's  syntax](https://github.com/MartinPacker/md2pptx/blob/master/docs/user-guide.md#creating-slides).

<details>

```
# This Is A Presentation Title Page

## This Is A Presentation Section Page

### This Is A Bulleted List Page

* One
    * One A
    * One B
* Two
```
</details>


![](_assets/md_to_pptx_1.png)

---

### Markdown → HTML

![](_assets/md_to_html_1.png)

---

### Markdown → PDF

![](_assets/md_to_pdf_1.png)

---

### Markdown → PNG

![](_assets/md_to_png_1.png)

---

### Markdown → Code Blocks files (.py/.sh/.html/.css, etc.)

  Multiple generated files in formats by language type of the extracted code blocks:
  <ul>
      <li>python → .py file</li>
      <li>javascript → .js file</li>
      <li>html → .html file</li>
      <li>bash → .sh file</li>
      <li>json → .json file</li>
      <li>xml → .xml file</li>
      <li>svg → .svg file</li>
      <li>css → .css file</li>
      <li>yaml → .yaml file</li>
      <li>ruby → .rb file</li>
      <li>java → .java file</li>
      <li>php → .php file</li>
      <li>markdown → .md file</li>
  </ul>

![](_assets/usage_md_to_codeblock_2.png)

If compression is enabled, all the code blocks will be generated into a single ZIP file.
![](_assets/usage_md_to_codeblock_3.png)
![](_assets/usage_md_to_codeblock_4.png)

---

### Markdown → Linked Image files

![](_assets/usage_md_to_linked_image_1.png)

---

### Markdown → RST (reStructedText)

Converted .rst file by using mistune's RST render with basic reStructedText syntax support.

![](_assets/md_to_rst_1.png)

---

### Markdown → CSV


![](_assets/md_to_csv_1.png)


---

### Markdown → JSON

![](_assets/md_to_json_1.png)

---

### Markdown → XML

![](_assets/md_to_xml_1.png)

---

### Markdown → LaTeX

output LaTeX file:

![](_assets/md_to_latex_1.png)

viewed as PDF:

![](_assets/md_to_latex_2.png)

---

### Markdown → Markdown

Output `.md` file with orginal input Markdown text.



---

## Changelog
- 1.9.0:
  - Support custom sheet name in `md_to_xlsx` tool by using headings in Markdown text
  - Force convert column type to string in `md_to_xlsx` tool to prevent data precision loss and display issues in Microsoft Excel
  - Autofit column width in `md_to_xlsx` tool

- 1.8.0:
  - Solve issues with garbled characters when opening CSV files containing non-ASCII characters (eg. Chinese or Japanese characters, Emoji characters etc.) in Microsoft Excel

- 1.7.0:
  - Support custom PPTX template file in `md_to_pptx` tool
  - Support file generation from multiple tables in md_to_csv, md_to_latex, md_to_xlsx tools

- 1.6.0:
  - Introducing `md_to_html_text` tool, support converting Markdown text to HTML text
  - Standardize fonts for headings and body paragraphs DOCX file generated by `md_to_docx` tool

- 1.5.0:
  - Improve PDF display for pure English markdown text input in `md_to_pdf` tool, by skipping the font setting for CJK characters
  - Introduce `md_to_epub` tool, support converting Markdown text to EPUB eBook files
  - Support compressing all png files in single zip file in `md_to_png` tool
  - Increase capacity limit for PDF file to 100MB in `md_to_pdf` tool
  - Remove explicit timeout config MAX_REQUEST_TIMEOUT

- 1.4.100:
  - Special version for celebrating [Dify](https://github.com/langgenius/dify)'s 100k GitHub stars milestone
  - add `md_to_png` tool, support converting Markdown text to PNG image files

- 1.3.0:
  - update SDK version  

- 1.2.0:
  - Support compressing images to single zip file in `md_to_linked_image` tool

- 1.1.0:
  - Enable line breaks normalization in all tools by default, replacing all the occurrences of `\\n` to `\n`
  - Remove `<think>` tags of reasoning content in the input Markdown text
  - Fix missing custom output filename support in md_to_csv, md_to_json, md_to_latex tool

- 1.0.1:
  - Remove redundant URL safe conversion in custom output filename

- 1.0.0:
  - Support customize the output file name

- 0.5.0:
  - Introducing `md_to_linked_image` tool, support extracting image files in links in Markdown text

- 0.4.3:
  - improve the display of Chinese characters in text paragraph in `md_to_docx` tool, by setting global font to Song if content contains Chinese     - improve the display of Chinese characters in text paragraph in `md_to_docx` tool, by setting global font to Song if content contains Chinese charactor

- 0.4.2:
  - support Java, PHP and Ruby file exporting in `md_to_codeblocks` tool

- 0.4.1:
  - support YAML file exporting in `md_to_codeblocks` tool

- 0.4.0:
  - support exporting Markdown codeblocks in to single zip file in `md_to_codeblocks` tool

- 0.3.0:
  - Fixed the error in importing libraries of `md_to_pptx` tool when running on self-hosted Dify plugin-daemon service

- 0.2.0:
  - Introducing `md_to_codeblock` tool, support extracting code blocks in Markdown to Python, JSON, JS, BASH, SVG, HTML, XML, MARKDOWN files. 
  - Introducing `md_to_rst` tool, support reStructuredText `.rst` file format as destination file format

- 0.1.x:
  - Introducing `md_to_pptx` tool, support PowerPoint `.pptx` file format as destination file format

- 0.0.x:
  - Published to Dify Marketplace
  - support exporting Markdown to DOCX, PPTX, XLSX, PDF, HTML, MD, CSV, JSON, XML, LaTex files

## Used Open sourced projects

This Dify plugin uses the following open sourced projects:

- [mark2epub](https://github.com/AlexPof/mark2epub)
- [md2pptx](https://github.com/MartinPacker/md2pptx) , MIT License
- [mistune](https://github.com/lepture/mistune), BSD 3-Clause License
- [pandas](https://github.com/pandas-dev/pandas), BSD 3-Clause License
- [python-docx](https://github.com/python-openxml/python-docx), MIT License
- [python-pptx](https://github.com/scanny/python-pptx), MIT License
- [xhtml2pdf](https://github.com/xhtml2pdf/xhtml2pdf), Apache License 2.0

## License
- Apache License 2.0


## Privacy

This plugin collects no data.

All the file transformations are completed locally. NO data is transmitted to third-party services.
