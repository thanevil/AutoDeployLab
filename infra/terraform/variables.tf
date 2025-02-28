variable "subnet_ids" {
  description = "List of subnet IDs for EKS"
  type        = list(string)
  default     = []
}
