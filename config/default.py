"""
Copyright ©2019. The Regents of the University of California (Regents). All Rights Reserved.

Permission to use, copy, modify, and distribute this software and its documentation
for educational, research, and not-for-profit purposes, without fee and without a
signed licensing agreement, is hereby granted, provided that the above copyright
notice, this paragraph and the following two paragraphs appear in all copies,
modifications, and distributions.

Contact The Office of Technology Licensing, UC Berkeley, 2150 Shattuck Avenue,
Suite 510, Berkeley, CA 94720-1620, (510) 643-7201, otl@berkeley.edu,
http://ipira.berkeley.edu/industry-info for commercial licensing opportunities.

IN NO EVENT SHALL REGENTS BE LIABLE TO ANY PARTY FOR DIRECT, INDIRECT, SPECIAL,
INCIDENTAL, OR CONSEQUENTIAL DAMAGES, INCLUDING LOST PROFITS, ARISING OUT OF
THE USE OF THIS SOFTWARE AND ITS DOCUMENTATION, EVEN IF REGENTS HAS BEEN ADVISED
OF THE POSSIBILITY OF SUCH DAMAGE.

REGENTS SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE
SOFTWARE AND ACCOMPANYING DOCUMENTATION, IF ANY, PROVIDED HEREUNDER IS PROVIDED
"AS IS". REGENTS HAS NO OBLIGATION TO PROVIDE MAINTENANCE, SUPPORT, UPDATES,
ENHANCEMENTS, OR MODIFICATIONS.
"""


import logging
import os


# Base directory for the application (one level up from this config file).
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

TIMEZONE = 'America/Los_Angeles'

SQLALCHEMY_DATABASE_URI = 'postgres://nessie:nessie@localhost:5432/nessie'
SQLALCHEMY_TRACK_MODIFICATIONS = False

CAS_SERVER = 'https://auth-test.berkeley.edu/cas/'
CAS_LOGOUT_URL = 'https://auth-test.berkeley.edu/cas/logout'

# Some defaults.
CSRF_ENABLED = True
CSRF_SESSION_KEY = 'secret'
# Used to encrypt session cookie.
SECRET_KEY = 'secret'
# Used to authorize administrative API.
API_USERNAME = 'username'
API_PASSWORD = 'password'
# UIDs of authorized 'Admin' users
AUTHORIZED_USERS = [0000000, 1111111, 2222222]

# Override in local configs.
HOST = '0.0.0.0'
PORT = 1234

# The 'dist' directory is generated by 'npm run build-vue'
INDEX_HTML = 'dist/static/index.html'

AWS_ACCESS_KEY_ID = 'key'
AWS_APP_ROLE_ARN = 'aws:arn::<account>:role/<app_nessie_specific_role>'
AWS_DMS_VPC_ROLE = 'dms vpc role'
AWS_SECRET_ACCESS_KEY = 'secret'
AWS_REGION = 'aws region'

ASC_ATHLETES_API_URL = 'https://secreturl.berkeley.edu/intensives.php?AcadYr=2017-18'
ASC_ATHLETES_API_KEY = 'secret'
ASC_THIS_ACAD_YR = '2017-18'

BOAC_REFRESHERS = [{'API_KEY': 'Regents of the University of California', 'URL': 'https://ets-boac.example.com/api/refresh_me'}]

CAL1CARD_PHOTO_API_URL = 'https://secreturl.berkeley.edu/photos'
CAL1CARD_PHOTO_API_USERNAME = 'secretuser'
CAL1CARD_PHOTO_API_PASSWORD = 'secretpassword'

CANVAS_DATA_API_KEY = 'some key'
CANVAS_DATA_API_SECRET = 'some secret'
CANVAS_DATA_HOST = 'foo.instructure.com'

CANVAS_HTTP_URL = 'https://wottsamatta.instructure.com'
CANVAS_HTTP_TOKEN = 'yet another secret'

CURRENT_TERM = 'Fall 2017'

CYCLICAL_API_IMPORT_BATCH_SIZE = 5000
HIST_ENR_REGISTRATIONS_IMPORT_BATCH_SIZE = 20000

DEGREE_PROGRESS_API_URL = 'https://secreturl.berkeley.edu/PSFT_CS'
DEGREE_PROGRESS_API_USERNAME = 'secretuser'
DEGREE_PROGRESS_API_PASSWORD = 'secretpassword'

EARLIEST_LEGACY_TERM = 'Fall 2001'
EARLIEST_TERM = 'Fall 2016'

ENROLLMENTS_API_ID = 'secretid'
ENROLLMENTS_API_KEY = 'secretkey'
ENROLLMENTS_API_URL = 'https://secreturl.berkeley.edu/enrollments'

FUTURE_TERM = 'Spring 2018'

# True on master node, false on worker nodes.
# Override by embedding "master" or "worker" in the EB_ENVIRONMENT environment variable.
JOB_SCHEDULING_ENABLED = True

# See http://apscheduler.readthedocs.io/en/latest/modules/triggers/cron.html for supported schedule formats.
# Schedules should be provided as dictionaries in configs, e.g. {'hour': 12, 'minute': 30}
JOB_SYNC_CANVAS_SNAPSHOTS = {}
JOB_RESYNC_CANVAS_SNAPSHOTS = {}
JOB_IMPORT_ADVISORS = {}
JOB_IMPORT_CANVAS_ENROLLMENTS = {}
JOB_IMPORT_STUDENT_POPULATION = {}
JOB_IMPORT_DEGREE_PROGRESS = {}
JOB_IMPORT_REGISTRATIONS = {}
JOB_IMPORT_SIS_STUDENTS = {}
JOB_GENERATE_ALL_TABLES = {}
JOB_GENERATE_CANVAS_CALIPER_ANALYTICS = {}
JOB_GENERATE_CURRENT_TERM_FEEDS = {}
JOB_LOAD_LRS_INCREMENTALS = {}
JOB_LOAD_ADVISING_NOTES = {}

LDAP_HOST = 'ldap-test.berkeley.edu'
LDAP_BIND = 'mybind'
LDAP_PASSWORD = 'secret'

# Loch LRS configs
LRS_DATABASE_URI = 'postgres://lrs:lrs@localhost:5432/lrs'

LRS_CANVAS_INCREMENTAL_REPLICATION_TASK_ID = 'task-id'
LRS_CANVAS_INCREMENTAL_TRANSIENT_BUCKET = 'transient bucket'
LRS_CANVAS_INCREMENTAL_TRANSIENT_PATH = 'lrs/transient/path'
LRS_CANVAS_INCREMENTAL_DESTINATION_BUCKETS = ['bucket', 'list']
LRS_CANVAS_INCREMENTAL_DESTINATION_PATH = 'lrs/destination/path'
LRS_CANVAS_INCREMENTAL_ETL_PATH_REDSHIFT = 'lrs/etl/path/redshift'

LRS_CANVAS_CALIPER_SCHEMA_PATH = 'lrs/path/to/caliper/schema'
LRS_CANVAS_CALIPER_INPUT_DATA_PATH = 'lrs/input/data/s3/location'
LRS_CANVAS_CALIPER_EXPLODE_OUTPUT_PATH = 'lrs/glue/output/s3/location'

LOCH_CANVAS_CALIPER_TIMESTAMP_DISCREPANCY_TOLERANCE = [-7200, 300]

LRS_CANVAS_GLUE_JOB_NAME = 'job_name_env'
LRS_CANVAS_GLUE_JOB_CAPACITY = 2
LRS_CANVAS_GLUE_JOB_TIMEOUT = 20
LRS_CANVAS_GLUE_JOB_SCRIPT_PATH = 's3://<bucket>/path/to/glue/script'
LRS_GLUE_TEMP_DIR = 'glue/temp/dir'
LRS_GLUE_SERVICE_ROLE = 'glue-service-role-name'

# Loch EDX configs
LOCH_EDX_NESSIE_ENV = 'deployment env'
LOCH_EDX_S3_BUCKET = 'edx-bucket-name'
LOCH_EDX_S3_WEEKLY_DATA_PATH = 'path/to/edx/weekly/data'
LOCH_EDX_S3_TRANSACTION_LOG_PATH = 'path/to/edx/transaction/log'

# Loch Nessie configs
LOCH_S3_BUCKET = 'bucket_name'
LOCH_S3_ENCRYPTION = 'AES256'
LOCH_S3_PROTECTED_BUCKET = 'protected_bucket_name'
LOCH_S3_PUBLIC_BUCKET = 'public_bucket_name'
LOCH_S3_REGION = 'us-west-2'

LOCH_S3_CANVAS_DATA_PATH_CURRENT_TERM = 'canvas/path/to/current/term'
LOCH_S3_CANVAS_DATA_PATH_DAILY = 'canvas/path/to/daily'
LOCH_S3_CANVAS_DATA_PATH_HISTORICAL = 'canvas/path/to/historical'

# The following paths are consistent across environments and do not need to be overridden locally.
LOCH_S3_ADVISING_NOTE_ATTACHMENT_DEST_PATH = 'sis-data/sis-sftp/historical/advising-notes/attachment-files'
LOCH_S3_ADVISING_NOTE_ATTACHMENT_SOURCE_PATH = 'sis-data/sis-sftp/incremental/advising-notes/attachment-files'
LOCH_S3_ASC_DATA_PATH = 'asc-data'
LOCH_S3_ASC_DATA_SFTP_PATH = 'asc-data/asc-sftp'
LOCH_S3_BOA_DATA_API_PATH = 'boa-data/boa-api'
LOCH_S3_BOAC_ANALYTICS_DATA_PATH = 'boac-analytics'
LOCH_S3_CAL1CARD_PHOTOS_PATH = 'cal1card-data/photos'
LOCH_S3_CALNET_DATA_PATH = 'calnet-data'
LOCH_S3_COE_DATA_PATH = 'coe-data'
LOCH_S3_E_I_DATA_SFTP_PATH = 'e-and-i-data'
LOCH_S3_SIS_DATA_PATH = 'sis-data'
LOCH_S3_SIS_API_DATA_PATH = 'sis-api-data'

LOCH_CANVAS_DATA_REQUESTS_CUTOFF_DATE = '20180101'

LOGGING_FORMAT = '[%(asctime)s] - %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
LOGGING_LOCATION = 'nessie.log'
LOGGING_LEVEL = logging.DEBUG
LOGGING_PROPAGATION_LEVEL = logging.INFO

# These RDS schemas are copied from the Redshift schemas below and contain a subset of index tables.
RDS_SCHEMA_ADVISING_NOTES = 'boac_advising_notes'
RDS_SCHEMA_ADVISOR = 'boac_advisor'
RDS_SCHEMA_ASC = 'boac_advising_asc'
RDS_SCHEMA_BOAC = 'boac_analytics'
RDS_SCHEMA_COE = 'boac_advising_coe'
RDS_SCHEMA_E_I = 'boac_advising_e_i'
RDS_SCHEMA_METADATA = 'metadata'
RDS_SCHEMA_SIS_ADVISING_NOTES = 'sis_advising_notes'
RDS_SCHEMA_SIS_INTERNAL = 'sis_data'
RDS_SCHEMA_STUDENT = 'student'
RDS_SCHEMA_UNDERGRADS = 'undergrads'

REDSHIFT_DATABASE = 'database'
REDSHIFT_HOST = 'redshift cluster'
REDSHIFT_PASSWORD = 'password'
REDSHIFT_PORT = 1234
REDSHIFT_USER = 'username'

REDSHIFT_IAM_ROLE = 'iam role'

# BOA limited access credentials to nessie rds and redshift
RDS_APP_BOA_USER = 'boa rds username'
REDSHIFT_APP_BOA_USER = 'boa redshift username'

# Redshift-side readonly role for dblink user mapping
REDSHIFT_DBLINK_GROUP = 'nessie_dblink_group'

# The following internal schemas are consistent across environments and do not need to be overridden locally.
REDSHIFT_SCHEMA_ADVISEE = 'boac_advisee'
REDSHIFT_SCHEMA_ADVISOR_INTERNAL = 'boac_advisor'
REDSHIFT_SCHEMA_ASC = 'boac_advising_asc'
REDSHIFT_SCHEMA_ASC_ADVISING_NOTES_INTERNAL = 'asc_advising_notes'
REDSHIFT_SCHEMA_BOAC = 'boac_analytics'
REDSHIFT_SCHEMA_CALIPER = 'lrs_caliper_analytics'
REDSHIFT_SCHEMA_COE = 'boac_advising_coe'
REDSHIFT_SCHEMA_E_I_ADVISING_NOTES_INTERNAL = 'e_i_advising_notes'
REDSHIFT_SCHEMA_EDW = 'edw_data'
REDSHIFT_SCHEMA_INTERMEDIATE = 'intermediate'
REDSHIFT_SCHEMA_SIS_INTERNAL = 'sis_data'
REDSHIFT_SCHEMA_STUDENT = 'student'
REDSHIFT_SCHEMA_SIS_ADVISING_NOTES_INTERNAL = 'sis_advising_notes'
REDSHIFT_SCHEMA_UNDERGRADS = 'boac_advising_undergrads'

# The following external schemas vary between environments and do need to be overridden locally.
REDSHIFT_SCHEMA_ADVISOR = 'External Advisor schema name'
REDSHIFT_SCHEMA_ASC_ADVISING_NOTES = 'External ASC Advising Notes schema name'
REDSHIFT_SCHEMA_CALNET = 'External CalNet schema name'
REDSHIFT_SCHEMA_CANVAS = 'External Canvas schema name'
REDSHIFT_SCHEMA_COE_EXTERNAL = 'External COE schema name'
REDSHIFT_SCHEMA_E_I_ADVISING_NOTES = 'External E&I Advising Notes schema name'
REDSHIFT_SCHEMA_LRS = 'External LRS schema name'
REDSHIFT_SCHEMA_SIS = 'External SIS schema name'
REDSHIFT_SCHEMA_SIS_ADVISING_NOTES = 'External SIS Advising Notes schema name'
REDSHIFT_SCHEMA_UNDERGRADS_EXTERNAL = 'External Undergrads schema name'

STUDENT_API_ID = 'secretid'
STUDENT_API_KEY = 'secretkey'
STUDENT_API_URL = 'https://secreturl.berkeley.edu/sis/v2/students'
STUDENT_V1_API_URL = 'https://secreturl.berkeley.edu/sis/v1/students'
STUDENT_V1_API_PREFERRED = False
STUDENT_API_MAX_THREADS = 5
# Although production API hosts use app_id/app_key headers, non-production environments may use basic auth.
STUDENT_API_PWD = None
STUDENT_API_USER = None

TERMS_API_ID = 'secretid'
TERMS_API_KEY = 'secretkey'
TERMS_API_URL = 'https://secreturl.berkeley.edu/terms'

VUE_LOCALHOST_BASE_URL = None

WORKER_HOST = 'hard-working-nessie.berkeley.edu'

# Thread queues will be ignored if "master" is embedded in the EB_ENVIRONMENT environment variable.
WORKER_QUEUE_ENABLED = True
WORKER_THREADS = 5
