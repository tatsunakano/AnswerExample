import csv
from email.message import EmailMessage
from email.generator import Generator

#メール本文用テキスト
def read_txt(path):
    with open(path,'r',encoding='utf-8') as f:
        return f.read()

def create_mail(subject, to_addr, cc_addr, from_addr, body_txt):
    mail_data = EmailMessage()
    mail_data["subject"] = subject
    mail_data["To"] = to_addr
    mail_data["CC"] = cc_addr
    mail_data["From"] = from_addr
    mail_data.set_content(body_txt)
    return mail_data

def att_check():
    try:
        mail_attach = input("添付ファイルを入れる場合は、「1」を不要の場合は「2」を入れてください。")
        mail_attach_int = int(mail_attach)
    except ValueError:
        print("【エラー】数字の「1」もしくは「2」を入れてください。")
        sys.exit()

    if mail_attach_int == 0:
        print("【エラー】数字の「1」もしくは「2」を入れてください。")
        sys.exit()
    elif mail_attach_int > 3:
        print("【エラー】数字の「1」もしくは「2」を入れてください。")
        sys.exit()




