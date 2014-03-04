from django.db import models
import string
import random

def id_generator(size=32, chars=string.ascii_lowercase + string.digits):
    """

    :param size: integer, indicates the size of the id
    :param chars: strings, the samples to randomly select from
    :return: string randomly generated from chars with size length
    """
    return ''.join(random.choice(chars) for _ in range(size))

# Create your models here.
# GLOBAL_ID format XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX

class TIMETABLE(models.Model):
    _id = models.AutoField(primary_key=True)
    NAME = models.CharField(max_length=30)
    GLOBAL_ID = models.CharField(max_length=36)
    VALID_FROM = models.IntegerField(blank=True)
    VALID_UNTIL = models.IntegerField(blank=True)
    DEFAULT_LENGTH = models.IntegerField(default=45)

    def save(self, *args, **kwargs):
        self.GLOBAL_ID = id_generator()
        super(TIMETABLE, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.NAME

    class Meta:
        db_table = 'TIMETABLE'

class TEACHER(models.Model):
    _id = models.AutoField(primary_key=True)
    GLOBAL_ID = models.CharField(max_length=36)
    NAME = models.CharField(max_length=30)
    MAIL = models.CharField(max_length=30, blank=True)

    def save(self, *args, **kwargs):
        self.GLOBAL_ID = id_generator()
        super(TEACHER, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.NAME

    class Meta:
        db_table = 'TEACHER'

class SUBJECT(models.Model):
    _id = models.AutoField(primary_key=True)
    NAME = models.CharField(max_length=35)
    GLOBAL_ID = models.CharField(max_length=36)
    SHORT_NAME = models.CharField(max_length=5)
    COLOR = models.IntegerField()
    TEACHER_ID = models.ForeignKey(TEACHER, db_column='TEACHER_ID')
    URL = models.CharField(max_length=30, blank=True)
    NOTE = models.CharField(max_length=30, blank=True)

    def __unicode__(self):
        return self.NAME

    def save(self, *args, **kwargs):
        self.GLOBAL_ID = id_generator()
        super(SUBJECT, self).save(*args, **kwargs)

    class Meta:
        db_table = 'SUBJECT'

class TASK(models.Model):
    _id = models.AutoField(primary_key=True)
    GLOBAL_ID = models.CharField(max_length=36)
    NAME = models.CharField(max_length=30)
    IS_DONE = models.IntegerField()
    DESCRIPTION = models.TextField()
    SUBJECT_ID = models.ForeignKey(SUBJECT, db_column='SUBJECT_ID')
    PRIORITY = models.IntegerField()
    DUE_UNTIL = models.IntegerField()

    def __unicode__(self):
        return self.NAME

    def save(self, *args, **kwargs):
        self.GLOBAL_ID = id_generator()
        super(TASK, self).save(*args, **kwargs)

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

    def save(self, *args, **kwargs):
        self.GLOBAL_ID = id_generator()
        super(HOLIDAY, self).save(*args, **kwargs)

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

    def save(self, *args, **kwargs):
        self.GLOBAL_ID = id_generator()
        super(LESSON_TYPE, self).save(*args, **kwargs)

    class Meta:
        db_table = 'LESSON_TYPE'

class LOCATION(models.Model):
    _id = models.AutoField(primary_key=True)
    GLOBAL_ID = models.CharField(max_length=36)
    NAME = models.CharField(max_length=30)

    def __unicode__(self):
        return self.NAME

    def save(self, *args, **kwargs):
        self.GLOBAL_ID = id_generator()
        super(LOCATION, self).save(*args, **kwargs)

    class Meta:
        db_table = 'LOCATION'

class LESSON(models.Model):
    _id = models.AutoField(primary_key=True)
    GLOBAL_ID = models.CharField(max_length=36)
    NAME = models.CharField(max_length=30, default='unknown')
    TIMETABLE_ID = models.ForeignKey(TIMETABLE, db_column='TIMETABLE_ID')
    SUBJECT_ID = models.ForeignKey(SUBJECT, db_column='SUBJECT_ID')
    DAY_ID = models.IntegerField()
    # START_TIME and END_TIME measured in seconds from 00:00 to 23:59
    START_TIME = models.IntegerField()
    END_TIME = models.IntegerField()
    VALID_FROM = models.IntegerField()
    VALID_TO = models.IntegerField()
    WEEK_ID = models.IntegerField()
    NOTE = models.CharField(max_length=30)
    TEACHER_ID = models.ForeignKey(TEACHER, db_column='TEACHER_ID')
    LOCATION_ID = models.ForeignKey(LOCATION, db_column='LOCATION_ID')
    TYPE_ID = models.ForeignKey(LESSON_TYPE, db_column='TYPE_ID')

    def __unicode__(self):
        return self.NAME

    def save(self, *args, **kwargs):
        self.GLOBAL_ID = id_generator()
        super(LESSON, self).save(*args, **kwargs)

    class Meta:
        db_table = 'LESSON'

class EXAM_TYPE(models.Model):
    _id = models.AutoField(primary_key=True)
    GLOBAL_ID = models.CharField(max_length=36)
    NAME = models.CharField(max_length=30)

    def __unicode__(self):
        return self.NAME

    def save(self, *args, **kwargs):
        self.GLOBAL_ID = id_generator()
        super(EXAM_TYPE, self).save(*args, **kwargs)

    class Meta:
        db_table = 'EXAM_TYPE'

class EXAM_GROUP(models.Model):
    _id = models.AutoField(primary_key=True)
    GLOBAL_ID = models.CharField(max_length=36)
    NAME = models.CharField(max_length=30)

    def __unicode__(self):
        return self.NAME

    def save(self, *args, **kwargs):
        self.GLOBAL_ID = id_generator()
        super(EXAM_GROUP, self).save(*args, **kwargs)

    class Meta:
        db_table = 'EXAM_GROUP'

class EXAM(models.Model):
    _id = models.AutoField(primary_key=True)
    GLOBAL_ID = models.CharField(max_length=36)
    TIME_MILLIS = models.IntegerField()
    SUBJECT_ID = models.ForeignKey(SUBJECT, db_column='SUBJECT_ID')
    TIMETABLE_ID = models.ForeignKey(TIMETABLE, db_column='TIMETABLE_ID')
    NAME = models.CharField(max_length=30)
    GRADE = models.FloatField()
    WEIGHT = models.FloatField()
    NOTE = models.CharField(max_length=30)
    PASSED = models.IntegerField()
    TYPE_ID = models.ForeignKey(EXAM_TYPE, db_column='TYPE_ID')
    GROUP_ID = models.ForeignKey(EXAM_GROUP, db_column='GROUP_ID')

    def __unicode__(self):
        return self.NAME

    def save(self, *args, **kwargs):
        self.GLOBAL_ID = id_generator()
        super(EXAM, self).save(*args, **kwargs)

    class Meta:
        db_table = 'EXAM'