#!/bin/bash
# Rotación mensual de JWT secrets
vault kv put secret/mechbot/jwt \
  secret=$(openssl rand -hex 64) \
  expiration="30d"

# Reinicio controlado de servicios
kubectl rollout restart deployment/mechbot-api
