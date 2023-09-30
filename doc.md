# documentation

## users => models.py

### class User(AbstractUser):
The Django’s built-in authentication system is great.
For the most part we can use it out-of-the-box,
saving a lot of development and testing effort.
It fits most of the use cases and is very safe.
But in our case we needed to extend the default Django User Model.
there are four different ways to extend the existing User model:  

1. [Using a Proxy Model](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#proxy)
2. [Using One-To-One Link With a User Model](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone)
3. [Creating a Custom User Model Extending AbstractBaseUser](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#abstractbaseuser)
4. [Creating a Custom User Model Extending AbstractUser](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#abstractuser)

Option 1 simply didn't meet our needs.
Option 3 is the most manual way and is just too much work that wasn't necessary.
The debate was between option 4 and 2. In the end we decided to go with option 4.
And that's how User class end up to be a subclass of Django's AbstractUser.
It represents a user of the system and extends the built-in authentication system with additional fields.
It adds an email field, phone_number field, and a one-to-one relationship with the Wallet model.
The save() method is overridden to automatically create a wallet for
the user if one doesn't exist when the user is saved.

### class Wallet(models.Model):
The Wallet class represents a user's wallet and contains a method called balance().
This method calculates the balance of the wallet by summing the total amount received and total amount paid by the wallet.

### class Payment(models.Model):
The Payment class represents a financial transaction between two wallets.
It has fields for the payer (the wallet making the payment),
the receiver (the wallet receiving the payment), and the amount of the payment.

### class Event(models.Model):
The Event class represents an event and has fields for the title of the event,
a one-to-one relationship with the Wallet model (for event-specific transactions),
an owner field representing the User who owns the event,
and a many-to-many relationship with User for the event staff.
