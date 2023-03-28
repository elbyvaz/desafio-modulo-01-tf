resource "aws_s3_bucket" "desafio-modulo-01-tf" {
  bucket = "desafio-modulo-01-tf"
  acl    = "private"

  tags = {
    NAME = "ELBY",
    IES   = "IGTI",
    CURSO = "EDC"
  }

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }
}