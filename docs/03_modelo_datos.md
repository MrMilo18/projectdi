# Modelo de datos inicial — ProyectaDi

## Descripción general

El modelo de datos inicial de ProyectaDi se basa en una estructura relacional. La base de datos principal será PostgreSQL, ya sea administrada directamente o mediante Supabase.

El objetivo del modelo es representar usuarios, proyectos, miembros, etapas, tareas, avances, gastos, evidencias, comentarios, reportes e historial de actividad.

---

## Entidades principales

### 1. users

Registra las cuentas de usuario del sistema.

| Campo | Tipo sugerido | Descripción |
|---|---|---|
| id | UUID | Identificador único del usuario. |
| name | VARCHAR | Nombre completo del usuario. |
| email | VARCHAR | Correo electrónico único. |
| password_hash | VARCHAR | Contraseña cifrada. |
| status | VARCHAR | Estado de la cuenta: active, inactive, suspended. |
| created_at | TIMESTAMP | Fecha de creación. |
| updated_at | TIMESTAMP | Fecha de última actualización. |

---

### 2. projects

Registra los proyectos principales.

| Campo | Tipo sugerido | Descripción |
|---|---|---|
| id | UUID | Identificador único del proyecto. |
| name | VARCHAR | Nombre del proyecto. |
| description | TEXT | Descripción general. |
| start_date | DATE | Fecha de inicio. |
| end_date | DATE | Fecha estimada de término. |
| total_budget | NUMERIC | Presupuesto total del proyecto. |
| status | VARCHAR | Estado: planning, active, paused, completed, archived. |
| progress_percentage | NUMERIC | Avance general calculado. |
| created_by | UUID | Usuario que creó el proyecto. |
| created_at | TIMESTAMP | Fecha de creación. |
| updated_at | TIMESTAMP | Fecha de última actualización. |

---

### 3. project_members

Relaciona usuarios con proyectos y roles.

| Campo | Tipo sugerido | Descripción |
|---|---|---|
| id | UUID | Identificador único del registro. |
| project_id | UUID | Proyecto relacionado. |
| user_id | UUID | Usuario relacionado. |
| role | VARCHAR | Rol del usuario dentro del proyecto. |
| joined_at | TIMESTAMP | Fecha de incorporación. |

Roles permitidos inicialmente:

- admin
- coordinator
- collaborator
- reader

---

### 4. stages

Registra etapas o fases dentro de un proyecto.

| Campo | Tipo sugerido | Descripción |
|---|---|---|
| id | UUID | Identificador único de la etapa. |
| project_id | UUID | Proyecto al que pertenece. |
| name | VARCHAR | Nombre de la etapa. |
| description | TEXT | Descripción de la etapa. |
| start_date | DATE | Fecha de inicio. |
| end_date | DATE | Fecha de término. |
| budget_assigned | NUMERIC | Presupuesto asignado a la etapa. |
| weight | NUMERIC | Peso relativo de la etapa dentro del proyecto. |
| progress_percentage | NUMERIC | Avance calculado de la etapa. |
| status | VARCHAR | Estado de la etapa. |
| created_at | TIMESTAMP | Fecha de creación. |
| updated_at | TIMESTAMP | Fecha de última actualización. |

---

### 5. tasks

Registra tareas dentro de una etapa.

| Campo | Tipo sugerido | Descripción |
|---|---|---|
| id | UUID | Identificador único de la tarea. |
| stage_id | UUID | Etapa a la que pertenece. |
| title | VARCHAR | Título de la tarea. |
| description | TEXT | Descripción de la tarea. |
| assigned_to | UUID | Usuario responsable. |
| due_date | DATE | Fecha límite. |
| priority | VARCHAR | Prioridad: low, medium, high, urgent. |
| status | VARCHAR | Estado: pending, in_progress, completed, blocked. |
| weight | NUMERIC | Peso relativo de la tarea dentro de la etapa. |
| progress_percentage | NUMERIC | Avance de la tarea. |
| created_at | TIMESTAMP | Fecha de creación. |
| updated_at | TIMESTAMP | Fecha de última actualización. |

---

### 6. progress_updates

Registra bitácoras de avance.

| Campo | Tipo sugerido | Descripción |
|---|---|---|
| id | UUID | Identificador único del avance. |
| task_id | UUID | Tarea relacionada. |
| user_id | UUID | Usuario que registró el avance. |
| description | TEXT | Descripción del avance. |
| progress_value | NUMERIC | Porcentaje reportado. |
| created_at | TIMESTAMP | Fecha de registro. |

---

### 7. expenses

Registra gastos asociados a proyectos o etapas.

| Campo | Tipo sugerido | Descripción |
|---|---|---|
| id | UUID | Identificador único del gasto. |
| project_id | UUID | Proyecto relacionado. |
| stage_id | UUID | Etapa relacionada, si aplica. |
| category | VARCHAR | Categoría del gasto. |
| amount | NUMERIC | Monto del gasto. |
| description | TEXT | Descripción. |
| expense_date | DATE | Fecha del gasto. |
| created_by | UUID | Usuario que registró el gasto. |
| created_at | TIMESTAMP | Fecha de registro. |

---

### 8. files

Registra metadatos de evidencias y documentos.

| Campo | Tipo sugerido | Descripción |
|---|---|---|
| id | UUID | Identificador único del archivo. |
| owner_type | VARCHAR | Tipo de entidad asociada: project, stage, task, progress_update, expense, report. |
| owner_id | UUID | Identificador de la entidad asociada. |
| filename | VARCHAR | Nombre del archivo. |
| file_url | TEXT | URL o ruta de almacenamiento. |
| mime_type | VARCHAR | Tipo de archivo. |
| uploaded_by | UUID | Usuario que subió el archivo. |
| uploaded_at | TIMESTAMP | Fecha de carga. |

---

### 9. comments

Registra comentarios asociados a tareas, avances u otras entidades.

| Campo | Tipo sugerido | Descripción |
|---|---|---|
| id | UUID | Identificador único del comentario. |
| owner_type | VARCHAR | Tipo de entidad comentada. |
| owner_id | UUID | Identificador de la entidad comentada. |
| user_id | UUID | Usuario que comentó. |
| comment | TEXT | Contenido del comentario. |
| created_at | TIMESTAMP | Fecha de creación. |

---

### 10. reports

Registra informes generados.

| Campo | Tipo sugerido | Descripción |
|---|---|---|
| id | UUID | Identificador único del reporte. |
| project_id | UUID | Proyecto relacionado. |
| report_type | VARCHAR | Tipo: weekly, monthly, executive, financial, final. |
| file_url | TEXT | Ruta o URL del PDF generado. |
| generated_by | UUID | Usuario que generó el reporte. |
| generated_at | TIMESTAMP | Fecha de generación. |

---

### 11. activity_log

Registra cambios relevantes para auditoría.

| Campo | Tipo sugerido | Descripción |
|---|---|---|
| id | UUID | Identificador único del evento. |
| user_id | UUID | Usuario que realizó la acción. |
| project_id | UUID | Proyecto relacionado. |
| action | VARCHAR | Acción realizada. |
| entity_type | VARCHAR | Tipo de entidad afectada. |
| entity_id | UUID | Identificador de la entidad afectada. |
| created_at | TIMESTAMP | Fecha del evento. |

---

## Relaciones principales

- Un usuario puede pertenecer a muchos proyectos.
- Un proyecto puede tener muchos miembros.
- Un proyecto puede contener muchas etapas.
- Una etapa puede contener muchas tareas.
- Una tarea puede tener múltiples avances.
- Un proyecto puede tener múltiples gastos.
- Las tareas, avances, gastos y reportes pueden tener archivos asociados.
- Las tareas y avances pueden tener comentarios.
- Los cambios relevantes se registran en `activity_log`.

---

## Reglas iniciales de negocio

### Avance de tareas

Cada tarea tendrá un porcentaje de avance entre 0 y 100.

### Avance de etapas

El avance de una etapa se calculará mediante la suma ponderada de sus tareas:

```text
avance_etapa = Σ(avance_tarea_i × peso_tarea_i)
