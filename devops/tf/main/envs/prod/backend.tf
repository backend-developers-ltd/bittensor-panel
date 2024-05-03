terraform {
  backend "s3" {
    bucket = "bittensor-panel-qxnlar"
    key    = "prod/main.tfstate"
    region = "us-east-1"
  }
}
