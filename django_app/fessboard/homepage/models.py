import django.db.models
from django.db import models


class Companies(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255)
    company_type = models.ForeignKey('CompanyTypes', models.DO_NOTHING, default=None)
    company_sphere = models.ForeignKey('CompanySpheres', models.DO_NOTHING, default=None)
    company_website = models.TextField()
    company_logo = models.CharField(max_length=255)

    class Meta:
        db_table = 'companies'

    def __str__(self):
        return self.company_name


class CompanySpheres(models.Model):
    company_sphere_id = models.AutoField(primary_key=True)
    company_sphere = models.CharField(max_length=255)

    class Meta:
        db_table = 'company_spheres'

    def __str__(self):
        return self.company_sphere


class CompanyTypes(models.Model):
    company_type_id = models.AutoField(primary_key=True)
    company_type = models.CharField(max_length=255)

    class Meta:
        db_table = 'company_types'

    def __str__(self):
        return self.company_type


class Events(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=255)
    event_start_date = models.DateField()
    event_end_date = models.DateField()
    event_description = models.TextField()
    is_frozen = models.IntegerField()
    event_region = models.ForeignKey('Regions', models.DO_NOTHING, default=None)

    class Meta:
        db_table = 'events'

    def __str__(self):
        return self.event_name


class FieldSpheres(models.Model):
    sphere_id = models.AutoField(primary_key=True)
    sphere = models.CharField(max_length=255)

    class Meta:
        db_table = 'field_spheres'

    def __str__(self):
        return self.sphere


class ManagersInEvents(models.Model):
    event = models.ForeignKey(Events, models.DO_NOTHING, default=None)
    student = models.ForeignKey('Students', models.DO_NOTHING, default=None)

    class Meta:
        db_table = 'managers_in_events'


class ParticipantsInEvents(models.Model):
    event = models.ForeignKey(Events, models.DO_NOTHING, default=None)
    student = models.ForeignKey('Students', models.DO_NOTHING, default=None)

    class Meta:
        db_table = 'participants_in_events'


class ProjectFields(models.Model):
    field_id = models.AutoField(primary_key=True)
    field = models.CharField(max_length=255)
    sphere = models.ForeignKey(FieldSpheres, models.DO_NOTHING, default=None)

    class Meta:
        db_table = 'project_fields'

    def __str__(self):
        return self.field


class ProjectGrades(models.Model):
    grade_id = models.AutoField(primary_key=True)
    grade = models.CharField(max_length=255)

    class Meta:
        db_table = 'project_grades'

    def __str__(self):
        return self.grade


class Projects(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=255)
    project_description = models.TextField()
    project_result = models.TextField()
    is_frozen = models.IntegerField()
    project_start_date = models.DateField()
    project_end_date = models.DateField()
    project_grade = models.ForeignKey(ProjectGrades, models.DO_NOTHING, default=None)
    project_field = models.ForeignKey(ProjectFields, models.DO_NOTHING, default=None)
    project_company = models.ForeignKey(Companies, models.DO_NOTHING, default=None)
    project_dateadded = models.DateTimeField(db_column='project_dateAdded', blank=True,
                                             null=True)  # Field name made lowercase.
    project_dateupdated = models.DateTimeField(db_column='project_dateUpdated', blank=True,
                                               null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'projects'

    def __str__(self):
        return self.project_name


class Regions(models.Model):
    region_id = models.AutoField(primary_key=True)
    region = models.CharField(max_length=255)
    is_foreign = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'regions'

    def __str__(self):
        return self.region

class Students(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_surname = models.CharField(max_length=255)
    student_name = models.CharField(max_length=255)
    student_midname = models.CharField(max_length=255)
    bachelors_start_year = models.TextField(blank=True,
                                            null=True)  # This field type is a guess.
    masters_start_year = models.TextField(blank=True,
                                          null=True)  # This field type is a guess.
    bachelors_university = models.ForeignKey('Universities', models.DO_NOTHING, blank=True, null=True)
    masters_university = models.ForeignKey('Universities', models.DO_NOTHING, related_name='mastersuni',blank=True, null=True)
    student_birthday = models.DateField()
    is_banned = models.IntegerField()

    class Meta:
        db_table = 'students'

    def __str__(self):
        return self.student_name + self.student_surname + self.student_midname


class StudentsInProjects(models.Model):
    project = models.ForeignKey(Projects, django.db.models.CASCADE, default=None)
    student = models.ForeignKey(Students, django.db.models.CASCADE, default=None)
    is_curator = models.IntegerField()
    is_moderator = models.IntegerField()
    team = models.SmallIntegerField()

    class Meta:
        db_table = 'students_in_projects'


class Teachers(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    teacher_surname = models.CharField(max_length=255)
    teacher_name = models.CharField(max_length=255)
    teacher_midname = models.CharField(max_length=255)
    teacher_university = models.ForeignKey('Universities', models.DO_NOTHING, blank=True, null=True, default=None)

    class Meta:
        db_table = 'teachers'


class TeachersInEvents(models.Model):
    teacher = models.ForeignKey(Teachers, models.DO_NOTHING, default=None)
    event = models.ForeignKey(Events, models.DO_NOTHING, default=None)

    class Meta:
        db_table = 'teachers_in_events'


class TeachersInProjects(models.Model):
    teacher = models.ForeignKey(Teachers, django.db.models.CASCADE, default=None)
    project = models.ForeignKey(Projects, django.db.models.CASCADE, default=None)

    class Meta:
        db_table = 'teachers_in_projects'


class Universities(models.Model):
    university_id = models.AutoField(primary_key=True)
    university_name = models.CharField(max_length=255)
    university_logo = models.CharField(max_length=255)
    university_region = models.ForeignKey(Regions, models.DO_NOTHING, default=None)

    class Meta:
        db_table = 'universities'