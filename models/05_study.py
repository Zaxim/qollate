#Information associated with a study

db.define_table('study',
	Field('name', notnull=True),
	Field('short_description', 'text'),
	format='%(name)s')

db.define_table('participant',
	Field('participant_alias'),
	Field('auth_user', 'reference auth_user'),
	Field('study', 'reference study'),
	Field('isConsented', 'boolean', default=False),
	format='%(participant_alias)s'
	)

db.define_table('qstatement',
	Field('name', notnull=True),
	Field('participant', 'reference participant'),
	Field('study', 'reference study'),
	Field('short_description', 'text'),
	Field('long_description', 'text'),
	Field('isShow', 'boolean', default=True),
	Field('modified', 'datetime'),
	format='%(name)s')

db.define_table('q_answer',
	Field('qstatement' 'reference qstatement'),
	Field('participant', 'reference participant'),
	Field('ranking', 'integer')
	)