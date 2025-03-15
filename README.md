## Markdown Exporter

**Author:** [bowenliang123](https://github.com/bowenliang123)

**Github Repo:** https://github.com/bowenliang123/md_exporter

### Description

This plugin provides tools to export Markdown text to Docx/PDF/HTML/md/Xlsx/CSV/JSON/XML files.

<table>
  <tr>
    <th>Tool</th>
    <th>Input</th>
    <th>Output</th>
  </tr>
  <tr>
    <td><code>md_to_docx</code></td>
    <td rowspan="5">Markdown text</td>
    <td>DOCX file</td>
  </tr>
  <tr>
    <td><code>md_to_html</code></td>
    <td>HTML file</td>
  </tr>
  <tr>
    <td><code>md_to_pdf</code></td>
    <td>PDF file</td>
  </tr>
  <tr>
    <td><code>md_to_md</code></td>
    <td>Markdown file</td>
  </tr>
  <tr>
    <td><code>md_to_xml</code></td>
    <td>XML file</td>
  </tr>
  <tr>
    <td><code>md_to_xlsx</code></td>
    <td><a href="https://www.markdownguide.org/extended-syntax/#tables">Markdown tables</a></td>
    <td>XLSX file</td>
  </tr>
  <tr>
    <td><code>md_to_csv</code></td>
    <td rowspan="4">
      <a href="https://www.markdownguide.org/extended-syntax/#tables">Single Markdown table</a>
  </td>
    <td>CSV file</td>
  </tr>
  <tr>
    <td><code>md_to_json</code></td>
    <td>JSON file</td>
  </tr>
  <tr>
    <td><code>md_to_latex</code></td>
    <td>LaTeX file</td>
  </tr>
</table>

The transformation processes for each file format are as followed:

- Docx file: Markdown > HTML -> Docx file
- HTML file: Markdown -> HTML -> HTML file
- PDF file: Markdown -> HTML -> PDF file
- md file: Markdown -> md file
- XML file: Markdown -> HTML -> XML file
- Xlsx file: Markdown -> HTML -> Pandas DataFrame -> Xlsx file
- CSV file: Markdown -> HTML -> Pandas DataFrame -> CSV file
- JSON file: Markdown -> HTML -> Pandas DataFrame -> JSON file
- LaTeX file: Markdown -> HTML -> Pandas DataFrame -> LaTeX file

## Tools

- `md_to_docx` Tool

  Input Markdown text:

```
# English
The Moon is a celestial body that orbits the Earth, with a diameter of about 3,474 kilometers.

# 月球
月球是一个围绕地球运行的星球，直径约为3474公里。

# 繁体中文
月球是一個圍繞地球運行的星球，直徑約為3474公里。

# 日本語
月は地球の周りを回る天体で、直径は約3474キロメートルです。

# Português
A Lua é um corpo celeste que orbita a Terra, com um diâmetro de cerca de 3.474 quilômetros.
```

usage:

<img src="./_assets/img1.png" width="600px" >

output DOCX file:

<img src="./_assets/img2.png" width="600px" >

- `md_to_html` Tool

output HTML file:

<img src="./_assets/img11.png" width="600px" >

- `md_to_pdf` Tool

- output PDF file:

<img src="./_assets/img12.png" width="600px" >

- `md_to_xlsx` Tool

Input Markdown text:

```
| Name    | Age | City        |
|---------|-----|-------------|
| Alice   | 30  | New York    |
| Bowen   | 25  | Guangzhou   |
| Charlie | 35  | Tokyo       |
| David   | 40  | Miami       |
```

usage:

<img src="./_assets/img3.png" width="600px" >

output XLSX file:

<img src="./_assets/img4.png" width="600px" >

- `md_to_csv` Tool


- `md_to_json` Tool

output JSON file:

<img src="./_assets/img5.png" width="300px" >

- `md_to_xml` Tool

output XML file:

<img src="./_assets/img6.png" width="300px" >

- `md_to_latex` Tool

output LaTex file:

<img src="./_assets/img7.png" width="300px" >

Viewed as PDF:

<img src="./_assets/img8.png" width="300px" >

- `md_to_md` Tool
