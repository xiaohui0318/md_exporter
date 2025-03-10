from enum import StrEnum


class MimeType(StrEnum):
    CSV = "text/csv"
    JSON = "application/json"
    MD = "text/markdown"
    DOCX = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    PDF = "application/pdf"
    XLSX = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
