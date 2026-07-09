import boto3
import os

# Configuration
BUCKET_NAME = "pipeline-trafic-web-bi"
FILE_LOCAL = "data/processed/trafic_nettoye.csv"
FILE_S3 = "processed/trafic_nettoye.csv"
REGION = "eu-north-1" 

# Connexion S3
s3 = boto3.client('s3', region_name=REGION)

# Créer le bucket
try:
    s3.create_bucket(
        Bucket=BUCKET_NAME,
        CreateBucketConfiguration={'LocationConstraint': REGION}
    )
    print(f"Bucket '{BUCKET_NAME}' créé avec succès")
except Exception as e:
    print(f"Bucket existant ou erreur : {e}")

# Upload du fichier
try:
    s3.upload_file(FILE_LOCAL, BUCKET_NAME, FILE_S3)
    print(f"Fichier uploadé : s3://{BUCKET_NAME}/{FILE_S3}")
except Exception as e:
    print(f"Erreur upload : {e}")