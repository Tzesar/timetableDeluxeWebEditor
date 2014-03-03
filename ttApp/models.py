from django.db import models

# Create your models here.
# GLOBAL_ID format XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX

class TIMETABLE(models.Model):
    _id = models.AutoField(primary_key=True)
    GLOBAL_ID = models.CharField(max_length=29)
    NAME = models.CharField(max_length=30)
    VALID_FROM = models.IntegerField()
    VALID_UNTIL = models.IntegerField()
    DEFAULT_LENGTH = models.IntegerField()

    def __unicode__(self):
        return self.NAME

    class Meta:
        db_table = 'TIMETABLE'

class TEACHER(models.Model):
    _id = models.AutoField(primary_key=True)
    GLOBAL_ID = models.CharField(max_length=36)
    NAME = models.CharField(max_length=30)
    MAIL = models.CharField(max_length=30)

    def __unicode__(self):
        return self.NAME

    class Meta:
        db_table = 'TEACHER'

class SUBJECT(models.Model):
    _id = models.AutoField(primary_key=True)
    GLOBAL_ID = models.CharField(max_length=36)
    NAME = models.CharField(max_length=30)
    SHORT_NAME = models.CharField(max_length=5)
    COLOR = models.IntegerField()
    TEACHER_ID = models.ForeignKey(TEACHER)
    URL = models.CharField(max_length=30, blank=True)
    NOTE = models.CharField(max_length=30, blank=True)

    def __unicode__(self):
        return self.NAME

    class Meta:
        db_table = 'SUBJECT'

class TASK(models.Model):
    _id = models.AutoField(primary_key=True)
    GLOBAL_ID = models.CharField(max_length=29)
    NAME = models.CharField(max_length=30)
    IS_DONE = models.IntegerField()
    DESCRIPTION = models.TextField()
    SUBJECT_ID = models.ForeignKey(SUBJECT)
    PRIORITY = models.IntegerField()
    DUE_UNTIL = models.IntegerField()

    def __unicode__(self):
        return self.NAME

    class Meta:
        db_table = 'TASK'

class HOLIDAY(models.Model):
    _id = models.AutoField(primary_key=True)
    GLOBAL_ID = models.CharField(max_length=36)
    NAME = models.CharField(max_length=30)
    MICRO_TIME_FROM = models.IntegerField()
    MICRO_TIME_TO = models.IntegerField()

    def __unicode__(self):
        return self.NAME

    class Meta:
        db_table = 'HOLIDAY'

# class AUDIT_TRAIL(models.Model):
#     _id = models.AutoField(primary_key=True)
#     CHANGE_TIME = models.IntegerField()
#     GLOBAL_ID = models.CharField(max_length=29)
#     NAME = models.CharField(max_length=30)
#     SHORT_NAME = models.CharField(max_length=30)
#     TEACHER_ID = models.IntegerField()
#     URL = models.CharField(max_length=30)
#     NOTE = models.CharField(max_length=30)
#
#     def __unicode__(self):
#         return self.NAME
#
#     class Meta:
#         db_table = 'AUDIT_TRAIL'

class LESSON_TYPE(models.Model):
    _id = models.AutoField(primary_key=True)
    GLOBAL_ID = models.CharField(max_length=36)
    NAME = models.CharField(max_length=30)

    def __unicode__(self):
        return self.NAME

    class Meta:
        db_table = 'LESSON_TYPE'

class LOCATION(models.Model):
    _id = models.AutoField(primary_key=True)
    GLOBAL_ID = models.CharField(max_length=36)
    NAME = models.CharField(max_length=30)

    def __unicode__(self):
        return self.NAME

    class Meta:
        db_table = 'LOCATION'

class LESSON(models.Model):
    _id = models.AutoField(primary_key=True)
    GLOBAL_ID = models.CharField(max_length=36)
    NAME = models.CharField(max_length=30)
    TIMETABLE_ID = models.ForeignKey(TIMETABLE)
    SUBJECT_ID = models.ForeignKey(SUBJECT)
    DAY_ID = models.IntegerField()
    # START_TIME and END_TIME measured in seconds from 00:00 to 23:59
    START_TIME = models.IntegerField()
    END_TIME = models.IntegerField()
    VALID_FROM = models.IntegerField()
    VALID_TO = models.IntegerField()
    WEEK_ID = models.IntegerField()
    NOTE = models.CharField(max_length=30)
    TEACHER_ID = models.ForeignKey(TEACHER)
    LOCATION_ID = models.ForeignKey(LOCATION)
    TYPE_ID = models.ForeignKey(LESSON_TYPE)

    def __unicode__(self):
        return self.NAME

    class Meta:
        db_table = 'LESSON'

class EXAM_TYPE(models.Model):
    _id = models.AutoField(primary_key=True)
    GLOBAL_ID = models.CharField(max_length=36)
    NAME = models.CharField(max_length=30)

    def __unicode__(self):
        return self.NAME

    class Meta:
        db_table = 'EXAM_TYPE'

class EXAM_GROUP(models.Model):
    _id = models.AutoField(primary_key=True)
    GLOBAL_ID = models.CharField(max_length=36)
    NAME = models.CharField(max_length=30)

    def __unicode__(self):
        return self.NAME

    class Meta:
        db_table = 'EXAM_GROUP'

class EXAM(models.Model):
    _id = models.AutoField(primary_key=True)
    GLOBAL_ID = models.CharField(max_length=36)
    TIME_MILLIS = models.IntegerField()
    SUBJECT_ID = models.ForeignKey(SUBJECT)
    TIMETABLE_ID = models.ForeignKey(TIMETABLE)
    NAME = models.CharField(max_length=30)
    GRADE = models.FloatField()
    WEIGHT = models.FloatField()
    NOTE = models.CharField(max_length=30)
    PASSED = models.IntegerField()
    TYPE_ID = models.ForeignKey(EXAM_TYPE)
    GROUP_ID = models.ForeignKey(EXAM_GROUP)

    def __unicode__(self):
        return self.NAME

    class Meta:
        db_table = 'EXAM'