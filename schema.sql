# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AppNewsletter(models.Model):
    email = models.CharField(unique=True, max_length=254)
    activate = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'app_newsletter'


class AppPartner(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=100)
    info = models.TextField()

    class Meta:
        managed = False
        db_table = 'app_partner'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MaterialAcademicevent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_type = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    is_important = models.BooleanField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'material_academicevent'


class MaterialAnnouncement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_active = models.BooleanField()
    priority = models.CharField(max_length=10)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING)
    image = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'material_announcement'


class MaterialBlog(models.Model):
    body = models.TextField()
    author = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'material_blog'


class MaterialBulletin(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'material_bulletin'


class MaterialComment(models.Model):
    body = models.TextField()
    author = models.ForeignKey(AuthUser, models.DO_NOTHING)
    blog = models.ForeignKey(MaterialBlog, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'material_comment'


class MaterialCommentReply(models.Model):
    from_comment = models.ForeignKey(MaterialComment, models.DO_NOTHING)
    to_comment = models.ForeignKey(MaterialComment, models.DO_NOTHING, related_name='materialcommentreply_to_comment_set')

    class Meta:
        managed = False
        db_table = 'material_comment_reply'
        unique_together = (('from_comment', 'to_comment'),)


class MaterialCourse(models.Model):
    code = models.CharField(max_length=8)
    title = models.CharField(max_length=50)
    info = models.TextField()
    outline = models.CharField(max_length=100, blank=True, null=True)
    level = models.IntegerField()
    department = models.ForeignKey('MaterialDepartment', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'material_course'


class MaterialCoursecomment(models.Model):
    user = models.CharField(max_length=20)
    comment = models.TextField()
    posted_on = models.DateTimeField()
    course = models.ForeignKey(MaterialCourse, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'material_coursecomment'


class MaterialDay(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'material_day'


class MaterialDepartment(models.Model):
    name = models.CharField(max_length=50)
    slogan = models.TextField()
    active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'material_department'


class MaterialDepartmentrepresentative(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    person_phone = models.CharField(max_length=255)
    person_img = models.CharField(max_length=100, blank=True, null=True)
    level = models.IntegerField()
    active = models.BooleanField()
    department = models.ForeignKey(MaterialDepartment, models.DO_NOTHING)
    person = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'material_departmentrepresentative'


class MaterialDepartmentrepresentativeUploadedMaterials(models.Model):
    departmentrepresentative = models.ForeignKey(MaterialDepartmentrepresentative, models.DO_NOTHING)
    material = models.ForeignKey('MaterialMaterial', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'material_departmentrepresentative_uploaded_materials'
        unique_together = (('departmentrepresentative', 'material'),)


class MaterialLecturehour(models.Model):
    venue = models.CharField(max_length=20)
    course = models.ForeignKey(MaterialCourse, models.DO_NOTHING)
    day = models.ForeignKey(MaterialDay, models.DO_NOTHING)
    hour = models.ForeignKey('MaterialTime', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'material_lecturehour'


class MaterialMaterial(models.Model):
    title = models.CharField(max_length=200)
    file = models.CharField(max_length=100)
    comment = models.TextField()
    upload_on = models.DateTimeField()
    course = models.ForeignKey(MaterialCourse, models.DO_NOTHING)
    download_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'material_material'


class MaterialPastquestion(models.Model):
    pq = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    course = models.ForeignKey(MaterialCourse, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'material_pastquestion'


class MaterialRequest(models.Model):
    body = models.TextField()
    topic = models.CharField(max_length=50)
    priority = models.IntegerField()
    type = models.CharField(max_length=15)
    email = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'material_request'


class MaterialTime(models.Model):
    time = models.CharField(max_length=20)
    index = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'material_time'


class MaterialTimetable(models.Model):
    level = models.CharField(max_length=3)
    department = models.ForeignKey(MaterialDepartment, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'material_timetable'


class MaterialTimetableLectures(models.Model):
    timetable = models.ForeignKey(MaterialTimetable, models.DO_NOTHING)
    lecturehour = models.ForeignKey(MaterialLecturehour, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'material_timetable_lectures'
        unique_together = (('timetable', 'lecturehour'),)


class UserAccountAccount(models.Model):
    coins = models.PositiveIntegerField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)
    date_of_birth = models.DateField()
    department = models.ForeignKey(MaterialDepartment, models.DO_NOTHING, blank=True, null=True)
    gender = models.CharField(max_length=1)
    phone_number = models.CharField(max_length=20)
    profile_pic = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_account_account'


class UserAccountFlaggedissue(models.Model):
    response = models.TextField()
    email = models.CharField(max_length=50)
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_account_flaggedissue'
