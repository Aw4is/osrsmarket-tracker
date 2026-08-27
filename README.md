# OSRS Market Tracker

> **Currently in development**

A full-stack Old School RuneScape Grand Exchange market tracking application for exploring item prices, historical market data, and market trends.

The project is being built as a full-stack application with a Python/FastAPI backend and a React frontend.

## Planned Features

- Browse and search Grand Exchange items
- View current high and low prices
- Track historical item prices and trading volume
- Interactive price and volume charts
- Item watchlists
- User accounts and authentication
- Track favourite items
- Market trend and price-change analysis
- Price alerts
- Portfolio / profit tracking
- Market data ingestion from OSRS APIs
- Caching for frequently accessed market data

## Tech Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- Pydantic
- PostgreSQL
- Alembic
- psycopg

### Frontend
- React
- TypeScript
- *Additional frontend tooling to be decided*

### Infrastructure
- Docker / Docker Compose
- Redis *(planned)*

## Current Progress

- [x] FastAPI project setup
- [x] PostgreSQL development database with Docker
- [x] Environment-based application configuration
- [ ] SQLAlchemy database configuration
- [ ] Item model and API
- [ ] Price history model and API
- [ ] OSRS market data ingestion
- [ ] Frontend
- [ ] Authentication
- [ ] Watchlists and user features

## Architecture

The application is being developed as a separate frontend and backend:

React / TypeScript
        ↓
     FastAPI
        ↓
     Services
        ↓
    SQLAlchemy
        ↓
    PostgreSQL

External OSRS market data will be ingested and stored to support historical price tracking and analytics.
