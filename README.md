# WeatherPipeline

## Beskrivelse
WeatherPipeline er et Python-prosjekt som henter værdata fra [Frost API](https://frost.met.no) og lagrer det i en PostgreSQL-database. Prosjektet inkluderer funksjoner for å hente stasjoner, hente værdata, og lagre det i en strukturert database.  

Prosjektet viser hvordan man kan kombinere API-integrasjon, databaser og Python for å bygge en enkel datainnsamlingspipeline.

---

## Funksjonalitet
- Henter stasjoner i en valgt region (f.eks. Vestfold).  
- Henter værdata (temperatur, mm.) for alle stasjoner innenfor en periode.  
- Lagrer stasjoner og værdata i PostgreSQL-database.  
- Støtter `.env`-filer for å holde API-nøkler og databasepassord sikre.  
- Kan enkelt utvides til flere typer værdata eller regioner.

---
## Skjermbilde av hvordan man kan gjøre spørringer mot databasen
<img width="1710" height="740" alt="Skjermbilde 2025-09-24 151055" src="https://github.com/user-attachments/assets/8a0305c4-ed15-4b08-a2c8-6c8559508186" />
