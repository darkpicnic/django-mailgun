import requests
import app_settings

def api(call_type, method='GET', *args, **kwargs):

	data   = kwargs.get('data', None)
	
	if method.upper() == 'POST':
		r = requests.\
			post((app_settings.MAILGUN_URL + call_type),
				 auth=("api", app_settings.MAILGUN_KEY),
				 data=data
				 )
	
	elif method.upper() == 'GET':
		r = requests.\
			get((app_settings.MAILGUN_URL + call_type),
				 auth=("api", app_settings.MAILGUN_KEY),
				 data=data
				 )

	return r


def send_mail(emails, *args, **kwargs):

	if not emails:
		return False

	subject    = kwargs.get('subject', '')
	body_text  = kwargs.get('text', None)
	body_html  = kwargs.get('html', None)
	from_email = kwargs.get('from', app_settings.FROM_EMAIL)

	if isinstance(emails, basestring):
		target_email_string = emails
	else:
		target_email_string = ', '.join(target_emails)

	if not body_text and not body_html:
		return False

	if app_settings.DEBUG_MODE:
		# Prepend DEBUG to subject, body
		subject = "**DEBUG** :: %s" % subject

		# Just email admins if in debug mode
		emails = [email for name,email in app_settings.ADMINS]

	data = {
		 "from": from_email,
		 "to": emails,
		 "subject": subject,
	}

	if body_text is not None:
		if app_settings.DEBUG_MODE:
			body_text    = "**DEBUG ~ Message originally for %s**\r\n%s" % (target_email_string, body_text)
		data['text'] = body_text

	if body_html is not None:
		if app_settings.DEBUG_MODE:
			body_html = "<p><strong>**DEBUG ~ Message originally for %s**</strong></p>%s" % (target_email_string, body_html)
		data['html'] = body_html

	r = api(app_settings.MAILGUN_APP + "/messages", 'POST', data=data)

	resp = True if r.status_code == requests.codes.ok else False
	return resp


def remove_email_from_list(email, list_address, *args, **kwargs):
	
	r = api("lists/" + list_address + "/members/" + email, "POST")
	resp = True if r.status_code == requests.codes.ok else False
	return resp


def add_email_to_list(email, list_address, *args, **kwargs):

	data = { 'address' : email }
	name = kwargs.get('name', None)
	if name is not None:
		data['name'] = name

	create_list(list_address)
	r = api("lists/" + list_address + "/members", "POST", data=data)

	resp = True if r.status_code == requests.codes.ok else False
	return resp
	

def create_list(address, *args, **kwargs):
	r = api("lists", "POST", data={'address' : address})
	resp = True if r.status_code == requests.codes.ok else False
	return resp


def email_list(list_id, *args, **kwargs):
	pass