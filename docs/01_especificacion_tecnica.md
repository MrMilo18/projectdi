# Especificación técnica resumida — ProyectaDi

## 1. Descripción general

ProyectaDi es una plataforma colaborativa de gestión de proyectos orientada a la planeación, seguimiento técnico, control presupuestal, registro de avances, generación de indicadores visuales e informes automáticos.

El sistema permitirá que equipos institucionales u organizacionales administren proyectos mediante etapas, tareas, responsables, cronogramas, presupuesto, evidencias y reportes descargables.

---

## 2. Objetivo general

Desarrollar una plataforma intuitiva, colaborativa y escalable que permita organizar, monitorear y reportar el avance técnico, operativo y financiero de proyectos mediante cronogramas, etapas, tareas, presupuesto, evidencias, gráficas e informes automáticos.

---

## 3. Alcance inicial

La primera versión funcional del sistema deberá incluir:

- registro e inicio de sesión de usuarios;
- creación y consulta de proyectos;
- gestión de miembros por proyecto;
- creación de etapas;
- creación de tareas;
- registro de avances;
- cálculo automático de avance por tarea, etapa y proyecto;
- registro de presupuesto y gastos;
- dashboard con indicadores básicos;
- gráficas de avance y presupuesto;
- generación de informe PDF básico;
- documentación técnica inicial.

---

## 4. Elementos fuera del alcance inicial

Para mantener un MVP realista, quedan fuera de la primera versión:

- aplicación móvil nativa;
- chat interno avanzado;
- inteligencia artificial predictiva;
- facturación o contabilidad fiscal completa;
- integraciones bancarias;
- firma electrónica avanzada;
- modo offline completo;
- nómina o recursos humanos;
- aplicación de escritorio completa con Tauri.

Estos elementos podrán evaluarse después de validar el flujo principal del sistema.

---

## 5. Arquitectura general

```text
[Cliente web / App de escritorio futura]
        ↓
[Frontend React + TypeScript]
        ↓
[API Backend FastAPI]
        ↓
[PostgreSQL / Supabase]
        ↓
[Storage de archivos + Generador de reportes]
