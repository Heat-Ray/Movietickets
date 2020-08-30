from django.db import models
from django.core.exceptions import ValidationError


def small_username(name):
    if len(name) < 4:
        raise ValidationError(('%(name)s is smaller than 4 characters'), params={'name' : name})
    if not name.isalnum():
        raise ValidationError(('%(name)s is not alphanumeric'), params={'name' : name})
    return name

def small_phonenum(number):
    valid_chars = [0,1,2,3,4,5,6,7,8,9]
    if len(number) < 7:
        raise ValidationError(('%(number)s is smaller than 7 digits'), params={'number' : number})
    if (number[0] is not '+') and (int(number[0]) not in valid_chars):
        '''print(number)'''
        raise ValidationError(('%(number)s is invalid'), params={'number' : number})
    for i in range(1, len(number)):
        if int(number[i]) not in valid_chars:
            raise ValidationError(('%(number)s is invalid'), params={'number' : number})
    return number

def validate_date(date):
    if date == None:
        raise ValidationError(('Date is invalid'))
    return date

def validate_time(time):
    if time == None:
        raise ValidationError(('Time is invalid'))
    return time



class Booking(models.Model):
    ticket_id = models.AutoField(primary_key = True)
    user_name = models.CharField(max_length = 40, validators=[small_username])
    phone_number = models.CharField(max_length = 13, validators=[small_phonenum])
    date = models.DateField(null=True, validators=[validate_date])
    time = models.TimeField(null=True, validators=[validate_time])
    status = models.IntegerField(default=1)


