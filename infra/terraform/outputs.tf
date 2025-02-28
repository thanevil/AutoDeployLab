output "cluster_name" {
  value = aws_eks_cluster.autodeploylab.name
}

output "cluster_endpoint" {
  value = aws_eks_cluster.autodeploylab.endpoint
}

output "node_group_arn" {
  value = aws_eks_node_group.node_group.arn
}
