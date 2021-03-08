class CreateStudent:

    def __init__(self, Name, Surname, Password, Email, Address, conctactNumber, studentId):
          self.Name = Name
          self.Surname = Surname
          self.Password = Password
          self.Email = Email
          self.Address = Address
          self.conctactNumber = conctactNumber
          self.studentId = studentId
          print(self.Name, self.Surname, self.Password, self.Email, self.Address, self.conctactNumber, self.studentId)


class Register:
    stuList = 0


    def __init__(self):
        self.stuList = {}

    def createStudent(self):
        name = input("İsminizi giriniz")
        surname = input("Soyadınızı giriniz")
        password = input("Şifrenizi giriniz")
        email = input("Emailinizi giriniz")
        address = input("Adresinizi giriniz")
        concactNumber = input("Telefonun numaranızı giriniz")
        studentId = input("Öğrenci numaranızı giriniz")
        student = CreateStudent(name, surname, password, email, address, concactNumber, studentId)
        self.studentRegister(student)

    def studentRegister(self, student):
        self.stuList[student] = student
        print(self.stuList)

    def display(self):

        for item in self.stuList:
            print(item.Name, item.Surname, item.Password, item.Email, item.Address, item.conctactNumber, item.studentId)

class createcourse:
    classList = 0
    def __init__(self,coursecode = None,coursename = None,facultycode = None,startdate= None,enddate = None):
        self.coursecode = coursecode
        self.coursename = coursename
        self.facultycode = facultycode
        self.startdate = startdate
        self.enddate = enddate
        self.classList = {}
        print(self.coursecode,self.coursename,self.facultycode,self.startdate,self.enddate)




    def courses(self):
        coursecode = input("kurs kodunu giriniz")
        coursename = input(("kurs adını yazınız"))
        facultycode = input("fakülte kodunu giriniz")
        startdate = input("kursa başlangıç tarihini giriniz")
        enddate = input("kursun bitiş tarihini giriniz")

        course = createcourse(coursecode, coursename, facultycode, startdate, enddate)
        self.courseRegister(course)

    def courseRegister(self,course):
        self.classList[course] = course
        print(self.classList)

    def display(self):
        print(self.classList)
        for item in self.classList:
            print(item.coursecode, item.coursename,item.facultycode,item.startdate,item.enddate)

    def get_changedList(self):
        coursecode = input("kurs kodunu giriniz")
        coursename = input(("kurs adını yazınız"))
        facultycode = input("fakülte kodunu giriniz")
        startdate = input("kursa başlangıç tarihini giriniz")
        enddate = input("kursun bitiş tarihini giriniz")
        changedList = {
            "coursecode": coursecode,
            "coursename": coursename,
            "coursestartdate":startdate,
            "courseenddate": enddate,
            "facultycode": facultycode,

        }

        return changedList
    def modifycourse(self,coursecode, ):
        changedList = self.get_changedList()
        for data in self.classList:
            print(f' eski kurs kodu:{data.coursecode} eski kurs adı:{data.coursename} eski kurs başlangıç tarihi:{data.startdate}eski kurs bitiş tarihi:{ data.enddate}eski kurs fakülte kodu:{data.facultycode}')
            if data.coursecode == coursecode:
                data.coursename = changedList.get("coursename")
                data.startdate = changedList.get("startdate")
                data.enddate = changedList.get("enddate")
                data.facultycode = changedList.get("facultycode")
                print(f'yeni kurs kodu:{data.coursecode} yeni kurs adı:{data.coursename} yeni kurs başlangıç tarihi: {data.startdate }yeni kurs bitiş tarihi:{data.enddate} yeni fakülte kodu:{data.facultycode}')
                break

    def removecourse(self,coursecode):
        for item in self.classList:
            if item.coursecode == coursecode:
                print(item, " ")
                print(f'{item.coursename}isimli kurs silindi')

                self.classList.pop(item)
                break











def menu():
    selection = input("Select action")
    print(selection)
    return selection
selection = menu()
a = Register()
b = createcourse()

while selection != 12:
    if selection == "1":
        a.createStudent()
        selection = menu()

    if selection == "2":
        a.display()
        selection = menu()

    if selection == "5":
        b.display()
        selection = menu()

    if selection == "6":
        b.courses()
        selection = menu()
    if selection == "7":
        coursecode = input("hangi kursu değiştirmek istiyorsanız kodunu giriniz")
        b.modifycourse(coursecode)
        selection = menu()
    if selection == "8":
        coursecode = input("hangi kursu silmek istiyorsanız kodunu giriniz")
        b.removecourse(coursecode)
        selection = menu()






