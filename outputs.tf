output "network_interface" {
  value = google_compute_instance.vm_instance.network_interface
}

output "subnet_ids" {
  value = { for k, v in google_compute_subnetwork.subnets : k => v.id }
}