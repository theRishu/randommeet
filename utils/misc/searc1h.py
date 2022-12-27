from utils.misc import db_commands as db
from sqlalchemy import select
from utils.db_api.models import User
from utils.db_api.db import async_session

def create_indexes():
    # Create an index on the 'state' column
    stmt = CreateIndex(User.__table__.c.state)
    async with async_session() as session:
        await session.execute(stmt)
    print("Created index on 'state' column")

    # Create an index on the 'partner_id' column
    stmt = CreateIndex(User.__table__.c.partner_id)
    async with async_session() as session:
        await session.execute(stmt)
    print("Created index on 'partner_id' column")

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x[0] < pivot[0] or (x[0] == pivot[0] and x[1] < pivot[1])]
    middle = [x for x in arr if x[0] == pivot[0] and x[1] == pivot[1]]
    right = [x for x in arr if x[0] > pivot[0] or (x[0] == pivot[0] and x[1] > pivot[1])]
    return quicksort(left) + middle + quicksort(right)

async def find_match_user(user_id):
    current_user = await db.select_user(user_id)

    # Select eligible users from the database using a more efficient query
    stmt = select(User).where(User.state == "B" and User.partner_id == None)
    eligible_users = []
    async with async_session() as session:
        result = await session.execute(stmt)
        eligible_users = [await db.select_user(user.user_id) for user in result.scalars()]

    # Sort eligible users by VIP status and rating using quicksort
    eligible_users = quicksort(eligible_users, key=lambda x: (not x.is_vip, -x.rating))

    # Find the first eligible match
    for potential_partner in eligible_users:
        if current_user.gender == "M" and current_user.partner_gender == potential_partner.gender:
            return potential_partner.user_id
        elif current_user.gender == "F" and current_user.partner_gender == potential_partner.gender and current_user.is_vip:
            return potential_partner.user_id
        elif current_user.last_partner_id != potential_partner.user_id and current_user.user_id != potential_partner.user_id:
            return potential_partner.user_id
    
    # Return None if no match was found
    return None

