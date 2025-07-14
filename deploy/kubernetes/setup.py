# Cluster initialization
eksctl create cluster \
  --name mechbot-prod \
  --nodes 3 \
  --node-type m6i.2xlarge \
  --region us-west-2
KUBERNETES_SETUP.md
