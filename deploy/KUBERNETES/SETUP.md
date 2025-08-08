## **6. Deployment Guides**
📄 `deploy/KUBERNETES_SETUP.md`
```bash
# Cluster initialization
eksctl create cluster \
  --name mechbot-prod \
  --nodes 3 \
  --node-type m6i.2xlarge \
  --region us-west-2
```

📄 `deploy/EDGE_DEVICES.md`
```bash
# Flash Raspberry Pi image
sudo dd if=mechbot-edge-v2.1.img \
  of=/dev/mmcblk0 \
  bs=4M status=progress
```
