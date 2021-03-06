class Document:
    _id = None


class Person(Document):
    name = None
    birthdate = None


class ProfileData(Document):
    type_id = None
    person_id = None
    fields_values = {}  # field id to value


class ProfileType(Document):
    fields = []  # of Field


class Field(Document):  # abstract
    name = None
    type = None


class TextField(Field):
    type = 'Text'


class DateField(Field):
    type = 'Date'


class OptionsField(Field):
    type = 'Options'
    possible_values = []

class AllTask:
    _id = None
    name = None

class PersonTasks:
    person_id = None
    task_id = None

class RelatedTasksGroupsAggregationPerProfile:
    profile_id = None
    tasks_group_id = None
    count = None

class RelatedTasksGroups(Document):
    task_id = None

class RelatedTasksGroupsAggregationPerProfile:
    profile_id = None
    tasks_group_id = None
    count = None

class RelatedTasksGroups(Document):
    task_id = None
