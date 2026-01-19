# CICDXBAUTISV
**Nombre:** Xavier Bautista 
**Caso:** Base Supertienda/Superstore de Tableau 

Repositorio GIT para el trabajo final de curso

# Trabajo Final – Ingeniería de Datos e IA con Databricks

## 📌 Descripción general
Este repositorio contiene el **trabajo final del curso "Ingeniería de Datos e IA con Databricks"**, cuyo objetivo es diseñar e implementar un flujo **end-to-end de datos** utilizando la plataforma Databricks bajo el enfoque **Lakehouse**, incorporando buenas prácticas de **ETL, CI/CD, seguridad, gobierno de datos y visualización**.

El proyecto abarca desde la preparación del ambiente y la ingesta de múltiples fuentes de datos, hasta la transformación, carga de información analítica y su consumo mediante dashboards.

---

## 📂 Estructura del directorio

```
CICDXBAUTISV/
├── .github/
│   └── workspaces/
│       └── deploy_desa_to_prod.yml
│
├── certificaciones/
│   ├── Acreditacion_Databricks.jpg
│   └── Certificado_Databricks_Fundamentals.pdf
│
├── dashboards/
│   ├── Gold_Orden_Compra_Sectorizada.pdf
│   ├── Gold_Orden_Compra_Sectorizada.pbix
│   └── WF_Ordenes_Sectorizadas_OK.jpg
│
├── proceso/
│   └── ETL_XBAUTISV/
│       ├── 01_XBAUTISV_Preparacion_Ambiente.py
│       ├── 02_XBAUTISV_Ingesta_Compras.py
│       ├── 03_XBAUTISV_Ingesta_Devoluciones.py
│       ├── 04_XBAUTISV_Ingesta_Personas.py
│       ├── 05_XBAUTISV_Ingesta_Productos.py
│       ├── 06_XBAUTISV_Ingesta_Clientes.py
│       ├── 07_XBAUTISV_Transformacion.ipynb
│       └── 08_XBAUTISV_Carga_Informacion.ipynb
│
├── reversion/
│   └── 01_XBAUTISV_Preparacion_Ambiente.py
│
└── seguridad/
    └── 09_XBAUTISV_Habilitacion_Accesos.py
```

---

## 🔄 CI/CD
**Ruta:** `.github/workspaces/deploy_desa_to_prod.yml`

Archivo de configuración para automatizar el despliegue de artefactos desde un entorno de desarrollo hacia producción, aplicando prácticas de **CI/CD en Databricks** mediante GitHub Actions.

---

## 🏅 Certificaciones
**Ruta:** `certificaciones/`

Contiene respaldos de acreditaciones obtenidas durante la formación:
- Certificación Databricks Fundamentals
- Evidencia de acreditación académica

---

## 📊 Dashboards y visualización
**Ruta:** `dashboards/`

Incluye los artefactos de consumo analítico generados a partir de la capa **Gold**:
- Dashboard de órdenes de compra sectorizadas (PDF)
- Archivo Power BI (`.pbix`) para análisis interactivo
- Evidencia gráfica del workflow ejecutado en Databricks

---

## ⚙️ Proceso ETL
**Ruta:** `proceso/ETL_XBAUTISV/`

Pipeline ETL implementado en Databricks siguiendo una secuencia lógica:

1. **Preparación del ambiente**  
   Configuración inicial del entorno, variables, catálogos y esquemas.

2. **Ingesta de datos**  
   Scripts independientes para la carga de:
   - Compras
   - Devoluciones
   - Personas
   - Productos
   - Clientes

3. **Transformación**  
   Notebook encargado de aplicar reglas de negocio, normalización, enriquecimiento y consolidación de datos.

4. **Carga de información**  
   Publicación de datos transformados en tablas analíticas listas para consumo (capa Gold).

---

## 🔐 Seguridad y gobierno de datos
**Ruta:** `seguridad/`

Script para la **habilitación de accesos y permisos**, aplicando principios de gobierno de datos en Databricks y Unity Catalog (roles, grupos y privilegios).

---

## ♻️ Reversión
**Ruta:** `reversion/`

Scripts de respaldo que permiten revertir configuraciones críticas del ambiente en caso de errores o reprocesos.

---

## 🛠️ Tecnologías utilizadas
- Databricks Lakehouse Platform
- Apache Spark / PySpark
- Delta Lake
- Unity Catalog
- GitHub Actions (CI/CD)
- Power BI

---

## 🎓 Contexto académico
Proyecto desarrollado como **trabajo final del curso "Ingeniería de Datos e IA con Databricks"**, demostrando competencias en:
- Arquitectura Lakehouse
- Ingeniería de datos
- Automatización y despliegue
- Seguridad y gobierno de datos
- Analítica y visualización
