# Data Engineering Zoomcamp 2024 Notes Module 3

## Summary

## What is OLTP and OLAP?

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
