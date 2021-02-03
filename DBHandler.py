import pymysql


class DBHandler:
    def __init__(self, DATABASEIP, DB_USER, DB_PASSWORD, DATABASE):
        self.DATABASEIP = DATABASEIP
        self.DB_USER = DB_USER
        self.DB_PASSWORD = DB_PASSWORD
        self.DATABASE = DATABASE

    def __del__(self):
        print("Destructor")

    def insertFeedback(self, name, email, subject, message):
        db = None
        cursor = None
        insert = False
        try:
            db = pymysql.connect(host=self.DATABASEIP, port=3305, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'insert into feedbacks (name, email, subject, message) values (%s,%s,%s,%s)'
            args = (name, email, subject, message)
            cur.execute(sql, args)
            insert = True

        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
        return insert

    def signin(self, userid, password, type):
        db = None
        cursor = None
        insert = False
        try:
            db = pymysql.connect(host=self.DATABASEIP, port=3305, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            if (type == "user"):
                sql = 'Select * from users  WHERE userid=%s AND passwd=%s'
                args = (userid, password)
                cur.execute(sql, args)
                result = cur.fetchone()
                return result
            else:
                sql = 'Select * from admins WHERE userid=%s AND passwd=%s'
                args = (userid, password)
                cur.execute(sql, args)
                result = cur.fetchone()
                return result

        except Exception as e:
            print(e)
            print("some error")

    def getBirthCertificate(self, id):
        db = None
        cursor = None
        try:
            db = pymysql.connect(host=self.DATABASEIP, port=3305, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            print("here")
            sql = 'Select * from birthCertificates where user_idno = %s'
            args = (id)
            cur.execute(sql, args)
            result = cur.fetchone()
            return result

        except Exception as e:
            print(e)
            print("some error")
            return None;

    def getDomicile(self, id):
        db = None
        cursor = None
        try:
            db = pymysql.connect(host=self.DATABASEIP, port=3305, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            print("here")
            sql = 'Select * from domiciles where user_idno = %s'
            args = (id)
            cur.execute(sql, args)
            result = cur.fetchone()
            return result

        except Exception as e:
            print(e)
            print("some error")
            return None;

    def getCNIC(self, id):
        db = None
        cursor = None
        try:
            db = pymysql.connect(host=self.DATABASEIP, port=3305, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            print("here")
            sql = 'Select * from cnic where user_idno = %s'
            args = (id)
            cur.execute(sql, args)
            result = cur.fetchone()
            return result

        except Exception as e:
            print(e)
            print("some error")
            return None;

    def getDeathCertificate(self, id):
        db = None
        cursor = None
        try:
            db = pymysql.connect(host=self.DATABASEIP, port=3305, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            print("here")
            sql = 'Select * from deathCertificates where user_idno = %s'
            args = (id)
            cur.execute(sql, args)
            result = cur.fetchone()
            return result

        except Exception as e:
            print(e)
            print("some error")
            return None;

    def showUsers(self):
        db = None
        cursor = None
        try:
            db = pymysql.connect(host=self.DATABASEIP, port=3305, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            print("here")
            sql = 'Select * from users'
            cur.execute(sql)
            result = cur.fetchall()

        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return result

    def showFeedBack(self):
        db = None
        cursor = None
        try:
            db = pymysql.connect(host=self.DATABASEIP, port=3305, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            print("here")
            sql = 'Select * from feedbacks'
            cur.execute(sql)
            result = cur.fetchall()

        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return result

    def storeDataForBC(self, userid, candidate, relation, childName, fname, mname, gender, religion, districtOfDOB,
                       grandFatherName, grandFatherCNIC, dob, address, district, tehsil, doi):
        db = None
        cursor = None
        insert = False
        try:
            db = pymysql.connect(host=self.DATABASEIP, port=3305, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'insert into birthcertificates (user_idno, candidateName, relation, childName, fatherName, motherName, gender,' \
                  ' religion, districtOfDOB, grandFatherName, grandFatherCNIC, dateOfBirth, address, tehsil, district, dateOfIssue)' \
                  ' values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            args = (userid, candidate, relation, childName, fname, mname, gender, religion, districtOfDOB,
                    grandFatherName, grandFatherCNIC, dob, address, tehsil, district, doi)
            cur.execute(sql, args)
            insert = True

        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return insert

    def storeDataForCNIC(self, userid, uname, fname, gender, country, cnic, dob, doi, doe, currAddress, permAddress):
        db = None
        cursor = None
        insert = False
        try:
            db = pymysql.connect(host=self.DATABASEIP, port=3305, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'insert into cnic (user_idno, name, fatherName, gender, country, cnic, dateOfBirth, dateOfIssue, dateOfExpiry, currentAddress, permanentAddress)' \
                  ' values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            args = (userid, uname, fname, gender, country, cnic, dob, doi, doe, currAddress, permAddress)
            cur.execute(sql, args)
            insert = True

        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return insert

    def storeDataForDC(self, userid, unc, no, place, district, applicantName, applicantCNIC, relation, decessedName,
                       decessedCNIC, gender, religion, fname, fatherCNIC, graveyardName, dob, dod, reason, address,
                       occupation, markOfIndication, natureOfDeath):
        db = None
        cursor = None
        insert = False
        try:
            db = pymysql.connect(host=self.DATABASEIP, port=3305, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'insert into deathcertificates (user_idno, unc, no,place,district,applicantName,' \
                  'applicantCNIC,relation,decessedName,decessedCNIC, gender, religion,fatherName,fatherCNIC,graveyardName,' \
                  'dateOfBirth,dateOfDeath,reasonOfDeath,address,occupation,markOfIndication, natureOfDeath) ' \
                  'values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            args = (
                userid, unc, no, place, district, applicantName, applicantCNIC, relation, decessedName,
                decessedCNIC, gender, religion, fname, fatherCNIC, graveyardName, dob, dod, reason, address,
                occupation, markOfIndication, natureOfDeath)
            cur.execute(sql, args)
            insert = True

        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return insert

    def storeDataForD(self, userid, name, fname, province, place, district, tehsil, address, occupation, status,
                      student,
                      markOfIndication, doi):
        db = None
        cursor = None
        insert = False
        try:
            db = pymysql.connect(host=self.DATABASEIP, port=3305, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'insert into domiciles (user_idno, name,fatherName,province,placeOfdomicile,district,tehsil,address,' \
                  'occupation, maritualStatus,isStudent, markOfIndication,dateOfIssue) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

            args = (userid, name, fname, province, place, district, tehsil, address, occupation, status, student,
                    markOfIndication, doi)
            cur.execute(sql, args)
            insert = True

        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return insert

    def updateDataForBC(self, userid, candidate, relation, childName, fname, mname, gender, religion, districtOfDOB,
                        grandFatherName, grandFatherCNIC, dob, address, district, tehsil, doi):
        db = None
        cursor = None
        update = True
        try:
            db = pymysql.connect(host=self.DATABASEIP, port=3305, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'update birthcertificates set candidateName=%s, relation=%s, childName=%s, fatherName=%s, motherName=%s, gender=%s, religion=%s, districtOfDOB=%s, grandFatherName=%s, grandFatherCNIC=%s, dateOfBirth=%s, address=%s, tehsil=%s, district=%s, dateOfIssue=%s where user_idno=%s'
            args = (candidate, relation, childName, fname, mname, gender, religion, districtOfDOB,
                    grandFatherName, grandFatherCNIC, dob, address, tehsil, district, doi, userid)
            cur.execute(sql, args)
            db.commit()
            update = True

        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return update

    def updateDataForCNIC(self, userid, uname, fname, gender, country, cnic, dob, doi, doe, currAddress, permAddress):
        db = None
        cursor = None
        update = True
        try:
            db = pymysql.connect(host=self.DATABASEIP, port=3305, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'update cnic set fatherName=%s, name=%s, gender=%s, country=%s, cnic=%s, dateOfBirth=%s, dateOfIssue=%s, dateOfExpiry=%s, currentAddress=%s, permanentAddress=%s where user_idno=%s'
            args = (fname, uname, gender, country, cnic, dob, doi, doe, currAddress, permAddress, userid)
            cur.execute(sql, args)
            db.commit()
            update = True

        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return update

        db = None
        cursor = None
        insert = False
        try:
            db = pymysql.connect(host=self.DATABASEIP, port=3305, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'insert into deathcertificates (user_idno, unc, no,place,district,applicantName,' \
                  'applicantCNIC,relation,decessedName,decessedCNIC, gender, religion,fatherName,fatherCNIC,graveyardName,' \
                  'dateOfBirth,dateOfDeath,reasonOfDeath,address,occupation,markOfIndication, natureOfDeath) ' \
                  'values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            args = (
                userid, unc, no, place, district, applicantName, applicantCNIC, relation, decessedName,
                decessedCNIC, gender, religion, fname, fatherCNIC, graveyardName, dob, dod, reason, address,
                occupation, markOfIndication, natureOfDeath)
            cur.execute(sql, args)
            insert = True

        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return insert

    def updateDataForDC(self, userid, unc, no, place, district, applicantName, applicantCNIC, relation, decessedName,
                        decessedCNIC, gender, religion, fname, fatherCNIC, graveyardName, dob, dod, reason, address,
                        occupation, markOfIndication, natureOfDeath):
        db = None
        cursor = None
        update = True
        try:
            db = pymysql.connect(host=self.DATABASEIP, port=3305, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'update deathcertificates set unc=%s, no=%s, place=%s, district=%s, applicantName=%s, applicantCNIC=%s, relation=%s,' \
                  ' decessedName=%s, decessedCNIC=%s, gender=%s, religion=%s, fatherName=%s, fatherCNIC=%s, graveyardName=%s,' \
                  'dateOfBirth=%s, dateOfDeath=%s, reasonOfDeath=%s, address=%s, occupation=%s, markOfIndication=%s, natureOfDeath=%s where user_idno=%s'
            args = (unc, no, place, district, applicantName, applicantCNIC, relation, decessedName,
                    decessedCNIC, gender, religion, fname, fatherCNIC, graveyardName, dob, dod, reason, address,
                    occupation, markOfIndication, natureOfDeath, userid)
            cur.execute(sql, args)
            db.commit()
            update = True

        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return update

    def updateDataForD(self, userid, name, fname, province, place, district, tehsil, address, occupation, status,
                       student,
                       markOfIndication, doi):
        db = None
        cursor = None
        update = True
        try:
            db = pymysql.connect(host=self.DATABASEIP, port=3305, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'update domiciles set name=%s, fatherName=%s, province=%s, placeOfdomicile=%s, district=%s, tehsil=%s, address=%s, occupation=%s, maritualStatus=%s, isStudent=%s, markOfIndication=%s, dateOfIssue=%s where user_idno=%s'
            args = (name, fname, province, place, district, tehsil, address, occupation, status, student,
                    markOfIndication, doi, userid)
            cur.execute(sql, args)
            db.commit()
            update = True

        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return update

    def addUser(self, fname, lname, userid, pwd):
        db = None
        cursor = None
        insert = False
        try:
            db = pymysql.connect(host=self.DATABASEIP, port=3305, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'insert into users (firstName,lastName,userId,passwd) values (%s,%s,%s,%s)'

            args = (fname, lname, userid, pwd)
            insert = cur.execute(sql, args)

        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return insert

    def isUserAlreadyExits(self, userid):
        db = None
        cursor = None
        try:
            db = pymysql.connect(host=self.DATABASEIP, port=3305, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'Select * from users where userid = %s'
            args = (userid)
            cur.execute(sql, args)
            result = cur.fetchone()
            if (result == None):
                return False
            else:
                return True
        except Exception as e:
            print(e)
            return True

    def isDataAlreadyExits(self, userid, tableName):
        db = None
        cursor = None
        try:
            db = pymysql.connect(host=self.DATABASEIP, port=3305, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'Select * from ' + tableName + ' where user_idno = %s'
            args = (userid)
            cur.execute(sql, args)
            result = cur.fetchone()
            if (result == None):
                return False
            else:
                return True
        except Exception as e:
            print(e)
            return True

    def getUserId(self, FirstName, LastName, UserID, Password):
        db = None
        cursor = None
        try:
            db = pymysql.connect(host=self.DATABASEIP, port=3305, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'select id from users where firstName=%s AND lastName=%s AND userId=%s AND passwd=%s'
            args = (FirstName, LastName, UserID, Password)
            cur.execute(sql, args)
            result = cur.fetchone()
            return result[0]
        except Exception as e:
            print(e)

    def deleteUser(self, id):
        db = None
        cursor = None
        try:
            db = pymysql.connect(host=self.DATABASEIP, port=3305, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'Delete from users where id = %s'
            args = (id)
            result = cur.execute(sql, args)
            db.commit()
            if (result == None):
                return False
            else:
                return True
        except Exception as e:
            print(e)
            return False

    def deleteRecord(self, userId, tableName):
        db = None
        cursor = None
        try:
            db = pymysql.connect(host=self.DATABASEIP, port=3305, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'Delete from ' + tableName + ' where user_idno = %s'
            args = (userId)
            result = cur.execute(sql, args)
            db.commit()
            if (result == None):
                return False
            else:
                return True
        except Exception as e:
            print(e)
            return False


def Test():
    db = DBHandler("localhost", "root", "12345", "nadra")


if __name__ == '__main__':
    Test()
