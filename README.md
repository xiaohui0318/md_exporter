## Markdown Exporter

**Author:** [bowenliang123](https://github.com/bowenliang123)

**Github Repo:** https://github.com/bowenliang123/md_exporter

### Description

This plugin provides tools to export Markdown text to Docx/PDF/HTML/md/Xlsx/CSV/JSON files.
The transformation process for file formats are as follows:

- Docx file: Markdown -> Docx file
- HTML file: Markdown -> HTML -> HTML file
- PDF file: Markdown -> HTML -> PDF file
- md file: Markdown -> md file
- Xlsx file: Markdown -> HTML -> Pandas DataFrame -> Xlsx file
- CSV file: Markdown -> HTML -> Pandas DataFrame -> CSV file
- JSON file: Markdown -> HTML -> Pandas DataFrame -> JSON file
- XML file: Markdown -> HTML -> Pandas DataFrame -> XML file

| Tool         | Input                           | Output        |
|--------------|---------------------------------|---------------|
| `md_to_docx` | Markdown text                   | DOCX file     |
| `md_to_html` | Markdown text                   | HTML file     |
| `md_to_pdf`  | Markdown text                   | PDF file      |
| `md_to_md`   | Markdown text                   | Markdown file |
| `md_to_xlsx` | Tables in Markdown syntax       | XLSX file     |
| `md_to_csv`  | Single table in Markdown syntax | CSV file      |
| `md_to_json` | Single table in Markdown syntax | JSON file     |
| `md_to_xml`  | Single table in Markdown syntax | XML file      |

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

- `md_to_md` Tool
