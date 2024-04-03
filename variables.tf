variable "project_id" {
  description = "The GCP project ID"
}

variable "region" {
  description = "The GCP region"
  default     = "europe-west2"
}

variable "zone" {
  description = "The GCP zone"
  default     = "europe-west2-c"
}

variable "subnets" {
  default = {
    subnet1 = {
      name          = "subnet1"
      ip_cidr_range = "10.0.1.0/24"
    }
    subnet2 = {
      name          = "subnet2"
      ip_cidr_range = "10.0.2.0/24"
    }
  }
}