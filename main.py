import string
from flet import*
def main(page: Page):
    # واجهة التطبيق الأساسية 
    page.title = "Caesar cipher  App"
    page.window.width = 370
    page.window.height = 700
    page.bgcolor = Colors.RED
    page.window.top = 10
    page.window.left = 450
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.scroll = 'auto'
    # نهاية الواجهة الاساسية    
    # دالة الشفرة
    usr_message = TextField(label="Message to Encrypt",color=Colors.BLACK,multiline=True,min_lines=3,max_lines=7)
    usr_num = TextField(label="Shift Number",color=Colors.BLACK)

    result_text = Text("", size=19, color=Colors.BLACK,width=390,text_align="center",weight=FontWeight.BOLD)  
    tt = Text("")
    def Caesar_cipher(h):
        message = usr_message.value or ""
        # فحص الرقم
        if usr_num.value.strip() == "":
            result_text.value = "Please enter the encryption number"
            page.update()
            return

        num = int(usr_num.value)

        # بدون أي شرط يمنع الرموز
        letters = string.ascii_lowercase * 2
        result = ""

        for x in message:
            if x.isalpha():  # تطبيق شيفرة قيصر على الأحرف فقط
                letter_index = letters.index(x.lower())
                new_letter = letters[letter_index + num]
                if x.isupper():
                    new_letter = new_letter.upper()
                result += new_letter
            else:
                # ترك أي أرقام أو رموز أو مسافات كما هي
                result += x

        result_text.value = f"code word : {result}"
        tt.value = result
        page.update()   
                            
        

#########################################
    def Decode__cipher(d):
        message = usr_message.value or ""
        # فحص الرقم
        if usr_num.value.strip() == "":
            result_text.value = "Please enter the encryption number"
            page.update()
            return

        num = int(usr_num.value)

        # بدون أي شرط يمنع الرموز
        letters = string.ascii_lowercase * 2
        result = ""

        for x in message:
            if x.isalpha():  # تطبيق شيفرة قيصر على الأحرف فقط
                letter_index = letters.index(x.lower())
                new_letter = letters[letter_index - num]
                if x.isupper():
                    new_letter = new_letter.upper()
                result += new_letter
            else:
                # ترك أي أرقام أو رموز أو مسافات كما هي
                result += x

        result_text.value = f"code word : {result}"
        tt.value = result
        page.update()
##########################################

    # نهاية الدالة
    def copy(c):
        page.set_clipboard(tt.value)

    def show_page(v):
        page.views.clear()
        page.views.append(View("/",[
            AppBar(title=Text("Caesar cipher  App",
                              color=Colors.BLACK,size=35,width=390,text_align="center",weight=FontWeight.BOLD),
                              bgcolor=Colors.WHITE
                              ),
                                          Text(),     
            Text("Welcome to the Caesar Cipher app",
                 size=25,color=Colors.BLACK,width=390,text_align="center",weight=FontWeight.BOLD),
            Text(),     
            Text("Use this app to encrypt or decrypt your messages using the Caesar operating technique. Select one of the options below to begin."
                 ,size=20,color=Colors.BLACK,
                 width=390,text_align="center"
                 ),
            Text(),
            Text(),     
            Row([ElevatedButton("Create Cipher",
                           bgcolor=Colors.BLUE,width=210,height=60,color=Colors.WHITE,
                           on_click=lambda e:page.go("/انشاء"),style=ButtonStyle(text_style=TextStyle(size=20)))],alignment=MainAxisAlignment.CENTER,),
                           
            Row([ElevatedButton("Decode Message",
                            bgcolor=Colors.BLUE,width=210,height=60,color=Colors.WHITE,
                            on_click=lambda e:page.go("/فك"),style=ButtonStyle(text_style=TextStyle(size=20)))],alignment=MainAxisAlignment.CENTER)
        ],bgcolor=Colors.WHITE))

        if page.route == "/انشاء":
            page.views.append(View("/انشاء",[
                AppBar(title=Text("Create Cipher",color=Colors.BLACK,
                                  size=33,width=390,text_align="center",weight=FontWeight.BOLD
                                  ),bgcolor=Colors.WHITE),
                                              Text(),     
                usr_message,usr_num,result_text,
                Text(),
                Row([ElevatedButton("Generate Cipher",color=Colors.WHITE,width=200,height=55,on_click=Caesar_cipher,bgcolor=Colors.BLUE,style=ButtonStyle(text_style=TextStyle(size=20)))],
                    alignment=MainAxisAlignment.CENTER),
               Row([OutlinedButton("Copy to Clipboard",icon=Icons.COPY,on_click=copy,width=200,height=55,style=ButtonStyle(text_style=TextStyle(size=18)))],alignment=MainAxisAlignment.CENTER)     ,
            ],bgcolor=Colors.WHITE))

        elif page.route == "/فك":
            page.views.append(View("/فك",[
                AppBar(title=Text("Decode Message",color=Colors.BLACK,
                                  size=33,width=390,text_align="center",weight=FontWeight.BOLD
                                  ),bgcolor=Colors.WHITE),
                                              Text(),     
                usr_message,usr_num,result_text,
                Text(),
                Row([ElevatedButton("Decode Message",color=Colors.WHITE,width=200,height=55,on_click=Decode__cipher,bgcolor=Colors.BLUE,style=ButtonStyle(text_style=TextStyle(size=20)))],
                    alignment=MainAxisAlignment.CENTER),
                Row([OutlinedButton("Copy to Clipboard",icon=Icons.COPY,on_click=copy,width=200,height=55,style=ButtonStyle(text_style=TextStyle(size=18)))],alignment=MainAxisAlignment.CENTER),
            ],bgcolor=Colors.WHITE))

        page.update()
    # دالة الرجوع للوراء
    def page_go(g):
        page.views.pop()
        go_p = page.views[-1]
        page.go(go_p.route)

    page.update()
    page.on_route_change = show_page
    page.on_view_pop = page_go
    page.go(page.route)
app(main)
