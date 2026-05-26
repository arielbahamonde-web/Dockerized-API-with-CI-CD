# API Dockerizada con CICD

Proyecto ejemplo: una API construida con FastAPI, preparada para ejecutarse con Docker y orquestada mediante `docker-compose`. Incluye pruebas básicas y está pensada para integrarse en un pipeline de CI/CD.

**Características**
- **Lenguaje:** Python 3
- **Framework:** FastAPI
- **Servidor ASGI:** Uvicorn
- **Contenedores:** Docker, Docker Compose
- **Tests:** pytest

**Requisitos**
- Docker y Docker Compose instalados localmente
- Python 3.8+ (para ejecución local)

**Instalación (local)**
```bash
# crear y activar entorno virtual
python3 -m venv .venv
source .venv/bin/activate

# instalar dependencias
pip install -r requirements.txt

# arrancar la API en desarrollo
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Ejecución con Docker (recomendado)**
```bash
docker-compose up --build
```

Después de levantar la aplicación, la API estará disponible en `http://localhost:8000`.

**Ejecutar tests**
```bash
pytest -q
```

**Endpoints principales**
- `GET /` : Mensaje de estado de la API
- `GET /health` : Estado de salud (returns {"status": "ok"})
- `GET /version` : Versión de la API
- `GET /users/` : Lista de usuarios de ejemplo (definido en `app/routes/users.py`)

**Estructura del proyecto**
- `Dockerfile` : Imagen de la aplicación
- `docker-compose.yml` : Orquestación de contenedores
- `requirements.txt` : Dependencias Python
- `app/` : Código fuente de la aplicación
  - `app/main.py` : Punto de entrada FastAPI
  - `app/routes/users.py` : Rutas de ejemplo para usuarios
- `tests/` : Pruebas (ej. `tests/test_health.py`)

**Buenas prácticas / CI**
- Añadir un workflow de CI (GitHub Actions, GitLab CI, etc.) que:
  - Construya la imagen Docker
  - Ejecute los tests con `pytest`
  - Publique artefactos o despliegue si los tests pasan

**Contribuciones**
- Abre un Issue antes de implementar cambios significativos.
- Envía un Pull Request con pruebas y descripciones claras.

**Licencia**
Este repositorio usa licencia MIT (añadir archivo `LICENSE` si procede).
