terraform {
  backend "s3" {
    bucket = "bittensor-panel-qxnlar"
    key    = "staging/main.tfstate"
    region = "us-east-1"
  }
}
