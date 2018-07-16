# App-specific configuration

# Serve the Bootstrap template locally
# Set to False due to SCCF's subfolder reverse proxy shenanigans, 
# which will cause HTML paths to fail
BOOTSTRAP_SERVE_LOCAL = False

# Disable pretty-printing to conserve network transfer
JSONIFY_PRETTYPRINT_REGULAR = False

# Minify HTML to conserve network transfer
MINIFY_PAGE = True

# Statement for enabling the development environment
#DEBUG = True

THREADS_PER_PAGE = 2

MAIL_SERVER = ''
MAIL_PORT = 
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG =  True
MAIL_USERNAME = ''
REQUEST_EMAIL = ''

MYSQL_USER = ''
MYSQL_PW = ''
MYSQL_DB_methylation = 'CEMBA'
MYSQL_DB_snATAC = 'CEMBA_snATAC'
MYSQL_SERVER_NAME = 'localhost'
SQLALCHEMY_BINDS = {'methylation_data': 'mysql://' + MYSQL_USER + ':' + MYSQL_PW + '@' + MYSQL_SERVER_NAME + '/' + MYSQL_DB_methylation,
                    'snATAC_data': 'mysql://' + MYSQL_USER + ':' + MYSQL_PW + '@' + MYSQL_SERVER_NAME + '/' + MYSQL_DB_snATAC}

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = ''

SECRET_KEY = ''

APPLICATION_ROOT = '/portal'
