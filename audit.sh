#!/bin/bash
# En audit.sh
check_ssl() {
  openssl s_client -connect $1:443 | grep "TLSv1.3"
}
check_db_encryption() {
  psql -c "SHOW ssl;" | grep "on"
}
