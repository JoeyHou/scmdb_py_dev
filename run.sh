source ./team/venv/bin/activate

# Compile react code using webpack
cd team
./node_modules/.bin/webpack

# Serve web app using flask on port 5050
cd ..
flask --app=team serve -p 5060
