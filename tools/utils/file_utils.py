from typing import Optional

from tools.utils.mimetype_utils import MimeType


def get_meta_data(mime_type: MimeType, output_filename: Optional[str]) -> dict[str, str]:
    if not MimeType:
        raise ValueError("Failed to generate meta data, mime_type is not defined")

    # normalize the filename
    result_filename: Optional[str] = None
    if output_filename and output_filename.strip():
        # ensure extension name
        temp_filename = output_filename.strip()
        extension = MimeType.get_extension(mime_type)
        if temp_filename.lower().endswith(extension):
            result_filename = temp_filename
        else:
            result_filename = f"{temp_filename}{extension}"

    return {
        "mime_type": mime_type,
        "filename": result_filename,
    }
