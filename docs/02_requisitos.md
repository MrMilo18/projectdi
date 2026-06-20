# Requisitos del sistema — ProyectaDi

## Descripción general

ProyectaDi será una plataforma colaborativa para gestionar proyectos, etapas, tareas, avances, presupuesto, evidencias, gráficas e informes automáticos.

El sistema estará orientado a equipos que necesitan dar seguimiento técnico, operativo y financiero a proyectos institucionales o estratégicos.

---

## Requisitos funcionales iniciales

| ID | Requisito | Prioridad | Criterio de aceptación |
|---|---|---|---|
| RF-001 | El sistema deberá permitir registrar usuarios. | Alta | Un usuario puede crear una cuenta con nombre, correo y contraseña. |
| RF-002 | El sistema deberá permitir iniciar sesión. | Alta | Un usuario registrado puede acceder con credenciales válidas. |
| RF-003 | El sistema deberá permitir crear proyectos. | Alta | Un usuario autorizado puede crear un proyecto con nombre, descripción, fechas y presupuesto inicial. |
| RF-004 | El sistema deberá permitir consultar proyectos asignados. | Alta | El usuario puede ver una lista de proyectos donde participa. |
| RF-005 | El sistema deberá permitir agregar miembros a un proyecto. | Alta | Un miembro queda vinculado al proyecto con un rol asignado. |
| RF-006 | El sistema deberá permitir crear etapas dentro de un proyecto. | Alta | Una etapa queda vinculada a un proyecto con fechas, presupuesto, peso y responsable. |
| RF-007 | El sistema deberá permitir crear tareas dentro de una etapa. | Alta | Una tarea queda vinculada a una etapa con responsable, fecha límite, estado, prioridad y peso. |
| RF-008 | El sistema deberá permitir registrar avances en tareas. | Alta | El avance queda guardado con usuario, fecha, descripción y porcentaje reportado. |
| RF-009 | El sistema deberá calcular el avance de una etapa. | Alta | El avance de la etapa se actualiza según el peso y avance de sus tareas. |
| RF-010 | El sistema deberá calcular el avance general de un proyecto. | Alta | El dashboard muestra el avance ponderado del proyecto. |
| RF-011 | El sistema deberá permitir registrar gastos. | Alta | Un gasto queda asociado a un proyecto o etapa y actualiza el presupuesto ejercido. |
| RF-012 | El sistema deberá mostrar indicadores básicos. | Media | El dashboard muestra avance, presupuesto, tareas atrasadas y actividad reciente. |
| RF-013 | El sistema deberá mostrar gráficas de avance y presupuesto. | Media | El usuario puede visualizar gráficas básicas del estado del proyecto. |
| RF-014 | El sistema deberá generar informes PDF básicos. | Alta | El usuario puede descargar un informe con resumen, avance, presupuesto y gráficas. |
| RF-015 | El sistema deberá permitir adjuntar evidencias. | Media | Los archivos quedan asociados a avances, tareas o proyectos. |
| RF-016 | El sistema deberá registrar historial de actividad. | Media | Los cambios relevantes conservan fecha, usuario, acción y entidad afectada. |

---

## Requisitos no funcionales iniciales

| ID | Requisito | Prioridad | Criterio de aceptación |
|---|---|---|---|
| RNF-001 | El sistema deberá ser intuitivo para usuarios no técnicos. | Alta | Un usuario nuevo puede crear y consultar proyectos siguiendo flujos simples. |
| RNF-002 | El sistema deberá funcionar en navegadores modernos. | Alta | La interfaz funciona en Chrome, Edge, Firefox y Safari recientes. |
| RNF-003 | El sistema deberá proteger contraseñas de forma segura. | Alta | No se almacenan contraseñas en texto plano. |
| RNF-004 | El sistema deberá validar permisos desde el backend. | Alta | Un usuario sin permisos no puede modificar recursos restringidos. |
| RNF-005 | El sistema deberá usar variables de entorno para credenciales. | Alta | Llaves, tokens y conexiones no quedan escritas directamente en el código. |
| RNF-006 | El sistema deberá mantener separación entre frontend, backend y base de datos. | Alta | Cada capa tiene su propia carpeta, configuración y responsabilidad. |
| RNF-007 | El sistema deberá permitir respaldos de base de datos. | Media | Existe un procedimiento documentado para respaldo y restauración. |
| RNF-008 | El sistema deberá ser escalable a múltiples proyectos y usuarios. | Media | La arquitectura permite agregar nuevas funciones sin reescribir el sistema completo. |
| RNF-009 | El sistema deberá conservar trazabilidad de cambios importantes. | Alta | Las actualizaciones críticas registran usuario, fecha y acción. |
| RNF-010 | El sistema deberá tener interfaz responsiva. | Media | Las pantallas principales son utilizables en escritorio, tablet y navegador móvil. |

---

## Roles iniciales

| Rol | Descripción | Permisos principales |
|---|---|---|
| Administrador | Usuario con control completo del sistema o de un proyecto. | Crear proyectos, editar información, invitar usuarios, asignar roles, eliminar elementos y generar informes. |
| Coordinador | Responsable operativo del seguimiento del proyecto. | Crear etapas, crear tareas, asignar responsables, revisar avances, registrar gastos y generar reportes. |
| Colaborador | Integrante responsable de actividades específicas. | Ver proyectos asignados, actualizar tareas, registrar avances, subir evidencias y comentar actividades. |
| Lector | Usuario con acceso de consulta. | Ver estado del proyecto, consultar avances autorizados y descargar informes permitidos. |

---

## Criterios de aceptación generales

La primera versión funcional deberá permitir que:

- un usuario pueda registrarse e iniciar sesión;
- un administrador pueda crear un proyecto;
- un proyecto pueda dividirse en etapas;
- cada etapa pueda contener tareas;
- los colaboradores puedan registrar avances;
- el sistema calcule avance por tarea, etapa y proyecto;
- el sistema registre presupuesto ejercido y restante;
- el dashboard muestre indicadores principales;
- el sistema genere un informe PDF básico;
- los roles impidan acciones no autorizadas;
- la información quede almacenada en base de datos.
