from enum import StrEnum


class MimeType(StrEnum):
    CSV = "text/csv"
    DOCX = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    HTML = "text/html"
    JSON = "application/json"
    LATEX = "application/x-tex"
    MD = "text/markdown"
    PDF = "application/pdf"
    RST = "text/x-rst"
    XLSX = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    XML = "text/xml"
