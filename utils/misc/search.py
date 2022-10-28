from utils.misc import db_commands as db
from sqlalchemy import select
from utils.db_api.models import User
from utils.db_api.db import async_session


async def find_match_user(user_id):
    user = await db.select_user(user_id)
    stmt = select(User).where(User.state == "B" and User.partner_id == None)

    userlist = []
    async with async_session() as session:
        result = await session.execute(stmt)
        userlist = [user.user_id for user in result.scalars()]
        
        

    for match in userlist.reverse():
        match = await db.select_user(match)
        if user.gender == "M":
            if user.is_vip == True:
                if (
                    user.partner_gender == match.gender
                    and user.user_id != match.user_id
                    and user.last_partner_id != match.user_id
                ):
                    if match.partner_gender == user.gender:
                        return match.user_id

            else:
                if (
                    user.last_partner_id != match.user_id
                    and user.user_id != match.user_id
                ):
                    if match.partner_gender == "F" and match.is_vip == True:
                        pass
                    else:
                        return match.user_id

        if user.gender == "F":
            if user.is_vip == True:
                if (
                    user.partner_gender == match.gender
                    and user.user_id != match.user_id
                    and user.last_partner_id != match.user_id
                ):
                    return match.user_id
                else:
                    if (
                        user.user_id != match.user_id
                        and user.last_partner_id != match.user_id
                    ):
                        return match.user_id

            else:
                if (
                    user.user_id != match.user_id
                    and user.last_partner_id != match.user_id
                    and match.gender != "F"
                ):
                    return match.user_id

        else:
            if user.last_partner_id != match.user_id and user.user_id != match.user_id:
                if match.partner_gender != "NA" and match.is_vip == True:
                    pass

                else:
                    return match.user_id
