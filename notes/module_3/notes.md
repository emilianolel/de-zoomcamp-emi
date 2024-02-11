# Data Engineering Zoomcamp 2024 Notes Module 3

## Summary

## What is OLTP and OLAP?

![olap and oltp](../../assets/module_3/notes/olap_oltp.webp)

OLAP (Online Analytical Processing) and OLTP (Online Transactional Processing) are two different types of database systems, each optimized for distinct purposes.

1. **OLTP (Online Transactional Processing)**:
   - **Purpose**: OLTP systems are designed for managing transaction-oriented applications, where the emphasis is on processing a large number of short, online transactions (e.g., `INSERT`, `UPDATE`, `DELETE`).
   - **Characteristics**:
     - **High Volume**: Handles a large number of concurrent transactions. 📈
     - **Low Latency**: Prioritizes quick response times for individual transactions. ⏱️
     - **Normalized Schema**: Typically employs a highly normalized database schema to minimize redundancy and maintain data integrity. 🔍
     - **Example**: Online banking systems, e-commerce platforms, airline reservation systems. 💳 🛒 ✈️

2. **OLAP (Online Analytical Processing)**:
   - **Purpose**: OLAP systems are geared towards analytical and decision-support applications, where the focus is on complex queries involving aggregations, calculations, and historical data analysis.
   - **Characteristics**:
     - **Complex Queries**: Supports complex analytical queries involving aggregations, roll-ups, and drill-downs. 📊
     - **Read-Heavy**: Primarily optimized for read operations rather than write operations. 📚
     - **Denormalized Schema**: Often uses a denormalized or star/snowflake schema to optimize query performance. ❄️
     - **Example**: Business intelligence tools, reporting systems, data warehouses. 📈 📊 🏢

In summary, OLTP systems prioritize efficient transaction processing for day-to-day operations, while OLAP systems are tailored for analytical processing and decision support, enabling users to gain insights from large volumes of historical data. 🔄🧠

|                     | OLTP 💼                                                                                           | OLAP 🔍                                                                           |
| ------------------- | ------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Purpose             | Control and run essential business operations in real time                                        | Plan, solve problems, support decisions, discover hidden insights                 |
| Data updates        | Short, fast updates initiated by user                                                             | Data periodically refreshed with scheduled, long-running batch jobs               |
| Database design     | Normalized databases for efficiency                                                               | Denormalized databases for analysis                                               |
| Space requirements  | Generally small if historical data is archived                                                    | Generally large due to aggregating large datasets                                 |
| Backup and recovery | Regular backups required to ensure business continuity and meet legal and governance requirements | Lost data can be reloaded from OLTP database as needed in lieu of regular backups |
| Productivity        | Increases productivity of end users                                                               | Increases productivity of business managers, data analysts, and executives        |
| Data view           | Lists day-to-day business transactions                                                            | Multi-dimensional view of enterprise data                                         |
| User examples       | Customer-facing personnel, clerks, online shoppers                                                | Knowledge workers such as data analysts, business analysts, and executives        |

## What is a Data Warehouse? 🏢

![data warehouse](../../assets/module_3/notes/data-warehouse.png)

A data warehouse is a centralized repository that stores structured, historical data from one or more sources. It's designed to facilitate reporting, analysis, and data mining (OLAP solution).

1. **Purpose**: The primary purpose of a data warehouse is to provide a unified view of an organization's data, enabling decision-makers to analyze trends, patterns, and relationships across different aspects of the business. 📊

2. **Components**: A data warehouse typically includes components such as:
   - ETL (Extract, Transform, Load) processes to extract data from source systems, transform it into a consistent format, and load it into the warehouse.
   - Data marts, which are subsets of the data warehouse focused on specific business functions or departments.
   - OLAP (Online Analytical Processing) cubes for multidimensional analysis.
   - Metadata repositories for storing information about the data warehouse's structure and content. 🔄

3. **Benefits**: Data warehouses offer several benefits, including:
   - Improved decision-making: By providing access to integrated, high-quality data, data warehouses empower users to make more informed decisions.
   - Data consistency: Data warehouses enforce consistent naming conventions, definitions, and formats, ensuring that users can trust the accuracy and reliability of the data.
   - Scalability: Data warehouses are designed to handle large volumes of data and support complex analytical queries, making them suitable for organizations of all sizes. 📈

Overall, a data warehouse serves as a foundational component of a business intelligence and analytics infrastructure, enabling organizations to unlock the value of their data and gain insights that drive strategic decision-making. 🚀
