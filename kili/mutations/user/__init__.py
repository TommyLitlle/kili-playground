from ...helpers import format_result
from .queries import (GQL_CREATE_USER,
                      GQL_CREATE_USER_FROM_EMAIL_IF_NOT_EXISTS,
                      GQL_RESET_PASSWORD, GQL_SIGN_IN, GQL_UPDATE_PASSWORD,
                      GQL_UPDATE_PROPERTIES_IN_USER)


class MutationsUser:

    def __init__(self, auth):
        """
        Initializes the subclass

        Parameters
        ----------
        - auth : KiliAuth object
        """
        self.auth = auth

    def signin(self, email: str, password: str):
        """
        Sign in

        Parameters
        ----------
        - email : str
        - password : str

        Returns
        -------
        - a result object which indicates if the mutation was successful, or an error message else.
        """
        variables = {'email': email, 'password': password}
        result = self.auth.client.execute(GQL_SIGN_IN, variables)
        return format_result('data', result)


    def create_user(self, name: str, email: str, password: str, organization_role: str):
        """
        Add a user to your organization.

        Parameters
        ----------
        - name : str
            Name of the new user.
        - email : str
            Email of the new user, used as his unique identifier.
        - password : str
            On the first sign in, he will use this password and be able to change it.
        - organization_role : str
            One of "ADMIN", "USER".

        Returns
        -------
        - a result object which indicates if the mutation was successful, or an error message else.
        """
        variables = {
            'name': name,
            'email': email,
            'password': password,
            'organizationRole': organization_role
        }
        result = self.auth.client.execute(GQL_CREATE_USER, variables)
        return format_result('data', result)


    def create_user_from_email_if_not_exists(self, name: str, email: str, organization_role: str, project_id: str):
        """
        Create a user for a given project

        Parameters
        ----------
        - name : str
        - email : str
        - organization_role : str
            One of "ADMIN", "REVIEWER", "LABELER", "READER"
        - project_id : str

        Returns
        -------
        - a result object which indicates if the mutation was successful, or an error message else.
        """
        variables = {
            'name': name,
            'email': email,
            'organizationRole': organization_role,
            'projectID': project_id
        }
        result = self.auth.client.execute(
            GQL_CREATE_USER_FROM_EMAIL_IF_NOT_EXISTS, variables)
        return format_result('data', result)


    def update_password(self, email: str, old_password: str, new_password_1: str, new_password_2: str):
        """
        Update password

        Parameters
        ----------
        - email : str
        - old_password : str
        - new_password_1 : str
        - new_password_2 : str

        Returns
        -------
        - a result object which indicates if the mutation was successful, or an error message else.
        """
        variables = {
            'email': email,
            'oldPassword': old_password,
            'newPassword1': new_password_1,
            'newPassword2': new_password_2
        }
        result = self.auth.client.execute(GQL_UPDATE_PASSWORD, variables)
        return format_result('data', result)


    def reset_password(self, email: str):
        """
        Reset password

        Parameters
        ----------
        - email : str

        Returns
        -------
        - a result object which indicates if the mutation was successful, or an error message else.
        """
        variables = {'email': email}
        result = self.auth.client.execute(GQL_RESET_PASSWORD, variables)
        return format_result('data', result)


    def update_properties_in_user(self, email: str, name: str = None, organization_id: str = None, organization_role: str = None, activated: bool = None):
        """
        Update the properties of a user

        Parameters
        ----------
        - email : str
            The email is the identifier of the user
        - name : str, optional (default = None)
        - organization_id : str, optional (default = None)
            Change the organization the user is related to.
        - organization_role : str, optional (default = None)
            Change the role of the user. One of "ADMIN", "REVIEWER", "LABELER", "READER".
        - activated : bool, optional (default = None)
            In case we want to deactivate a user, but keep it.

        Returns
        -------
        - a result object which indicates if the mutation was successful, or an error message else.
        """
        variables = {
            'email': email,
            'name': name,
            'organizationId': organization_id,
            'organizationRole': organization_role,
            'activated': activated
        }
        result = self.auth.client.execute(GQL_UPDATE_PROPERTIES_IN_USER, variables)
        return format_result('data', result)


def signin(client, email: str, password: str):
    """
    Sign in

    Parameters
    ----------
    - client : GraphQLClient object
    - email : str
    - password : str

    Returns
    -------
    - a result object which indicates if the mutation was successful, or an error message else.
    """
    variables = {'email': email, 'password': password}
    result = client.execute(GQL_SIGN_IN, variables)
    return format_result('data', result)