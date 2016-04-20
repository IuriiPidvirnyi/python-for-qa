# 6 Having tuple  ('postgresql', 'semantic.amazonaws-prod.com', 5432, 'semantic', 'admin', '12345')
# -with production database connection properties (dialect, host, port, database name, user name, password), program should:
# -create  prod_config  dictionary, where dict keys are connection properties names and dict values are
# -appropriate values from the input tuple;
# -create  staging_config  dictionary with the same keys and values as  prod_config ;
# -in  staging_config  change host to 'semantic.amazonaws-staging.com' and password to 'root';
# -for  prod_config  and  staging_config  print connection strings in the following format  {dialect}://{user name}:{password}@{host}:{post}/{database name}

tupl = ('postgresql', 'semantic.amazonaws-prod.com', 5432, 'semantic', 'admin', '12345')
prod_config={'dialect':tupl[0],'host':tupl[1],'port':tupl[2],'database name':tupl[3],'user name':tupl[4],'password':tupl[5]}

staging_config=prod_config.copy()
staging_config['host']='semantic.amazonaws-staging.com'
staging_config['password']='root'

conn_prod="{}://{}:{}@{}:{}/{}".format(prod_config['dialect'],prod_config['user name'],prod_config['password'],prod_config['host'],prod_config['port'],prod_config['database name'])
print conn_prod

conn_stag="{}://{}:{}@{}:{}/{}".format(staging_config['dialect'],staging_config['user name'],staging_config['password'],staging_config['host'],staging_config['port'],staging_config['database name'])

print conn_stag