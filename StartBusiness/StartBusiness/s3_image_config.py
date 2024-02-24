import base64
import six
import uuid
import imghdr
import io
import boto3
from StartBusiness.settings import AWS_STORAGE_BUCKET_NAME
from StartBusiness.settings import AWS_ACCESS_KEY_ID
from StartBusiness.settings import AWS_SECRET_ACCESS_KEY


def get_file_extension(file_name, decoded_file):
    extension = imghdr.what(file_name, decoded_file)
    extension = "jpg" if extension == "jpeg" else extension
    return extension


def decode_base64_file(data):
    # Check if this is a base64 string
    if isinstance(data, six.string_types):
        # Check if the base64 string is in the "data:" format
        if 'data:' in data and ';base64,' in data:
            # Break out the header from the base64 content
            header, data = data.split(';base64,')

        # Try to decode the file. Return validation error if it fails.
        try:
            decoded_file = base64.b64decode(data)
        except TypeError:
            TypeError('invalid_image')

        # Generate file name:
        file_name = str(uuid.uuid4())[:12]  # 12 characters are more than enough.
        # Get the file name extension:
        file_extension = get_file_extension(file_name, decoded_file)

        complete_file_name = "%s.%s" % (file_name, file_extension,)

        return io.BytesIO(decoded_file), complete_file_name


def upload_base64_file(base64_file,folder_name):
    bucket_name = AWS_STORAGE_BUCKET_NAME
    file, file_name = decode_base64_file(base64_file)
    client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    content_type = "image/png"

    file_name = folder_name + "/" + file_name

    client.upload_fileobj(
        file,
        bucket_name,
        file_name,
        ExtraArgs={'ACL': 'public-read', 'ContentType': content_type}
    )
    return f"https://{bucket_name}.s3.amazonaws.com/{file_name}"