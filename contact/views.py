from django.shortcuts import redirect, render
from django.core.mail import send_mail
import phone_field
from .models import Contact, Enroll
from django.contrib.auth.models import User
from django.contrib import messages


def index(request):
    """
    Display contact page

    **Context**

    ``contact``
        An instance of :model:`contact.index`

    **Template**

    :template:`pages/contact.html`

    """
    if request.method == 'POST':
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        message = request.POST.get('message')
        # num = int(number)
        try:
            if name == '' or email == '' or message == '' or number == '':
                messages.error(
                    request, 'Some of the Field is Empty please check the field before you submit')
                return redirect('contact')
            elif len(number) < 10 or len(number) > 10:
                messages.error(
                    request, 'Phone Number should be 10 Digit Number')
                return redirect('contact')
            else:
                try:
                    num = int(number)
                    user = Contact.objects.create(
                        full_name=name, email=email, phone=number, message=message)
                    messages.success(
                        request, 'Thank you for give your time to share your information')
                    user.save()
                    return redirect('contact')
                except:
                    messages.error(
                        request, 'Phone Number should be 10 Digit Number')
                    return redirect('contact')
        except (number.DoesNotexit) as e:
            return render(request, 'pages/contact.html')
    else:
        return render(request, 'pages/contact.html')


def enroll(request):

    if request.method == 'POST':
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        qualification = request.POST.get('qualification')
        course_complete = request.POST.get('course_complete')
        gpa = request.POST.get('gpa')
        institution = request.POST.get('institution')
        parent_name = request.POST.get('parent_name')
        address = request.POST.get('address')
        courses = request.POST.get('courses')
        scores = request.POST.get('scores')
        planning = request.POST.get('planning')
        where_to_study = request.POST.get('where_to_study')
        preferred_course = request.POST.get('preferred_course')
        preferred_uni = request.POST.get('preferred_uni')
        declare = request.POST.get('declare')
        future_use = request.POST.get('future_use')
        consult_date = request.POST.get('consult')
        know_us = request.POST.get('know_us')
        try:

            if name == '' or email == '' or number == '' or qualification == '' or course_complete == '' or gpa == '' or institution == '' or parent_name == '' or address == '' or courses == '' or where_to_study == '' or preferred_course == '' or preferred_uni == '' or declare == '' or consult_date == '' or know_us == '' or future_use == '':
                messages.error(
                    request, 'Some of the Field is Empty please check the field before you submit')
                return redirect('enroll')
            elif len(number) < 10 or len(number) > 10:
                messages.error(
                    request, 'Phone Number should be 10 Digit Number')
                return redirect('enroll')
            else:
                try:
                    user = Enroll.objects.create(
                        full_name=name, email=email, phone=number, qualification=qualification, course_completed=course_complete, GPA=gpa, institution_name=institution, parents_Name=parent_name, address=address, courses=courses, scores=scores, planning_to_take_test=planning, where_to_study=where_to_study, preferred_course=preferred_course, preferred_uni=preferred_uni, declare_to_use_information=declare, can_use_details=future_use,
                        consult_date=consult_date, how_do_you_know_us=know_us
                    )
                    messages.success(
                        request, 'Thank you for give your time to share your information')
                    user.save()
                    return redirect('enroll')
                except:
                    messages.error(
                        request, 'Phone Number should be 10 Digit Number')
                    return redirect('contact')
        except(number.DoesNotexit) as e:
            return render(request, 'pages/enroll.html')
    else:
        return render(request, 'pages/enroll.html')
