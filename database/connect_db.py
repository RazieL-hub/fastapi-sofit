from databases import Database

database = Database('postgresql+asyncpg://postgres:postgres@localhost/postgres')
await database.connect()


