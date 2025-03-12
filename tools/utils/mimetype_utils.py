from enum import StrEnum


class MimeType(StrEnum):
    CSV = "text/csv"
    HTML = "text/html"
    JSON = "application/json"
    LATEX = "application/x-tex"
    MD = "text/markdown"
    DOCX = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    PDF = "application/pdf"
    XLSX = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    XML = "text/xml"
