resource "google_compute_instance" "vm_instance" {
  name         = "example-instance"
  machine_type = "e2-micro"
  zone         = var.zone

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-10"
    }
  }

  network_interface {
    network = google_compute_network.vpc_network.id
    access_config {}
  }
  allow_stopping_for_update = true
}
