
from MyDataBase import MyDatabase
from Constants import Constants

class CRUD:
    const = Constants()
    conn = MyDatabase(
            const.decrypt(Constants.e_host),
            int(const.decrypt(Constants.e_port)),
            const.decrypt(Constants.e_database),
            const.decrypt(Constants.e_user),
            const.decrypt(Constants.e_password)
        )
    
    def create_profile(self):

        sql  = '''CREATE TABLE Profile (
        idx int NOT NUL PRIMARY KEY,
          name varchar(50) NOT NULL,
            alias varchar(50) NOT NULL,
              token varchar(50) NOT NULL,
                birthdate DATE NOT NULL,
                  email varchar(50) NOT NULL,
                    lang_code varchar(50) NOT NULL,
                      `routine` varchar(50) NOT NULL,
                        alarm int NOT NULL,
                          inactivity_time TIME NOT NULL,
                          inactivity_type TIME NOT NULL,
                          )'''
        result = self.conn.query(sql)
        print(result)  

    def get_profile(self):
        sql = "SELECT idx, name, alias, token, birthdate, email, lang_code, `routine`, alarm, inactivity_time, inactivity_type" \
        " FROM defaultdb.Profiles;"
        result = self.conn.query(sql) 
        print(result)

    def set_profile(self, idx, name, alias, token, birthdate, email, lang_code, routine, alarm, inactivity_time, inactivity_type):
        sql = "INSERT INTO defaultdb.Profiles " \
        "(idx, name, alias, token, birthdate, email, lang_code, `routine`, alarm, inactivity_time, inactivity_type) " \
        "VALUES ({}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', '{}');".format(
            idx, name, alias, token, birthdate, email, lang_code, routine, alarm, inactivity_time, inactivity_type
            )
        print(sql)
        result = self.conn.query(sql) 
        print(result)

    def update_profile(self, name, alias, token, birthdate, email, lang_code, routine, alarm, inactivity_time, inactivity_type, idx):
        sql = "UPDATE defaultdb.profiles " \
        "SET name='{}', alias='{}', token='{}', birthdate={}, email='{}', lang_code='{}', `routine`={}, alarm={}, inactivity_time={}, inactivity_type={} " \
        "WHERE idx={};".format(
            name, alias, token, birthdate, email, lang_code, routine, alarm, inactivity_time, inactivity_type, idx
            )

    def delete_profile(self, idx):
        sql = "DELETE FROM defaultdb.profiles " \
        "WHERE idx={};".format(idx)

crud=CRUD()
#crud.create_profile()
crud.set_profile(1,"job esau torres jimenez","rolloatomico","456","2009-07-05 00:00:00","jobtorres277@gmail.com","python","Despierto Duermo",9,"07:00","00:20")
crud.set_profile(1,"Joel Alejandro Sanboval Camacho","rollo","498","2009-11-07 00:00:00","Joelsandoval277@gmail.com","python","Despierto Duermo",9,"07:00","00:20")
crud.set_profile(1,"job alan herrera martines","atomico","789","2009-10-05 00:00:00","JobHernandes277@gmail.com","python","Despierto Duermo",9,"07:00","00:20")
crud.set_profile(1,"carlos joel hernandes cruz","ralloatomico","355","2009-06-08 00:00:00","CarlosHernandes277@gmail.com","python","Despierto Duermo",9,"07:00","00:20")
crud.set_profile(1,"alan dickwii hernandes angeles","rollomitico","789","2009-03-05 00:00:00","AlanHernandes277@gmail.com","python","Despierto Duermo",9,"07:00","00:20")
crud.set_profile(1,"Alejandro Acercandro Camacho Sandoval","rol","340","2009-02-08 00:00:00","Alejandrosandoval277@gmail.com","python","Despierto Duermo",9,"07:00","00:20")
crud.set_profile(1,"Alan Dwii Angeles Hernandez","Epstein","067","2009-01-05 00:00:00","alandwii287@gmail.com","python","Despierto Duermo",9,"07:00","06:07")
crud.set_profile(1,"Carlos Gallardo Ledesma","matasapos","647","2009-09-05 00:00:00","CarlosGallardo277@gmail.com","python","Despierto Duermo",9,"07:00","00:20")
crud.set_profile(1,"Rodriogo Brandon Angeles Martines","moni","899","2009-08-05 00:00:00","Rodrigoangeles277@gmail.com","python","Despierto Duermo",9,"07:00","00:20")
crud.set_profile(1,"Diego Yeray Herrera Ramos","DDy","878","2009-05-05 00:00:00","diegoHerrera277@gmail.com","python","Despierto Duermo",9,"07:00","00:20")


  