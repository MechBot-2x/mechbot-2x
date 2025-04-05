```yaml
# Vault configuration (security/vault/config.hcl)
storage "raft" {
  path = "/vault/data"
  node_id = "mechbot_vault_1"
}@u32
```
