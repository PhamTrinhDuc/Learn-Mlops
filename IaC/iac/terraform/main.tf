# Ref: https://github.com/terraform-google-modules/terraform-google-kubernetes-engine/blob/master/examples/simple_autopilot_public
# To define that we will use GCP
terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "4.80.0" // Provider version
    }
  }
  required_version = "1.12.2" // Terraform version
}

// The library with methods for creating and
// managing the infrastructure in GCP, this will
// apply to all the resources in the project
provider "google" {
  project     = var.project_id
  region      = var.region
}

// Google Kubernetes Engine
resource "google_container_cluster" "my-gke" {
  name     = "${var.project_id}-new-gke"
  location = var.region
 
  // Enabling Autopilot for this cluster
  enable_autopilot = true
  
  # // Enable Istio (beta)
  # // https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_cluster#nested_istio_config
  # // not yet supported on Autopilot mode
  # addons_config {
  #   istio_config {
  #     disabled = false
  #     auth     = "AUTH_NONE"
  #   }
  # }
}

resource "google_storage_bucket" "my-bucket" {
  name          = var.bucket
  location      = var.region
  force_destroy = true

  uniform_bucket_level_access = true
}