
                    msg = email.message_from_string(response_part[1].decode())
                    msg = email.message_from_string(response_part[1].decode())
        mail.login(email, password)
    except Exception as e:
# -------------------------------------------------

            typ, data = mail.fetch(str(id), '(RFC822)' )
def read_email(email, password):
    if email.endswith("@gmail.com"):


                    email_from = msg['from']

FROM_EMAIL  = "XXXXXXXXXXXXXX@gmail.com"

                            print(payload.get_payload())
        id_list = mail_ids.split()
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
        mail.login(email, password)
            typ, data = mail.fetch(str(id), '(RFC822)' )

        type, data = mail.search(None, 'ALL')
                    msg = email.message_from_string(response_part[1].decode())
                    msg = email.message_from_string(response_part[1].decode())
                    print('Subject : ' + email_subject + '\n')

FROM_EMAIL  = "XXXXXXXXXXXXXX@gmail.com"
import imaplib
        type, data = mail.search(None, 'ALL')

            typ, data = mail.fetch(str(id), '(RFC822)' )
                    if msg.is_multipart:

FROM_EMAIL  = "XXXXXXXXXXXXXX@gmail.com"
                    msg = email.message_from_string(response_part[1].decode())
                    email_from = msg['from']
                    email_subject = msg['subject']
                    email_from = msg['from']

        print(str(e))
                            print(payload.get_payload())
        print(str(e))

                    if msg.is_multipart:


                    print('Subject : ' + email_subject + '\n')

    except Exception as e:
        print(str(e))
