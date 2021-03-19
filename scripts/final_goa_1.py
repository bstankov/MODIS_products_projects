

import smtplib
import string
import email, smtplib, ssl, csv
from datetime import date
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#==================================================================================================================
def ScriptCompletion(MessageBody):
    today = date.today()
    aday = today.day
    ayear = str(today.year)
    amonth = today.month
    s = ""
    #Compose the email message...
    Sender = 'WF.AWHQ-GIS@gov.ab.ca'
    listReceivers = ['bob.stankovic@gov.ab.ca']
##    listReceivers = ['kevin.keats@gov.ab.ca','bob.stankovic@gov.ab.ca']
    strReceivers = "<" + str(listReceivers) +">, <" +")" + ">"
    #Subject = "DAILY MODIS SNOW COVER MAP: sent %s  see at:%s" %(today, "https://fd88995855cf.ngrok.io")
   # Subject = "DAILY MODIS SNOW COVER MAP: sent %s may be seen at %s: " % (today, "http://6aebe382aa61.ngrok.io/")
    Subject = "DAILY MODIS SNOW COVER MAP: sent %s " % (today)
    body = "A new composite cloud-gap-filled (CGF) Snow Cover product has been uploaded to your servers.\
    For WMB stuff the product may be viewed at:\
           \\GOA\Shared\AF\Wildfire_Geospatial\Data_Repository\MODIS\Snow_and_Ice_Composite\MODIS_TerraAqua_Tiffs\original\
    \n\
    The CGF snow cover product is produced from the daily tiled Terra/Aqua Normalized Difference Snow Index (NDSI).  For an\
    interactive map of a daily NDSI snow cover go to the link in the Subject.\
    Daily gaps in the observations caused by cloud cover are filled by retaining the previous clear day view data in the CGF product.\
    For more information on the metadata see the attachment above.\
    \n\
    \n\
    \n\
    \n\
    \n\
    \n\
    -------------------------------------------\n\
    From:  WF Geomatics Group\n\
    Wildfire  Management  Branch,\n\
    Alberta, Agriculture and Forestry,\n\
    Edmonton, AB\n\
    \n\
    Tel: 780 446 8780"

    Message = """From: <""" + Sender + """>
    To: <""" + strReceivers + """
    Subject: """ + Subject + """

    """ + MessageBody + """
    """
    #*********3************************************
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = Sender
    message["To"] = strReceivers
    message["Subject"] = Subject
    # message["Bcc"] = receiver_email  # Recommended for mass emails
    message.attach(MIMEText(body, "plain"))

    filename = "U:/RS_Task_Workspaces/NDSI/scripts/MODIS_snow_cover_metadata_2021_.pdf"  # In same directory as script
    #filename = "Terra_CFG_Class__20210215.tif"  # In same directory as script
    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)
    # Add header as key/value pair to attachment part
    part.add_header("Content-Disposition", f"attachment; filename= {filename}", )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()
    #**************************************
    # Send the email...

    with smtplib.SMTP('goamail.gov.ab.ca') as server:
        with open("U:/RS_Task_Workspaces/NDSI/scripts/receipient_B.csv") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for name, email in reader:
                message["To"] = email
                server.sendmail(Sender, email, text)

            print("Successfully sent email")


# This is used for calling the function...
if __name__ == '__main__':

    ScriptCompletion("This is the msg body\nand this is on another line.\nAnd so is this\n")







