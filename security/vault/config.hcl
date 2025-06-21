storage "raft" { path = "/vault/data" node_id = "mechbot_vault_1" }

listener "tcp" { tls_cert_file = "/etc/certs/vault.crt" tls_key_file = "/etc/certs/vault.key" }

Implementation Command:

Initialize Vault
vault operator init -key-shares=5 -key-threshold=3
