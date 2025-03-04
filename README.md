## Markdown Exporter

**Author:** [bowenliang123](https://github.com/bowenliang123)

**Github Repo:** https://github.com/bowenliang123/md_exporter

### Description

This plugin provides tools to export Markdown text to Docx/Xlsx/PDF/HTML/md files.
The transformation process for file formats are as follows:

- Docx file: Markdown -> Docx file
- HTML file: Markdown -> HTML text -> HTML file
- PDF file: Markdown -> HTML text -> PDF file
- Xlsx file: Markdown -> HTML -> Pandas Dataframe -> Xlsx file
- md file: A .md file with raw Markdown text

| Tool         | Input                    | Output        |
|--------------|--------------------------|---------------|
| `md_to_docx` | Markdown text            | DOCX file     |
| `md_to_html` | Markdown text            | HTML file     |
| `md_to_pdf`  | Markdown text            | PDF file      |
| `md_to_xlsx` | Table in Markdown syntax | XLSX file     |
| `md_to_md`   | Markdown text            | Markdown file |

- `md_to_docx` Tool

  input markdown text:

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
<img src="./_assets/img1.png" width="100%" >

output DOCX file:
<img src="./_assets/img2.png" width="100%" >

- `md_to_html` Tool

output HTML file:
<img src="./_assets/img11.png" width="100%" >

- `md_to_pdf` Tool

- output PDF file:
  <img src="./_assets/img12.png" width="100%" >

- `md_to_xlsx` Tool

input markdown text:

```
| Name    | Age | City        |
|---------|-----|-------------|
| Alice   | 30  | New York    |
| Bowen   | 25  | Guangzhou   |
| Charlie | 35  | Tokyo       |
| David   | 40  | Miami       |
```

usage:

<img src="./_assets/img3.png" width="100%" >

output XLSX file:

<img src="./_assets/img4.png" width="100%" >

- `md_to_md` Tool
