import boto3
import os
import uuid

from storage.aws_config import (
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    AWS_REGION,
    S3_BUCKET_NAME
)


s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)


def upload_file_to_s3(
    file_path,
    folder_name="claims"
):

    file_extension = os.path.splitext(file_path)[1]

    s3_key = (
        folder_name
        + "/"
        + str(uuid.uuid4())
        + file_extension
    )

    s3_client.upload_file(
        file_path,
        S3_BUCKET_NAME,
        s3_key
    )

    return s3_key