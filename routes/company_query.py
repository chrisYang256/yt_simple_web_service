import pymysql

from db_module import db


cursor = db.cursor(pymysql.cursors.DictCursor)

def select_company_to_check_exist(company_id):
    company = """
        select * 
        from company 
        where id=%s
    """
    cursor.execute(company, (company_id))
    company = cursor.fetchone()

    return company 

def select_company_list(limit, skip):
    compaies = """
        select * 
        from company 
        order by cdate DESC 
        limit %s offset %s
    """
    cursor.execute(compaies, (limit, skip))
    compaies = cursor.fetchall() # all/one 구분하기

    return compaies
    
def create_company(company_name, description):
    company_data = """
        insert into company(company_name, description) 
        values(%s, %s)
    """
    cursor.execute(company_data, (company_name, description))

def update_company(company_name, description, now_date, company_id):
    company_data = """
        update company 
        set company_name=%s, description=%s, udate=%s
        where id=%s
    """
    cursor.execute(company_data, 
        (company_name, description, now_date, company_id)
    )
    cursor.fetchall()

def delete_company(company_id):
    company_data = """
        delete from company 
        where id=%s
    """

    cursor.execute(company_data, (company_id))
    cursor.fetchall()