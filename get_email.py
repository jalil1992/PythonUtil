FROM_EMAIL  = "XXXXXXXXXXXXXX@gmail.com"


            typ, data = mail.fetch(str(id), '(RFC822)' )

# -------------------------------------------------

# ------------------------------------------------
def read_email(email, password):
    if email.endswith("@gmail.com"):

            typ, data = mail.fetch(str(id), '(RFC822)' )
            typ, data = mail.fetch(str(id), '(RFC822)' )

FROM_EMAIL  = "XXXXXXXXXXXXXX@gmail.com"


        id_list = mail_ids.split()
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
        mail.login(email, password)
            typ, data = mail.fetch(str(id), '(RFC822)' )
                if isinstance(response_part, tuple):
        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]
        first_email_id = int(id_list[0])
        id_list = mail_ids.split()

FROM_EMAIL  = "XXXXXXXXXXXXXX@gmail.com"
import imaplib

        for id in range(latest_email_id,first_email_id, -1):
            typ, data = mail.fetch(str(id), '(RFC822)' )
                    if msg.is_multipart:
            for response_part in data:
# ------------------------------------------------
                    msg = email.message_from_string(response_part[1].decode())
        return read_email_from_gmail(email, password)
                    email_subject = msg['subject']
                    email_from = msg['from']

            typ, data = mail.fetch(str(id), '(RFC822)' )
                            print(payload.get_payload())
                            print(payload.get_payload())
    except Exception as e:
                        print(msg.get_payload())

        id_list = mail_ids.split()
                    print('Subject : ' + email_subject + '\n')

    except Exception as e:
        print(str(e))

read_email_from_gmail()