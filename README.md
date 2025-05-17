# Proyecto base Python puro

Proyecto base para practicar Git, GitHub Actions, pytest, CI/CD y Docker con Python puro.

## Estructura

- `app/main.py`: Código principal.
- `tests/test_main.py`: Pruebas con pytest.
- `.github/workflows/ci.yml`: Workflow GitHub Actions para correr tests.
- `Dockerfile` y `docker-compose.yml`: Contenedores para la app y pruebas.

## Comandos Docker

Ejecutar la app:

```bash
docker-compose run app
