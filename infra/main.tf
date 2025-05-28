module "eks_cluster" {
  source = "terraform-aws-modules/eks/aws"
  cluster_name = "mechbot-prod"
  node_groups = {
    main = {
      desired_capacity = 5
      max_capacity     = 10
      instance_types  = ["m6i.2xlarge"]
    }
  }
}
```

**Comandos**:  
# Planificar cambios
terraform plan -out=tfplan

# Aplicar infraestructura
terraform apply tfplan
