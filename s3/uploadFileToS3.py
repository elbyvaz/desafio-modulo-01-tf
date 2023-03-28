#importing boto3 library
import boto3

# create a client to interact with AWS S3
s3_client = boto3.client('s3')

# uploading RAIS file
s3_client.upload_file('../RAIS_VINC_PUB_CENTRO_OESTE.csv',   # file to upload
                      'desafio-modulo-01',   # bucket must be created manually
                      'raw/RAIS_VINC_PUB_CENTRO_OESTE.csv')   # destination path must be created manually