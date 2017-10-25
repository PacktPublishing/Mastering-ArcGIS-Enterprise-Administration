import calendar
import datetime
import httplib
import urllib
import json
import sys
import smtplib
from email.MIMEText import MIMEText


def send_email(the_subject, the_message):
    """
    Sends email over SMTP
    :param the_subject: String. Email subject line.
    :param the_message: String. Email message.
    :return: Nothing.
    """
    server = smtplib.SMTP("outlook.office365.com", None)
    server.starttls()
    server.login("slalerts@gisinc.com", "work vegetable met silence")
    msg = MIMEText("\n{0}".format(the_message))
    msg["Subject"] = the_subject
    msg["From"] = "slalerts@gisinc.com"
    msg["To"] = "chad.cooper@gisinc.com"
    server.sendmail("slalerts@gisinc.com", "chad.cooper@gisinc.com", msg.as_string())
    server.quit()


def get_token(username, password, server_name, server_port):
    """
    Generates a short-lived token for a given user and password at the 
    provided URL
    :param username: String. Username.
    :param password: String. Password.
    :param server_name: String. Name of ArcGIS Server machine.
    :param server_port: Integer. Port number, typically 6080.
    :return: String. ArcGIS Server short-lived token.
    """
    # Token URL is typically http://server[:port]/arcgis/admin/generateToken
    token_url = "/arcgis/admin/generateToken"

    # URL-encode the token parameters
    params = urllib.urlencode({'username': username, 'password': password, 'client': 'requestip', 'f': 'json'})

    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

    # Connect to URL and post parameters
    http_conn = httplib.HTTPConnection(server_name, server_port)
    http_conn.request("POST", token_url, params, headers)

    # Read response
    response = http_conn.getresponse()
    data = response.read()
    http_conn.close()

    # Extract the toke from it
    token = json.loads(data)
    return token['token']


def main(argv=None):

    username = "siteadmin"
    password = "somestrongpassword"

    server_name = "localhost"
    server_port = 6080
    logging_level = "SEVERE"

    # Get a token
    token = get_token(username, password, server_name, server_port)

    past = datetime.datetime.utcnow() - datetime.timedelta(hours=24)
    unix_stamp = calendar.timegm(past.timetuple())*1000

    log_query_url = "/arcgis/admin/logs/query"

    # Supply the log level, filter, token, and return format
    params = urllib.urlencode({'endTime': unix_stamp, 'level': logging_level, 'filter': {"codes": []}, 'token': token, 'f': 'json'})

    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

    # Connect to URL and post parameters
    http_conn = httplib.HTTPConnection(server_name, server_port)
    http_conn.request("POST", log_query_url, params, headers)

    # Read response
    response = http_conn.getresponse()

    data = response.read()

    # Deserialize response into Python object
    data_obj = json.loads(data)
    http_conn.close()

    email_body = ""
    email_log_level = logging_level if logging_level == "SEVERE" \
        else "{0} and higher".format(logging_level)

    # Iterate over messages
    if data_obj["logMessages"]:
        for item in data_obj["logMessages"]:
            msg = "{0} @ {1}: {2}".format(
                item["type"],
                datetime.datetime.fromtimestamp(
                    int(item["time"]/1000)
                ).strftime("%Y-%m-%d %H:%M:%S"),
                item["message"]
            )
            print msg
            email_body = "{0}\n{1}".format(
                email_body,
                msg
            )

        email_msg = "The following {0} errors were logged " \
                    "in ArcGIS Server in the last " \
                    "24 hours:\n\n{1}".format(
            email_log_level,
            email_body)
        send_email("ArcGIS Server error report", email_msg)
    else:
        email_msg = "There were no {0} errors logged in " \
                    "ArcGIS Server in the last 24 " \
                    "hours.\n".format(email_log_level)
        send_email("ArcGIS Server error report", email_msg)

    return


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
