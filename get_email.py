
                    msg = email.message_from_string(response_part[1].decode())
                    msg = email.message_from_string(response_part[1].decode())
        mail.login(email, password)
                    msg = email.message_from_string(response_part[1].decode())
        mail.login(email, password)
# -------------------------------------------------
        mail.login(email, password)
                    msg = email.message_from_string(response_part[1].decode())
    except Exception as e:


                    email_from = msg['from']

FROM_EMAIL  = "XXXXXXXXXXXXXX@gmail.com"

                            print(payload.get_payload())
    except Exception as e:
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
        mail.login(email, password)
            typ, data = mail.fetch(str(id), '(RFC822)' )


                    msg = email.message_from_string(response_part[1].decode())
                    msg = email.message_from_string(response_part[1].decode())
                    print('Subject : ' + email_subject + '\n')

FROM_EMAIL  = "XXXXXXXXXXXXXX@gmail.com"
import imaplib

            typ, data = mail.fetch(str(id), '(RFC822)' )
            typ, data = mail.fetch(str(id), '(RFC822)' )
                    if msg.is_multipart:
                    msg = email.message_from_string(response_part[1].decode())
FROM_EMAIL  = "XXXXXXXXXXXXXX@gmail.com"
                    msg = email.message_from_string(response_part[1].decode())
                    email_from = msg['from']
                    email_subject = msg['subject']

                            print(payload.get_payload())
        print(str(e))
                            print(payload.get_payload())


                    email_from = msg['from']

            typ, data = mail.fetch(str(id), '(RFC822)' )
                    print('Subject : ' + email_subject + '\n')

    except Exception as e:
                    email_subject = msg['subject']