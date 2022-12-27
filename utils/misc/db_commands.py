from sqlalchemy import update, select
from sqlalchemy.sql.expression import delete


from utils.db_api.models import User
from utils.db_api.db import async_session


async def add_user(user_id):
    stmt = select(User).where(User.user_id == user_id)
    async with async_session() as session:
        request = await session.execute(stmt)
        user = request.scalar()
        if not user:
            user = User(user_id=user_id)
            session.add(user)
            await session.commit()
            await session.close()
        else:
            pass


async def update_state(user_id, state_data):
    stmt = update(User).where(User.user_id == user_id).values(state=state_data)
    async with async_session() as session:
        await session.execute(stmt)
        await session.commit()
        await session.close()

async def allow_mperm(user_id):
    stmt = update(User).where(User.user_id == user_id).values(mperm=True)
    async with async_session() as session:
        await session.execute(stmt)
        await session.commit()
        await session.close()

async def disallow_mperm(user_id):

    stmt = update(User).where(User.user_id == user_id).values(mperm=False)
    async with async_session() as session:
        await session.execute(stmt)
        await session.commit()
        await session.close()



async def update_total_referral(code):
    try:
        stmt = (
            update(User)
            .where(User.user_id == code)
            .values(rating=User.rating + 20, total_referral=User.total_referral + 1)
        )
        async with async_session() as session:
            await session.execute(stmt)
            await session.commit()
            await session.close()
    except Exception as e:
        print(str(e))


async def update_after_leavechat(user_id, partner_id):
    stmt1 = (
        update(User)
        .where(User.user_id == user_id)
        .values(partner_id=None, state="A", last_partner_id=partner_id , mperm=False)
    )
    stmt2 = (
        update(User)
        .where(User.user_id == partner_id)
        .values(partner_id=None, state="A", last_partner_id=user_id,mperm=False)
    )
    print(f"{user_id} && {partner_id} left the chat.")
    async with async_session() as session:
        await session.execute(stmt1)
        await session.execute(stmt2)
        await session.commit()
        await session.close()


async def update_after_anotherchat(user_id, partner_id):
    stmt1 = (
        update(User)
        .where(User.user_id == user_id)
        .values(partner_id=None, state="B", last_partner_id=partner_id)
    )

    stmt2 = (
        update(User)
        .where(User.user_id == partner_id)
        .values(partner_id=None, state="A", last_partner_id=user_id)
    )
    print(f"{user_id} left the chat.")
    async with async_session() as session:
        await session.execute(stmt1)
        await session.execute(stmt2)
        await session.commit()
        await session.close()


async def delete_user(user_id):
    try:
        stmt = delete(User).where(User.user_id == user_id)
        async with async_session() as session:
            await session.execute(stmt)
            await session.commit()
            await session.close()
    except Exception as e:
        print(str(e))


async def select_user(user_id):
    async with async_session() as session:
        result = await session.execute(select(User).where(User.user_id == user_id))
        return result.scalars().first()


async def update_after_match(user_id, found_match):

    stmt1 = (
        update(User)
        .where(User.user_id == user_id)
        .values(partner_id=found_match, state="C")
    )
    stmt2 = (
        update(User)
        .where(User.user_id == found_match)
        .values(partner_id=user_id, state="C")
    )

    async with async_session() as session:
        await session.execute(stmt2)
        await session.execute(stmt1)
        await session.commit()
        await session.close()


async def update_partner_id(user_id, id):
    stmt = (
        update(User)
        .where(User.user_id == user_id)
        .values(partner_id=id)
        .returning(User.state)
    )

    async with async_session() as session:
        await session.execute(stmt)
        await session.commit()
        await session.close()


async def update_gender(user_id, gender_data):
    stmt = (
        update(User).where(User.user_id == user_id).values({User.gender: gender_data})
    )
    async with async_session() as session:

        await session.execute(stmt)
        await session.commit()
        await session.close()


async def update_ro_id(user_id, ro_id_data):
    stmt = update(User).where(User.user_id == user_id).values({User.ro_id: ro_id_data})
    async with async_session() as session:

        await session.execute(stmt)
        await session.commit()
        await session.close()


async def update_partner_gender(user_id, partner_gender_data):
    stmt = (
        update(User)
        .where(User.user_id == user_id)
        .values({User.partner_gender: partner_gender_data})
    )
    async with async_session() as session:

        await session.execute(stmt)
        await session.commit()
        await session.close()


"""
async def update_after_leavechat(user_id, partner_id):

    stmt = (
        update(User)
        .where(User.user_id == user_id)
        .values(partner_id=None, state="A", last_partner_id=partner_id)
    )
    print(f"{user_id} left the chat.")
    async with async_session() as session:
        await session.execute(stmt)
        await session.commit()
        await session.close()

"""


async def kick_user_from_match_queue(user_id):

    stmt = (
        update(User)
        .where(User.user_id == user_id)
        .values(state="A")
        .returning(User.is_vip)
    )

    async with async_session() as session:
        await session.execute(stmt)
        await session.commit()
        await session.close()


async def makevip(user_id):
    stmt = update(User).where(User.user_id == user_id).values(is_vip=True , rating =60)
    async with async_session() as session:
        await session.execute(stmt)
        await session.commit()
        await session.close()


async def update_rate_by_admin(user_id, rate):
    stmt = update(User).where(User.user_id == user_id).values(rating=rate)

    async with async_session() as session:
        await session.execute(stmt)
        await session.commit()
        await session.close()
        
        
        
        
async def revokvips(user_id ):
    stmt = (
        update(User)
        .where(User.user_id == user_id)
        .values(partner_gender='NA',total_referral= 0 ,  rating =0 , is_vip = False)
        .returning(User.is_vip)
    )
    async with async_session() as session:
        await session.execute(stmt)
        await session.commit()
        await session.close()

