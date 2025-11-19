# Car Finder – Oportunidades Automotivas

Este projeto faz buscas automáticas em portais automotivos (OLX, Webmotors, iCarros etc.) procurando anúncios particulares com margem de lucro acima de 12 a 15 mil reais em relação à Tabela FIPE.

O sistema funciona através de uma API deployada na Vercel e utiliza web scraping.

## Como funciona
- Busca anúncios particulares
- Compara preço do anúncio x FIPE
- Retorna somente oportunidades reais
- Atualiza automaticamente (auto-loop)
- Aceita consultas via browser

## Tecnologias
- Python
- Flask
- Requests
- BeautifulSoup4
- Vercel Serverless Functions
