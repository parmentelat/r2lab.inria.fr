#!/usr/bin/env python3

from django.contrib.auth.models import User

##################################################
from manifoldapi.manifoldapi import ManifoldException

from .mfdetails import manifold_details

from r2lab.settings import manifold_url as config_manifold_url
from r2lab.settings import logger
from plc.plcsfauser import get_r2lab_user

debug = True

class ManifoldBackend:
    """
    Authenticate against the onelab portal user accounts
    """

    def __init__(self, manifold_url=config_manifold_url):
        self.manifold_url = manifold_url

    # Required for your backend to work properly - unchanged in most scenarios
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    # This is called by the standard Django login procedure
    def authenticate(self, token=None):
        if token is None:
            return

        if debug:
            print("authenticating token={}".format(token))
        try:
            email = token['username']
            password = token['password']
            request = token['request']

            session, auth, user_details = manifold_details(
                self.manifold_url, email, password, logger)
            if session is None or user_details is None:
                if debug:
                    logger.info(
                        "dbg: could not get or missing manifold details")
                return None
            if debug:
                logger.info("dbg: SESSION keys: {}".format(session.keys()))

            # get a more relevant list of slices right at the r2lab portal
            r2lab_user = get_r2lab_user(email)
            if debug:
                logger.info("dbg: r2lab_user = {}".format(r2lab_user))

            if not r2lab_user:
                logger.error("mfbackend.authenticate emergency exit")
                return

            # extend request to save this environment
            # auth and session['expires'] may be of further interest
            # we cannot expose just 'api' because it can't be marshalled in JSON
            # BUT we can expose the 'auth' field
            request.session['r2lab_context'] = {
                'session': session,
                'auth': auth,
                'user_details': user_details,
                'accounts': r2lab_user['accounts'],
                'manifold_url': self.manifold_url,
            }

        except ManifoldException as e:
            logger.error("ManifoldException in Auth Backend: {}"
                         .format(e.manifold_result))
        except Exception as e:
            logger.exception("ERROR in Manifold Auth Backend")
            return None

        try:
            # Check if the user exists in Django's local database
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            logger.info("Creating django user object {}".format(email))
            # Create a user in Django's local database
            # first arg is a name, second an email
            user = User.objects.create_user(
                email, email, 'passworddoesntmatter')

        if 'firstname' in user_details:
            user.first_name = user_details['firstname']
        if 'lastname' in user_details:
            user.last_name = user_details['lastname']

        return user
