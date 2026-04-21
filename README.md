# DevOps CI/CD Final

Aplicación web desplegada con pipeline CI/CD completo.

## Tecnologías
- Python + Flask (app web)
- Pytest (pruebas unitarias)
- Docker (contenedor)
- GitHub Actions (CI/CD)
- Docker Hub (registro de imagen)
- Render (producción)

## Pipeline CI/CD
Al hacer push a main se ejecuta automáticamente:
1. Instala dependencias
2. Ejecuta pruebas unitarias con pytest
3. Construye y sube imagen a Docker Hub
4. Despliega en producción

## URLs
- App en producción: https://devops-cicd-final.onrender.com
- Imagen Docker Hub: https://hub.docker.com/r/jhoanmceron/devops-cicd-final
