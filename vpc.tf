# Create a VPC network
resource "google_compute_network" "vpc_network" {
  name = "terraform-network"
}

resource "google_compute_subnetwork" "subnets" {
  for_each = var.subnets

  name          = each.value.name
  region        = var.region
  network       = google_compute_network.vpc_network.name
  ip_cidr_range = each.value.ip_cidr_range
}

