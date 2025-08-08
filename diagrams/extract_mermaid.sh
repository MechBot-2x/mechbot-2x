#!/bin/bash
# Extrae código Mermaid de archivos .md sin modificarlos

find docs/ -name "*.md" -type f | while read -r file; do
    echo "Procesando: $file"
    awk '
    BEGIN { in_mermaid=0; count=0 }
    /```mermaid/ { in_mermaid=1; count++; next }
    /```/ && in_mermaid { in_mermaid=0; next }
    in_mermaid { 
        gsub(/^[ \t]+/, "", $0);  # Elimina indentación
        print > "diagrams/mermaid/" basename "_" count ".mmd"
    }
    ' basename="$(basename "$file" .md)" "$file"
done

echo "Extracción completada. Diagramas guardados en diagrams/mermaid/"
