import smtplib
import time
import imaplib
import email

# -------------------------------------------------
# Utility to read email from Gmail Using Python
# ------------------------------------------------
def read_email(email, password):
    if email.endswith("@gmail.com"):
        return read_email_from_gmail(email, password)
    else:
        raise NotImplementedError

FROM_EMAIL  = "#####"
FROM_PWD    = "#####"

def read_email_from_gmail(_email, _password):
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
        mail.login(_email, _password)
        print(mail.select('"[Gmail]/All Mail"'))
        rv, mailboxes = mail.list()
        

        # type, data = mail.search(None, 'HEADER Subject "RamCity Pty Ltd Order Receipt"')
        type, data = mail.search(None, r'X-GM-RAW "subject:(RamCity Pty Ltd Order Receipt#) has:attachment"')
        # type, data = mail.search(None, 'ALL')
        
        mail_ids = data[0]

        id_list = mail_ids.split()   
        print(len(id_list))
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        count = 0
        for id in range(latest_email_id,first_email_id, -1):
            typ, data = mail.fetch(str(id), '(RFC822)' )

            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1].decode())

                    email_subject = msg['Subject']
                    email_from = msg['from']
                    
                    # if msg.is_multipart:
                    #     for payload in msg.get_payload():
                    #         print(payload.get_payload())
                    # else:
                    #     print(msg.get_payload())
                        
                    # print('From : ' + email_from + '\n')
                    print('Subject : ',email_subject)
    except Exception as e:
        print(str(e))

read_email_from_gmail(FROM_EMAIL, FROM_PWD)