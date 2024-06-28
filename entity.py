import companies as cp
import first_names as fn
import job_titles as jt
import last_names as ln
import random

def get_entity():
	name = get_name()
	employer = get_employer()
	job_title = get_job_title()
	email = get_email(name, employer[1])
	print(email)


def get_name():
	first = random.choice(fn.first_names)
	last = random.choice(ln.last_names)
	middle = None
	#random chance for middle name or initial?
	if random.uniform(1, 10) < 2:
		middle = random.choice(fn.first_names)

	return [first,middle,last]

def get_employer():
	cn = random.choice(list(cp.companies.keys()))
	return cn, cp.companies[cn]

def get_job_title():
	return random.choice(jt.job_titles)

def get_email(name, employer_details):
	#possible formats:
	#first.last@domain.com, firstinitial lastname@domain.com, etc..
	#first.middle initial.last@domain.com, first lastinitial@domain.com
	return "{}.{}@{}".format(name[0], name[2], employer_details[0]).lower()

get_entity()