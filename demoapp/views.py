from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from .models import Register
from django.core.mail import send_mail

def register(request):
    if request.method == "POST":
        # Fetching form data from the POST request
        username = request.POST.get('username')
        uemail = request.POST.get('uemail')
        upassword = request.POST.get('upassword')

        # Check if all fields are provided
        if not username or not uemail or not upassword:
            messages.error(request, "All fields are required!")
            return render(request, 'register.html')

        # Check if email already exists
        if Register.objects.filter(uemail=uemail).exists():
            messages.error(request, "A user with this email already exists!")
            return render(request, 'register.html')

        # Hash the password before saving it to the database
        hashed_password = make_password(upassword)

        # Save user information to the Register model
        new_register = Register(username=username, uemail=uemail, upassword=hashed_password)
        new_register.save()

        # Send confirmation email from the user's email
        try:
            send_self_email(
                subject="Welcome to our platform!",
                message=f"Hello {username},\n\nfuck youuuuuuuuuuuuu!!!!! ik how to do this hahaha.",
                from_email=uemail,  # User's email as the "from email"
                recipient_list=[uemail],  # Replace with actual recipient email
            )
            messages.success(request, "User registered successfully! A confirmation email has been sent.")
        except Exception as e:
            messages.error(request, f"User registered but failed to send confirmation email: {e}")

        return redirect('login')

    return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        upassword = request.POST.get('upassword')

        if not username or not upassword:
            messages.error(request, "All fields are required.")
            return render(request, 'login.html')

        try:
            # Fetch the user from the Register model
            user = Register.objects.get(username=username)

            # Check if the provided password matches the stored hashed password
            if check_password(upassword, user.upassword):
                # Password matches, set session and redirect
                request.session['user_id'] = user.id
                messages.success(request, "Login successful! Redirecting to dashboard...")
                return redirect('dashboard')  # Replace 'dashboard' with your actual URL pattern name
            else:
                # Incorrect password
                messages.error(request, "Invalid password. Please try again.")
        except Register.DoesNotExist:
            # User not found
            messages.error(request, "User not found. Please check the username.")

    return render(request, 'login.html')


def home(request):
    if 'user_id' not in request.session:
        # If user is not logged in, redirect to login page
        return redirect('login')

    try:
        # Fetch the user from the Register model using the user_id in the session
        user = Register.objects.get(id=request.session['user_id'])
    except Register.DoesNotExist:
        # If user ID does not exist, clear session and redirect to login
        del request.session['user_id']
        return redirect('login')

    # Pass the user object to the template
    return render(request, 'dashboard.html', {'user': user})


def user_logout(request):
    # Clear session data
    request.session.flush()
    messages.success(request, "Logged out successfully.")
    return redirect('login')


def admindash(request):
    return render(request, 'admin.html')


def send_self_email(subject, message, from_email, recipient_list):
    """
    Function to send an email.
    """
    try:
        send_mail(
            subject=subject,  # Email subject
            message=message,  # Email message
            from_email=from_email,  # Sender's email (user's email)
            recipient_list=recipient_list,  # Recipient email(s)
        )
    except Exception as e:
        raise Exception(f"Failed to send email: {e}")
