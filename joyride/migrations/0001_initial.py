# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 18:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import positions.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JoyRide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='This will be slugify automatically and will be used as ID for a joy ride', max_length=50, unique=True, verbose_name='Joy Ride Name')),
                ('url_path', models.CharField(blank=True, help_text='The url e.g. /about/ or url regex /abc/\\d+/ of the page on which this joyride will be activated.         If left blank joyride will be activated on global scope', max_length=255, null=True, verbose_name='Page URL')),
                ('slug', models.SlugField(editable=False)),
                ('tipLocation', models.CharField(choices=[('top', 'top'), ('bottom', 'bottom'), ('right', 'right'), ('left', 'left')], default='bottom', help_text='"top" or "bottom" in relation to parent', max_length=10)),
                ('nubPosition', models.CharField(default='auto', help_text='Override on a per tooltip bases', max_length=10)),
                ('scroll', models.BooleanField(default=True, help_text='Whether to scroll to tips')),
                ('scrollSpeed', models.PositiveIntegerField(default=300, help_text='Page scrolling speed in milliseconds')),
                ('timer', models.PositiveIntegerField(default=0, help_text='0 = no timer , all other numbers = timer in milliseconds')),
                ('autoStart', models.BooleanField(default=False, help_text='true or false - false tour starts when restart called')),
                ('startTimerOnClick', models.BooleanField(default=True, help_text='true or false - true requires clicking the first button start the timer')),
                ('startOffset', models.PositiveIntegerField(default=0, help_text='the index of the tooltip you want to start on (index of the li)')),
                ('nextButton', models.BooleanField(default=True, help_text='true or false to control whether a next button is used')),
                ('tipAnimation', models.CharField(choices=[('pop', 'pop'), ('fade', 'fade')], default='fade', help_text='"pop" or "fade" in each tip', max_length=10)),
                ('tipAnimationFadeSpeed', models.PositiveIntegerField(default=300, help_text='when tipAnimation = "fade" this is speed in milliseconds for the transition')),
                ('cookieMonster', models.BooleanField(default=True, help_text='true or false to control whether cookies are used')),
                ('cookieName', models.CharField(default='joyride', help_text="Name the cookie you'll use", max_length=50)),
                ('cookieDomain', models.CharField(blank=True, help_text='Will this cookie be attached to a domain, ie. ".notableapp.com"', max_length=200, null=True)),
                ('cookiePath', models.CharField(blank=True, help_text='Set to "/" if you want the cookie for the whole website', max_length=255, null=True)),
                ('localStorage', models.BooleanField(default=False, help_text='true or false to control whether localstorage is used')),
                ('localStorageKey', models.CharField(default='joyride', help_text='Keyname in localstorage', max_length=50)),
                ('tipContainer', models.CharField(default='body', help_text='Where will the tip be attached', max_length=100)),
                ('modal', models.BooleanField(default=False, help_text='Whether to cover page with modal during the tour')),
                ('expose', models.BooleanField(default=False, help_text='Whether to expose the elements at each step in the tour (requires modal:true)')),
                ('postExposeCallback', models.CharField(blank=True, help_text='A method to call after an element has been exposed', max_length=100, null=True)),
                ('preRideCallback', models.CharField(blank=True, help_text='A method to call before the tour starts (passed index, tip, and cloned exposed element)', max_length=100, null=True)),
                ('postRideCallback', models.CharField(blank=True, help_text='A method to call once the tour closes (canceled or complete)', max_length=100, null=True)),
                ('preStepCallback', models.CharField(blank=True, help_text='A method to call before each step', max_length=100, null=True)),
                ('postStepCallback', models.CharField(blank=True, help_text='A method to call after each step', max_length=100, null=True)),
                ('showJoyRideElement', models.CharField(blank=True, help_text='A DOM element id or class, a method must be provided in showJoyRideElementOn,         if this is left blank then JoyRide will be shown on page load', max_length=100, null=True)),
                ('showJoyRideElementOn', models.CharField(blank=True, help_text='When to show JoyRide i.e "fous", "click". This must be set if showJoyRideElement is given', max_length=100, null=True)),
                ('destroy', models.CharField(blank=True, help_text='IDs of joyrides which should be destroyed before invoking this joyride e.g. #abc, #cde', max_length=255, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, help_text='Date and Time of when created', verbose_name='Creation Date')),
            ],
            options={
                'verbose_name': 'Joy Ride',
                'verbose_name_plural': 'Joy Rides',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='JoyRideHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewed', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('joyride', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='views', to='joyride.JoyRide')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='joyrides', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Joy Ride History',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='JoyRideSteps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(blank=True, help_text='The step header conent', max_length=255, null=True, verbose_name='Step Header')),
                ('content', models.TextField(help_text='The content for step, can be valid html', max_length=255, verbose_name='Step Content')),
                ('button', models.CharField(default='Next', max_length=50)),
                ('attachId', models.CharField(blank=True, help_text='Attach this step to particular dom element by id', max_length=100, null=True, verbose_name='data-id')),
                ('attachClass', models.CharField(blank=True, help_text='Attach this step to particular dom element by class', max_length=100, null=True, verbose_name='data-class')),
                ('options', models.CharField(blank=True, help_text='Custom attributes related to step which will be used in data-options,         i.e. tipLocation:top;tipAnimation:fade', max_length=255, null=True, verbose_name='Options')),
                ('cssClass', models.CharField(blank=True, help_text='A custom css class name for tip', max_length=50, null=True)),
                ('position', positions.fields.PositionField(default=0)),
                ('joyride', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='joyride.JoyRide')),
            ],
            options={
                'verbose_name': 'Joy Ride Step',
                'verbose_name_plural': 'Joy Ride Steps',
                'ordering': ['position'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='joyridehistory',
            unique_together=set([('joyride', 'user')]),
        ),
    ]
