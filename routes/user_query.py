import pymysql

from db_module import db


cursor = db.cursor(pymysql.cursors.DictCursor)

def select_user_to_check_exist(user_id):
    user = """
                select * 
                from user 
                where id=%s
            """
    cursor.execute(user, (user_id))
    user = cursor.fetchone()

    return user 

def select_user_list(limit, skip):
    users = """
        select u.*, c.company_name
        from user as u
            inner join company as c 
            on c.id = u.company_id
        order by u.cdate DESC 
        limit %s offset %s
    """
    cursor.execute(users, (limit, skip))
    users = cursor.fetchall() # all/one 구분하기

    return users
    
# def create_company(company_name, description):
#     company_info = """
#         insert into company(company_name, description) 
#         values(%s, %s)
#     """
#     cursor.execute(company_info, (company_name, description))

# def update_company(company_name, description, now_date, company_id):
#     company_info = """
#             update company 
#             set company_name=%s, description=%s, udate=%s
#             where id=%s
#         """
#     cursor.execute(company_info, 
#         (company_name, description, now_date, company_id)
#     )
#     cursor.fetchall()

# def delete_company(company_id):
#     company_info = """
#             delete from company 
#             where id=%s
#         """

#     cursor.execute(company_info, (company_id))
#     cursor.fetchall()