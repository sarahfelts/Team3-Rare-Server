from django.db import IntegrityError
from rest_framework.exceptions import AuthenticationFailed
from rareapi.models import RareUser
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has Associated User

    Method arguments:
      request -- The full HTTP request object
    '''
    if 'uid' not in request.data:
        return Response({'error': 'uid is a required field'}, status=400)

    uid = request.data['uid']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    user = RareUser.objects.filter(uid=uid).first()

    # If authentication was successful, respond with their token
    if user is not None:
        data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'bio': user.bio,
            'profile_image_url': user.profile_image_url,
            'email': user.email,
            'created_on': user.created_on,
            'active': user.active,
            'is_staff': user.is_staff,
            'uid': user.uid,
        }
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = { 'valid': False }
        return Response(data)

@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    try:
        # Now save the user info in the user table
        user = RareUser.objects.create(
            first_name=request.data['first_name'],
            last_name=request.data['last_name'],
            bio=request.data['bio'],
            profile_image_url=request.data['profile_image_url'],
            email=request.data['email'],
            created_on=request.data['created_on'],
            active=request.data['active'],
            is_staff=request.data['is_staff'],
            uid=request.data['uid']
        )

        # Return the user info to the client
        data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'bio': user.bio,
            'profile_image_url': user.profile_image_url,
            'email': user.email,
            'created_on': user.created_on,
            'active': user.active,
            'is_staff': user.is_staff,
            'uid': user.uid,
        }
        return Response(data)
    except KeyError:
        data = {'error': 'Required fields are missing'}
        return Response(data, status=400)
    except IntegrityError:
        return Response({'message': 'A user with this username already exists.'}, status=400)
    
    