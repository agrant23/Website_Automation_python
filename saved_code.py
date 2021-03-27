#Saved code

#unused Chrome commands thinking it will help with headless

options.add_argument('--no-sandbox')
options.add_argument('--allow-running-insecure-content')
options.add_argument('--proxy-server="direct://"')
options.add_argument('--proxy-bypass-list=*')   #needed very much so
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-pre-commit-inpu') #new
options.add_argument('--disable-crash-reporter')
#options.add_argument('--dump-dom')                 #this broke it, created a Resource warning
options.add_argument('--enable-crash-reporter')
#options.add_argument('--font-render-hinting')      #this broke it, created a Resource warning