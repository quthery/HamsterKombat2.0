
from sqlalchemy import update
from app.database import new_session, PetyaORM

class MangaRepository:
    @classmethod
    async def add_one(cls, id: int, first_name: str, last_name: str, full_name: str) -> int:
        try:
            async with new_session() as session:
                manga = PetyaORM(id=id, first_name=first_name, last_name=last_name, full_name=full_name)
                session.add(manga)
                await session.flush()
                await session.commit()
                return manga.id
        except:
            return "s"
            
    @classmethod
    async def add_coins(cls, id: int) -> None:
        async with new_session() as session:
            query = update(PetyaORM).where(PetyaORM.id == id).values(coins=PetyaORM.coins + 1)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def get_total_coins(cls, id: int) -> int:
        async with new_session() as session:
            manga = await session.get(PetyaORM, id)
            return manga.coins if manga else 0
        
    @classmethod
    async def get_stats(cls, id: int) -> int:
        async with new_session() as session:
            manga = await session.get(PetyaORM, id)
            return manga

# Пример использования:
async def main():
    user_id = 1  # Здесь укажи нужный ID пользователя
    total_coins = await MangaRepository.get_total_coins(id=user_id)
    print(f"Общее количество монет у пользователя с ID {user_id}: {total_coins}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())


# Пример использования:
async def main():
    manga_id = await MangaRepository.add_one(id=2, first_name="s", last_name="as", full_name="s")
    print(f"Добавлена манга с ID {manga_id}")
    await MangaRepository.add_coins(id=1)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
