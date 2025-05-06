# 🏦 Proyecto de Aplicación microservicios - "Riesgo Financiero"

Este proyecto es un sistema de microservicios construido con **FastAPI**, diseñado para simular una plataforma financiera, donde se registran transacciones, y el sistema valida e intercomunica entre servicios y mediante el entrenamiento de un modelo, decida si es una transacción con riesgo de fraude. El objetivo es construir una arquitectura robusta que escale a un ecosistema de eventos con **Kafka**, **observabilidad**, y buenas prácticas de desarrollo moderno.

## 🚧 En desarrollo...

Actualmente, el sistema cuenta con:

- 📦 `user-service`: Microservicio que maneja la creación, listado y gestión de usuarios.
- 💸 `transaction-service`: Microservicio que registra transacciones y valida la existencia del usuario en `user-service`.
- 🐳 Dockerizado con `Docker` y `Docker Compose`.
- 🔗 Comunicación entre microservicios mediante HTTP asíncrono (`httpx`).
- 📄 Validaciones y esquemas con `Pydantic`.
- 🧪 Pruebas funcionales usando Swagger UI.
- ⚙️ Preparado para escalar con Kafka, Prometheus y Grafana.

---

## 🔧 Tecnologías utilizadas
- Python 3.9+
- FastAPI
- SQLAlchemy (async)
- PostgreSQL
- Docker & Docker Compose
- httpx
- Pydantic

---

## 🛣️ Roadmap
- ✅ Crear servicios de usuarios y transacciones
- ✅ Validar usuarios entre microservicios vía HTTP
- ✅ Dockerizar cada microservicio
- Integrar Kafka para eventos distribuidos
- Agregar métricas con Prometheus + Grafana
- Autenticación y autorización
- CI/CD con GitHub Actions
- Despliegue en nube (Azure / AWS)