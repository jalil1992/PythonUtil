import smtplib
import time
import imaplib
FROM_PWD    = "XXXXXXXXXXX"

# -------------------------------------------------
FROM_EMAIL  = "XXXXXXXXXXXXXX@gmail.com"
# ------------------------------------------------
def read_email(email, password):
    if email.endswith("@gmail.com"):
        return read_email_from_gmail(email, password)
    else:
        raise NotImplementedError

FROM_EMAIL  = "XXXXXXXXXXXXXX@gmail.com"
FROM_PWD    = "XXXXXXXXXXX"

def read_email_from_gmail(email, password):
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
        mail.login(email, password)
        mail.select('inbox')
        id_list = mail_ids.split()
        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])


        for id in range(latest_email_id,first_email_id, -1):
            typ, data = mail.fetch(str(id), '(RFC822)' )

            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1].decode())
        return read_email_from_gmail(email, password)
                    email_subject = msg['subject']
                    email_from = msg['from']

                    if msg.is_multipart:
FROM_EMAIL  = "XXXXXXXXXXXXXX@gmail.com"
                            print(payload.get_payload())
    except Exception as e:
                        print(msg.get_payload())

                    print('From : ' + email_from + '\n')
                    print('Subject : ' + email_subject + '\n')

    except Exception as e:
        print(str(e))

read_email_from_gmail()