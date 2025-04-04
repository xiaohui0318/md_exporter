from enum import StrEnum


class MimeType(StrEnum):
    CSS = "text/css"
    CSV = "text/csv"
    DOCX = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    HTML = "text/html"
    JS = "text/javascript"
    JSON = "application/json"
    LATEX = "application/x-tex"
    MD = "text/markdown"
    PDF = "application/pdf"
    PPTX = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
    PY = "text/x-python"
    RST = "text/prs.fallenstein.rst"
    TXT = "text/plain"
    SH = "application/x-sh"
    SVG = "image/svg+xml"
    XLSX = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    XML = "text/xml"
    YAML = "text/yaml"
    ZIP = "application/zip"
