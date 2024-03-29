# Generated by Django 3.0.5 on 2020-04-11 07:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Communities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community_name', models.CharField(max_length=25, null=True)),
                ('community_bio', models.CharField(max_length=100, null=True)),
                ('community_image_icon', models.FileField(default='/community_icons/default_community_icon.jpg', null=True, upload_to='community_icons')),
                ('community_created_time', models.DateTimeField(auto_now_add=True)),
                ('community_slug', models.SlugField(max_length=40, unique=True)),
                ('user_created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Communities',
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_header', models.CharField(max_length=50, null=True)),
                ('post_content', models.CharField(max_length=180, null=True)),
                ('post_pic', models.FileField(blank=True, default='', upload_to='post_pics')),
                ('time_posted', models.DateTimeField(auto_now_add=True)),
                ('post_slug', models.SlugField(max_length=40, unique=True)),
                ('community', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Post.Communities')),
                ('user_posted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='User_Posted_By', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=180, null=True)),
                ('comment_pic', models.FileField(blank=True, default='', upload_to='post_pics/comment_pics')),
                ('time_commented', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='Post.Comments')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Comment', to='Post.Posts')),
                ('user_commented_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_comment', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
