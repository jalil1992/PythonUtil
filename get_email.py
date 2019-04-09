FROM_EMAIL  = "XXXXXXXXXXXXXX@gmail.com"

                    msg = email.message_from_string(response_part[1].decode())
            typ, data = mail.fetch(str(id), '(RFC822)' )

# -------------------------------------------------

            typ, data = mail.fetch(str(id), '(RFC822)' )
def read_email(email, password):
    if email.endswith("@gmail.com"):


                    msg = email.message_from_string(response_part[1].decode())

FROM_EMAIL  = "XXXXXXXXXXXXXX@gmail.com"


        id_list = mail_ids.split()
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
        mail.login(email, password)
            typ, data = mail.fetch(str(id), '(RFC822)' )

        type, data = mail.search(None, 'ALL')
                    msg = email.message_from_string(response_part[1].decode())
        first_email_id = int(id_list[0])
                    print('Subject : ' + email_subject + '\n')

FROM_EMAIL  = "XXXXXXXXXXXXXX@gmail.com"
import imaplib
        type, data = mail.search(None, 'ALL')
        for id in range(latest_email_id,first_email_id, -1):
            typ, data = mail.fetch(str(id), '(RFC822)' )
                    if msg.is_multipart:


                    msg = email.message_from_string(response_part[1].decode())
        id_list = mail_ids.split()
                    email_subject = msg['subject']
                    email_from = msg['from']

        print(str(e))
                            print(payload.get_payload())
                            print(payload.get_payload())
    except Exception as e:
                    if msg.is_multipart:

        id_list = mail_ids.split()
                    print('Subject : ' + email_subject + '\n')

    except Exception as e:
        print(str(e))

