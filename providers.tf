provider "google" {
  credentials = file("/Users/deepaktharanath/workspace/learn/terraform/graphite-cell-417208-bbebe0526b14.json")
  project = var.project_id
  region  = var.region
}