# Arquitectura técnica — ProyectaDi

## Descripción general

ProyectaDi será una plataforma colaborativa de gestión de proyectos compuesta por una interfaz web, una API backend, una base de datos relacional, almacenamiento de evidencias y un módulo de generación de reportes.

## Arquitectura propuesta

```text
[Cliente web / App escritorio]
        ↓
[Frontend React + TypeScript]
        ↓
[API Backend FastAPI]
        ↓
[PostgreSQL / Supabase]
        ↓
[Storage de archivos + Generador de reportes]
