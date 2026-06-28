
# HYF Shop

A simple Spring Boot REST API built as an **in-class exercise** for Week 9 of the Backend Track.

---

## 🚀 Getting Started

### Prerequisites

- Java 25+
- Maven
- A running PostgreSQL instance

### Database Setup

Run the provided `database.sql` file against your PostgreSQL database to create and populate the schema:

```bash
psql -U <your_user> -d <your_database> -f database.sql
```

This will:
- Create the `products` table (if it doesn't already exist)
- Create a GIN index on the `details` column for efficient JSONB querying
- Insert **115 sample products** across 7 categories

### Configuration
The application reads its database connection from environment variables. Set the following before running:

| Variable | Description |
| --- | --- |
| `DB_URL` | JDBC connection URL (e.g. `jdbc:postgresql://localhost:5432/hyfshop`) |
| `DB_USERNAME` | PostgreSQL username |
| `DB_PASSWORD` | PostgreSQL password |

### Running the Application
``` bash
./mvnw spring-boot:run
```
The server starts on port 8080.

## 🛠️ Tech Stack
- **Java 25**
- **Spring Boot 4.1.0** (Spring Web MVC, Spring JDBC)
- **PostgreSQL** (via `JdbcClient`)
- **Lombok** (boilerplate reduction)