from flask import Flask, request, render_template, url_for, redirect, sessions, session, Blueprint, flash
from DBHandler import DBHandler

app = Flask(__name__)
app.config.from_object('config')


# routes = Blueprint('routes', __name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    if session.get('type') == 'user':
        return redirect(url_for('userWelcome'))
    elif session.get('type') == 'admin':
        return redirect(url_for('adminWelcome'))
    else:
        return render_template('login.html')

@app.route('/AddUser.html')
def addUser():
    return render_template('AddUser.html')

@app.route('/administratorWelcome.html')
def adminWelcome():
    return render_template('administratorWelcome.html')

@app.route('/addUser', methods=['POST'])
def add_User():
    firstName = request.form['firstName'].capitalize()
    lastName = request.form['lastName'].capitalize()
    userId = request.form['userId']
    paswd = request.form['pwd']
    db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])
    if (db.isUserAlreadyExits(userId)==True):
        error='exists'
    else:
        result= db.addUser(firstName,lastName,userId,paswd)
        if(result==True):
            error='successfull'
        else:
            error='unsuccessfull'

    return render_template('AddUser.html',error=error)

@app.route('/CNIC.html')
def cnic():
    error = None
    db = None
    try:
        db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                       app.config["DATABASE"])
        id = session['id']
        result = db.getCNIC(id)
        if (result == None):
            error = 'Sorry! You Dont have a CNIC. Please ask the NADRA Administrator to Issue you a CNIC.'
        else:
            user_idno = result[0]
            name = result[1]
            fatherName = result[2]
            gender = result[3]
            country = result[4]
            cnic=result[5]
            dateOfBirth = result[6]
            dateOfIssue = result[7]
            dateOfExpiry = result[8]
            currentAddress = result[9]
            permanentAddress = result[10]
            return render_template('CNIC.html', error=error,
                                   user_idno=user_idno,
                                   name=name,
                                   fatherName=fatherName,
                                   gender=gender,
                                   country=country,
                                   cnic=cnic,
                                   dateOfBirth=dateOfBirth,
                                   dateOfIssue=dateOfIssue,
                                   dateOfExpiry=dateOfExpiry,
                                   currentAddress=currentAddress,
                                   permanentAddress=permanentAddress)
        return render_template('CNIC.html', error=error)
    except Exception as e:
        print(e)
        error = str(e)
        return render_template('CNIC.html', error=error)

@app.route('/deathCertificate.html')
def deathCertificate():
    error = None
    db = None
    try:
        db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                       app.config["DATABASE"])
        id = session['id']
        result = db.getDeathCertificate(id)
        if (result == None):
            error = 'Sorry! Death Certificate is not Issued to this User Yet.'
        else:
            user_idno = result[0]
            unc = result[1]
            no = result[2]
            place = result[3]
            district = result[4]
            applicantName = result[5]
            applicantCNIC = result[6]
            relation = result[7]
            decessedName = result[8]
            decessedCNIC = result[9]
            gender = result[10]
            religion = result[11]
            fatherName = result[12]
            fatherCNIC = result[13]
            graveyardName = result[14]
            dateOfBirth = result[15]
            dateOfDeath = result[16]
            reasonOfDeath = result[17]
            address = result[18]
            occupation = result[19]
            markOfIndication = result[20]
            natureOfDeath = result[21]

            return render_template('deathCertificate.html', error=error,
                                   user_idno=user_idno,
                                   unc=unc,
                                   no=no,
                                   place=place,
                                   district=district,
                                   applicantName=applicantName,
                                   applicantCNIC=applicantCNIC,
                                   relation=relation,
                                   decessedName=decessedName,
                                   decessedCNIC=decessedCNIC,
                                   gender=gender,
                                   religion=religion,
                                   fatherName=fatherName,
                                   fatherCNIC=fatherCNIC,
                                   graveyardName=graveyardName,
                                   dateOfBirth=dateOfBirth,
                                   dateOfDeath=dateOfDeath,
                                   reasonOfDeath=reasonOfDeath,
                                   address=address,
                                   occupation=occupation,
                                   markOfIndication=markOfIndication,
                                   natureOfDeath=natureOfDeath
                                   )
        return render_template('deathCertificate.html', error=error)
    except Exception as e:
        print(e)
        error = str(e)
        return render_template('deathCertificate.html', error=error)


@app.route('/feedback', methods=['POST'])
def feedback():
    error = None
    db = None
    try:
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                       app.config["DATABASE"])
        result = db.insertFeedback(name, email, subject, message)
        if (result != True):
            flash("Message Not Sent!")
        else:
            flash("Your Message have been Sent!")
            return redirect(url_for('index', _anchor='feedBack'))

    except Exception as e:
        print(e)
        error = str(e)
        return redirect(url_for('index', _anchor='feedBack'))


@app.route('/domicile.html')
def domicile():
    error = None
    db = None
    try:
        db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                       app.config["DATABASE"])
        id = session['id']
        result = db.getDomicile(id)
        if (result == None):
            error = 'Sorry! You Dont have a Domicile. Please Contact Administrator to Issue you a Domicile.'
        else:
            user_idno = result[0]
            name = result[1]
            fatherName = result[2]
            province = result[3]
            placeOfDomicile = result[4]
            district = result[5]
            tehsil = result[6]
            address = result[7]
            occupation = result[8]
            maritualStatus = result[9]
            isStudent = result[10]
            markOfIndication = result[11]
            dateOfIssue = result[12]
            return render_template('domicile.html', error=error, number=user_idno,
                                   name=name,
                                   fatherName=fatherName,
                                   province=province,
                                   placeOfDomicile=placeOfDomicile,
                                   district=district,
                                   tehsil=tehsil,
                                   address=address,
                                   occupation=occupation,
                                   maritualStatus=maritualStatus,
                                   isStudent=isStudent,
                                   markOfIndication=markOfIndication,
                                   dateOfIssue=dateOfIssue,
                                   )
        return render_template('domicile.html', error=error)
    except Exception as e:
        print(e)
        error = str(e)
        return render_template('domicile.html', error=error)


@app.route('/fee.html')
def f():
    return render_template('fee.html')

@app.route('/delete_User')
def du():
    return render_template('deleteUser.html')

@app.route("/deleteUser", methods=["GET", "POST"])
def deleteUser():
    firstName = request.form["firstName"].capitalize()
    lastName = request.form["lastName"].capitalize()
    userID = request.form["userID"]
    password = request.form["pwd"]
    error = None
    db = None
    db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"], app.config["DATABASE"])
    id = db.getUserId(firstName, lastName, userID, password)
    if (id == None):
        error="unsuccessfull"
    else:
        if (db.isDataAlreadyExits(id, "birthCertificates") == False):
            db.deleteRecord(id, "birthCertificates")
        if (db.isDataAlreadyExits(id, "domiciles") == False):
            db.deleteRecord(id, "domiciles")
        if (db.isDataAlreadyExits(id, "cnic") == False):
            db.deleteRecord(id, "cnic")
        if (db.isDataAlreadyExits(id, "deathCertificates") == False):
            db.deleteRecord(id, "deathCertificates")
        db.deleteUser(id)
        error='successfull'

    return render_template('deleteUser.html', error=error)

@app.route('/viewRecords')
def viewRecords():
    db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])
    result = db.showUsers()
    return render_template('usersForViweingRecords.html', result=result)

@app.route("/getRecord", methods=["GET", "POST"])
def getRecord():
    userid=request.form['users']
    recordType = request.form['record']
    db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"], app.config["DATABASE"])
    result1 = db.isDataAlreadyExits(userid, recordType)
    result2 = db.showUsers()
    error=None
    if (result1 == False):
        error='not'
        return render_template('usersForViweingRecords.html', result=result2, error=error, recordType=recordType)
    else:
        result = None;
        if(recordType=='birthCertificates'):
            result=db.getBirthCertificate(userid)
            candidateName = result[1]
            relation = result[2]
            childName = result[3]
            fName = result[4]
            mName = result[5]
            gender = result[6]
            religion = result[7]
            districtOfDOB = result[8]
            grandFatherName = result[9]
            grandFatherCNIC = result[10]
            dob = result[11]
            address = result[12]
            tehsil = result[13]
            district = result[14]
            doi = result[15]
            return render_template('viewBirthCertificate.html', candidateName=candidateName, relation=relation,
                                   childName=childName,
                                   fName=fName,
                                   mName=mName,
                                   gender=gender,
                                   religion=religion,
                                   districtOfDOB=districtOfDOB,
                                   grandFatherName=grandFatherName,
                                   grandFatherCNIC=grandFatherCNIC,
                                   dob=dob,
                                   address=address,
                                   tehsil=tehsil,
                                   district=district,
                                   doi=doi)

        elif(recordType=='cnic'):
            result=db.getCNIC(userid)
            user_idno = result[0]
            name = result[1]
            fatherName = result[2]
            gender = result[3]
            country = result[4]
            cnic = result[5]
            dateOfBirth = result[6]
            dateOfIssue = result[7]
            dateOfExpiry = result[8]
            currentAddress = result[9]
            permanentAddress = result[10]
            return render_template('viewCNIC.html',
                                   user_idno=user_idno,
                                   name=name,
                                   fatherName=fatherName,
                                   gender=gender,
                                   country=country,
                                   cnic=cnic,
                                   dateOfBirth=dateOfBirth,
                                   dateOfIssue=dateOfIssue,
                                   dateOfExpiry=dateOfExpiry,
                                   currentAddress=currentAddress,
                                   permanentAddress=permanentAddress)

        elif(recordType=='domiciles'):
            result=db.getDomicile(userid)
            user_idno = result[0]
            name = result[1]
            fatherName = result[2]
            province = result[3]
            placeOfDomicile = result[4]
            district = result[5]
            tehsil = result[6]
            address = result[7]
            occupation = result[8]
            maritualStatus = result[9]
            isStudent = result[10]
            markOfIndication = result[11]
            dateOfIssue = result[12]
            return render_template('viewDomicile.html', number=user_idno,
                                   name=name,
                                   fatherName=fatherName,
                                   province=province,
                                   placeOfDomicile=placeOfDomicile,
                                   district=district,
                                   tehsil=tehsil,
                                   address=address,
                                   occupation=occupation,
                                   maritualStatus=maritualStatus,
                                   isStudent=isStudent,
                                   markOfIndication=markOfIndication,
                                   dateOfIssue=dateOfIssue,
                                   )

        elif(recordType=='deathCertificates'):
            result=db.getDeathCertificate(userid)
            user_idno = result[0]
            unc = result[1]
            no = result[2]
            place = result[3]
            district = result[4]
            applicantName = result[5]
            applicantCNIC = result[6]
            relation = result[7]
            decessedName = result[8]
            decessedCNIC = result[9]
            gender = result[10]
            religion = result[11]
            fatherName = result[12]
            fatherCNIC = result[13]
            graveyardName = result[14]
            dateOfBirth = result[15]
            dateOfDeath = result[16]
            reasonOfDeath = result[17]
            address = result[18]
            occupation = result[19]
            markOfIndication = result[20]
            natureOfDeath = result[21]
            return render_template('deathCertificate.html',
                                   user_idno=user_idno,
                                   unc=unc,
                                   no=no,
                                   place=place,
                                   district=district,
                                   applicantName=applicantName,
                                   applicantCNIC=applicantCNIC,
                                   relation=relation,
                                   decessedName=decessedName,
                                   decessedCNIC=decessedCNIC,
                                   gender=gender,
                                   religion=religion,
                                   fatherName=fatherName,
                                   fatherCNIC=fatherCNIC,
                                   graveyardName=graveyardName,
                                   dateOfBirth=dateOfBirth,
                                   dateOfDeath=dateOfDeath,
                                   reasonOfDeath=reasonOfDeath,
                                   address=address,
                                   occupation=occupation,
                                   markOfIndication=markOfIndication,
                                   natureOfDeath=natureOfDeath
                                   )

@app.route('/userForIssueCNIC')
def uficnic():
    db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])
    result = db.showUsers()
    return render_template('userForIssueCNIC.html', result=result)


@app.route('/userForIssueD')
def ufid():
    db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])
    result = db.showUsers()
    return render_template('userForIssueD.html', result=result)


@app.route('/userForIssueDC')
def ufidc():
    db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])
    result = db.showUsers()
    return render_template('userForIssueDC.html', result=result)

@app.route('/userForIssueBC')
def ufibc():
    db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])
    result = db.showUsers()
    return render_template('userForIssueBC.html', result=result)


@app.route('/issueBirthCertificate', methods=['POST'])
def ibc():
    userid = request.form['users']
    db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])
    result1 = db.isDataAlreadyExits(userid, "birthcertificates")
    result2 = db.showUsers()
    if (result1 == True):
        return render_template('userForIssueBC.html', result=result2, error="Selected User Already Has BirthCertificate")
    else:
        return render_template('issueBirthCertificate.html', userid=userid)


@app.route('/issueCNIC', methods=['POST'])
def icnic():
    userid = request.form['users']
    db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])
    result1 = db.isDataAlreadyExits(userid, "cnic")
    result2 = db.showUsers()
    if (result1 == True):
        return render_template('userForIssueCNIC.html', result=result2, error="Selected User Already Has CNIC")
    else:
        return render_template('issueCNIC.html', userid=userid)


@app.route('/issueDomicile', methods=['POST'])
def id():
    userid = request.form['users']
    db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])
    result1 = db.isDataAlreadyExits(userid, "domiciles")
    result2 = db.showUsers()
    if (result1 == True):
        return render_template('userForIssueD.html', result=result2, error="Selected User Already Has Domicile")
    else:
        return render_template('issueDomicile.html', userid=userid)


@app.route('/issueDeathCertificate', methods=['POST'])
def idc():
    userid = request.form['users']
    db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])
    result1 = db.isDataAlreadyExits(userid, "deathcertificates")
    result2 = db.showUsers()
    if (result1 == True):
        return render_template('userForIssueDC.html', result=result2, error="Selected User Already Has DeathCertificate")
    else:
        return render_template('issueDeathCertificate.html', userid=userid)

@app.route('/userForUpdateCNIC')
def ufucnic():
    db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])
    result = db.showUsers()
    return render_template('userForUpdateCNIC.html', result=result)


@app.route('/userForUpdateD')
def ufud():
    db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])
    result = db.showUsers()
    return render_template('userForUpdateD.html', result=result)


@app.route('/userForUpdateDC')
def ufudc():
    db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])
    result = db.showUsers()
    return render_template('userForUpdateDC.html', result=result)

@app.route('/userForUpdateBC')
def ufubc():
    db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])
    result = db.showUsers()
    return render_template('userForUpdateBC.html', result=result)

@app.route('/updateBirthCertificate', methods=['POST'])
def ubc():
    userid = request.form['users']
    db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])
    result1 = db.isDataAlreadyExits(userid, "birthcertificates")
    result2 = db.showUsers()
    result3= db.getBirthCertificate(userid)
    if (result1 == False):
        return render_template('userForUpdateBC.html', result=result2, error="Selected User Does Not Have a Birth Certificate. Please Issue Birth Certificate!")
    else:
        return render_template('updateBirthCertificate.html', data=result3)


@app.route('/updateCNIC', methods=['POST'])
def ucnic():
    userid = request.form['users']
    db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])
    result1 = db.isDataAlreadyExits(userid, "cnic")
    result2 = db.showUsers()
    result3= db.getCNIC(userid)
    if (result1 == False):
        return render_template('userForUpdateCNIC.html', result=result2, error="Selected User Does Not Have a CNIC. Please Issue CNIC!")
    else:
        return render_template('updateCNIC.html', data=result3)


@app.route('/updateDomicile', methods=['POST'])
def ud():
    userid = request.form['users']
    db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])
    result1 = db.isDataAlreadyExits(userid, "domiciles")
    result2 = db.showUsers()
    result3=db.getDomicile(userid)
    if (result1 == False):
        return render_template('userForUpdateD.html', result=result2, error="Selected User Does Not Have a Domicile. Please Issue Domicile!")
    else:
        return render_template('updateDomicile.html', data=result3)


@app.route('/updateDeathCertificate', methods=['POST'])
def udc():
    userid = request.form['users']
    db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])
    result1 = db.isDataAlreadyExits(userid, "deathcertificates")
    result2 = db.showUsers()
    result3=db.getDeathCertificate(userid)
    if (result1 == False):
        return render_template('userForUpdateDC.html', result=result2, error="Selected User Does Not Have a Death Certificate. Please Issue Death Certificate!")
    else:
        return render_template('updateDeathCertificate.html', data=result3)

@app.route('/storeDataForBC', methods=['GET', 'POST'])
def sdfbc():
    userid = request.form['userid']
    candidate = request.form['candidate'].capitalize()
    relation = request.form['relation']
    childName = request.form['childName'].capitalize()
    fname = request.form['fname'].capitalize()
    mname = request.form['mname'].capitalize()
    gender = request.form['gender']
    religion = request.form['religion']
    districtOfDOB = request.form['districtOfDOB']
    grandFatherName = request.form['grandFatherName'].capitalize()
    grandFatherCNIC = request.form['grandFatherCNIC'].capitalize()
    dob = request.form['dob']
    address = request.form['address'].capitalize()
    district = request.form['district']
    tehsil = request.form['tehsil']
    doi = request.form['doi']

    db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])

    result = db.storeDataForBC(userid, candidate, relation, childName, fname, mname, gender, religion, districtOfDOB,
                               grandFatherName, grandFatherCNIC, dob, address, district, tehsil, doi)

    return redirect(url_for('ufibc'))


@app.route('/storeDataForCNIC', methods=['GET', 'POST'])
def sdfcncic():
    userid = request.form['userid']
    uname = request.form['uname'].capitalize()
    fname = request.form['fname'].capitalize()
    gender = request.form['gender']
    country = request.form['country']
    cnic = request.form['cnic']
    dob = request.form['dob']
    doi = request.form['doi']
    doe = request.form['doe']
    currAddress = request.form['currAddress'].capitalize()
    permAddress = request.form['permAddress'].capitalize()

    db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])

    result = db.storeDataForCNIC(userid, uname, fname, gender, country, cnic, dob, doi, doe, currAddress, permAddress)

    return redirect(url_for('uficnic'))


@app.route('/storeDataForDC', methods=['GET', 'POST'])
def sdfdc():
    userid = request.form['userid']
    natureOfDeath = request.form['natureOfDeath']
    unc = request.form['unc']
    no = request.form['no']
    place = request.form['place']
    district = request.form['district']
    applicantName = request.form['applicantName'].capitalize()
    applicantCNIC = request.form['applicantCNIC']
    relation = request.form['relation']
    decessedName = request.form['decessedName'].capitalize()
    decessedCNIC = request.form['decessedCNIC']
    gender = request.form['gender']
    religion = request.form['religion']
    fname = request.form['fname'].capitalize()
    fatherCNIC = request.form['fatherCNIC']
    graveyardName = request.form['graveyardName'].capitalize()
    dob = request.form['dob']
    dod = request.form['dod']
    reason = request.form['reason'].capitalize()
    address = request.form['address'].capitalize()
    occupation = request.form['occupation'].capitalize()
    markOfIndication = request.form['markOfIndication'].capitalize()

    db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])

    result = db.storeDataForDC(userid, unc, no, place, district, applicantName, applicantCNIC, relation,
                               decessedName, decessedCNIC, gender, religion, fname, fatherCNIC, graveyardName, dob, dod,
                               reason,
                               address, occupation, markOfIndication, natureOfDeath)

    return redirect(url_for('ufidc'))


@app.route('/storeDataForD', methods=['GET', 'POST'])
def sdfd():
    userid = request.form['userid']
    name = request.form['name'].capitalize()
    fname = request.form['fname'].capitalize()
    province = request.form['province']
    place = request.form['districtOfDOB']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address'].capitalize()
    occupation = request.form['occupation'].capitalize()
    status = request.form['maritualStatus'].capitalize()
    student = request.form['isStudent'].capitalize()
    markOfIndication = request.form['markOfIndication'].capitalize()
    doi = request.form['doi']

    db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])

    result = db.storeDataForD(userid, name, fname, province, place, district, tehsil, address, occupation, status,
                              student, markOfIndication, doi)
    return redirect(url_for('ufid'))

@app.route('/updateDataForBC', methods=['GET', 'POST'])
def udfbc():
    userid = request.form['userid']
    candidate = request.form['candidate'].capitalize()
    relation = request.form['relation']
    childName = request.form['childName'].capitalize()
    fname = request.form['fname'].capitalize()
    mname = request.form['mname'].capitalize()
    gender = request.form['gender']
    religion = request.form['religion']
    districtOfDOB = request.form['districtOfDOB']
    grandFatherName = request.form['grandFatherName'].capitalize()
    grandFatherCNIC = request.form['grandFatherCNIC'].capitalize()
    dob = request.form['dob']
    address = request.form['address'].capitalize()
    district = request.form['district']
    tehsil = request.form['tehsil']
    doi = request.form['doi']

    db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])

    result = db.updateDataForBC(userid, candidate, relation, childName, fname, mname, gender, religion, districtOfDOB,
                               grandFatherName, grandFatherCNIC, dob, address, district, tehsil, doi)

    return redirect(url_for('ufubc'))


@app.route('/updateDataForCNIC', methods=['GET', 'POST'])
def udfcncic():
    userid = request.form['userid']
    uname = request.form['uname'].capitalize()
    fname = request.form['fname'].capitalize()
    gender = request.form['gender']
    country = request.form['country']
    cnic = request.form['cnic']
    dob = request.form['dob']
    doi = request.form['doi']
    doe = request.form['doe']
    currAddress = request.form['currAddress'].capitalize()
    permAddress = request.form['permAddress'].capitalize()

    db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])

    result = db.updateDataForCNIC(userid, uname, fname, gender, country, cnic, dob, doi, doe, currAddress, permAddress)

    return redirect(url_for('ufucnic'))

@app.route('/updateDataForDC', methods=['GET', 'POST'])
def udfdc():
    userid = request.form['userid']
    natureOfDeath = request.form['natureOfDeath']
    unc = request.form['unc']
    no = request.form['no']
    place = request.form['place']
    district = request.form['district']
    applicantName = request.form['applicantName'].capitalize()
    applicantCNIC = request.form['applicantCNIC']
    relation = request.form['relation']
    decessedName = request.form['decessedName'].capitalize()
    decessedCNIC = request.form['decessedCNIC']
    gender = request.form['gender']
    religion = request.form['religion']
    fname = request.form['fname'].capitalize()
    fatherCNIC = request.form['fatherCNIC']
    graveyardName = request.form['graveyardName'].capitalize()
    dob = request.form['dob']
    dod = request.form['dod']
    reason = request.form['reason'].capitalize()
    address = request.form['address'].capitalize()
    occupation = request.form['occupation'].capitalize()
    markOfIndication = request.form['markOfIndication'].capitalize()

    db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])

    result = db.updateDataForDC(userid, unc, no, place, district, applicantName, applicantCNIC, relation,
                               decessedName, decessedCNIC, gender, religion, fname, fatherCNIC, graveyardName, dob, dod,
                               reason,
                               address, occupation, markOfIndication, natureOfDeath)


    return redirect(url_for('ufudc'))

@app.route('/updateDataForD', methods=['GET', 'POST'])
def udfd():
    userid = request.form['userid']
    name = request.form['name'].capitalize()
    fname = request.form['fname'].capitalize()
    province = request.form['province']
    place = request.form['districtOfDOB']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address'].capitalize()
    occupation = request.form['occupation'].capitalize()
    status = request.form['maritualStatus'].capitalize()
    student = request.form['isStudent'].capitalize()
    markOfIndication = request.form['markOfIndication'].capitalize()
    doi = request.form['doi']
    db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])

    result = db.updateDataForD(userid, name, fname, province, place, district, tehsil, address, occupation, status,
                              student, markOfIndication, doi)

    return redirect(url_for('ufud'))

@app.route('/officeTimings.html')
def ot():
    return render_template('officeTimings.html')

@app.route('/userWelcome.html')
def userWelcome():
    return render_template('userWelcome.html')

@app.route('/index.html')
def projects():
    return render_template('index.html')


@app.route('/log-out')
def sign_out():
    session.pop('logged_in')
    session.pop('username')
    session.pop('id')
    session.pop('userid')
    session.pop('type')
    return redirect(url_for('index'))


@app.route('/administratorSignIn', methods=['POST'])
def admSignIn():
    error = None
    db = None
    try:
        userId = request.form['userid']
        password = request.form['password']
        db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                       app.config["DATABASE"])
        result = db.signin(userId, password, "adm")
        if (result == None):
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            session['id'] = result[0]
            session['username'] = result[1]
            session['userid'] = result[3]
            session['type'] = 'admin'
            return redirect(url_for('.adminWelcome'))

        return render_template('login.html', error=error)

    except Exception as e:
        print(e)
        error = str(e)
        return render_template('login.html', error=error)


@app.route('/userSignIn', methods=['POST'])
def userSignIn():
    error = None
    db = None
    try:
        userId = request.form['userid']
        password = request.form['password']
        db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                       app.config["DATABASE"])
        result = db.signin(userId, password, "user")
        if (result == None):
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True;
            session['id'] = result[0]
            session['username'] = result[1].capitalize()
            session['userid'] = result[3]
            session['type'] = 'user'
            return redirect(url_for('userWelcome'))

        return render_template('login.html', error=error)

    except Exception as e:
        print(e)
        error = str(e)
        return render_template('login.html', error=error)


@app.route('/userData')
def userData():
    db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])
    result = db.showUsers()
    return render_template('userData.html', result=result)


@app.route('/checkFeedbacks', methods=['GET', 'POST'])
def userFeedBack():
    db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])
    result = db.showFeedBack()
    return render_template('feedbacks.html', result=result)


@app.route('/birthCertificate.html')
def birthCerificate():
    error = None
    db = None
    try:
        db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                       app.config["DATABASE"])
        id = session['id']
        result = db.getBirthCertificate(id)
        if (result == None):
            error = 'Sorry! You Dont have a Birth Certificate. Please Contact Administrator to Issue you a Birth Certificate.'
        else:
            candidateName = result[1]
            relation = result[2]
            childName = result[3]
            fName = result[4]
            mName = result[5]
            gender = result[6]
            religion = result[7]
            districtOfDOB = result[8]
            grandFatherName = result[9]
            grandFatherCNIC = result[10]
            dob = result[11]
            address = result[12]
            tehsil = result[13]
            district = result[14]
            doi = result[15]
            return render_template('BirthCertificate.html', error=error, candidateName=candidateName, relation=relation,
                                   childName=childName,
                                   fName=fName,
                                   mName=mName,
                                   gender=gender,
                                   religion=religion,
                                   districtOfDOB=districtOfDOB,
                                   grandFatherName=grandFatherName,
                                   grandFatherCNIC=grandFatherCNIC,
                                   dob=dob,
                                   address=address,
                                   tehsil=tehsil,
                                   district=district,
                                   doi=doi)

        return render_template('birthCertificate.html', error=error)
    except Exception as e:
        print(e)
        error = str(e)
        return render_template('birthCertificate.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)
