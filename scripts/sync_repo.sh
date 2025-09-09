#!/bin/bash
# Script para sincronizar repositorio sin perder archivos

echo "🔄 Sincronizando repositorio..."

# Backup de cambios locales
BACKUP_DIR="../mechbot-backup-$(date +%Y%m%d_%H%M%S)"
echo "📦 Creando backup en: $BACKUP_DIR"
cp -r . "$BACKUP_DIR"

# Stash de cambios locales
echo "💾 Guardando cambios locales en stash..."
git stash push -m "backup_$(date +%Y%m%d_%H%M%S)"

# Obtener últimos cambios
echo "⬇️  Obteniendo cambios del repositorio..."
git fetch origin

# Verificar estado
echo "📊 Estado actual:"
git status

# Hacer pull con rebase para evitar merges automáticos
echo "🔀 Aplicando cambios..."
git pull --rebase origin main

# Si hay conflictos, ayudar a resolver
if grep -q "conflict" <<< $(git status); then
    echo "⚠️  Hay conflictos que resolver:"
    git status
    echo "Por favor resuelve los conflictos manualmente y luego ejecuta:"
    echo "git rebase --continue"
    exit 1
fi

# Restaurar cambios locales si se desea
read -p "¿Restaurar cambios locales del stash? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    git stash pop
    echo "✅ Cambios locales restaurados"
else
    echo "ℹ️  Cambios locales mantenidos en stash. Usa 'git stash pop' para restaurar."
fi

echo "🎉 Sincronización completada!"
