from typing import Optional

from tools.utils.mimetype_utils import MimeType


def get_meta_data(mime_type: MimeType, output_filename: Optional[str]) -> dict[str, str]:
    if not MimeType:
        raise ValueError("Failed to generate meta data, mime_type is not defined")

    # normalize the filename
    result_filename: Optional[str] = None
    if output_filename and output_filename.strip():
        # remove the declared extension
        if "." in output_filename:
            result_filename = output_filename.split(".")[0]
        else:
            result_filename = output_filename

    return {
        "mime_type": mime_type,
        "filename": result_filename,
    }
