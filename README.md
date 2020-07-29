# Beginner_Loggin_non_secure
A few practice programs to simulate a login prompt. Added bcrypt to v1 of QT_log_and_pass.py. I included my failed attempts and a working non-secure version in this repo to show and remind myself how I tackled this problem/project.
<h2>QT_log_and_pass.py</h2><br>
<p>This is going to be my secure login program. It currently uses bcrypt to store the hashed password in user_name_password.db. First time running this you will need to uncomment lines 13-20 in order to create the db and then recomment when you run again. Files login_fun.py and create_account_fun.py are required.</p>
<h4>To Do:</h4>
<ul>
  <li>Censor user inputs</li>
  <li>Add more labels for user guidence such as input requirements</li>
</ul><br><br>
<h2>Login_non_secure.py:</h2><br>
<ul>
  <li>My first attempt, used on the command line and with a txt file.</li>
  <li>txt file name needs to be 'logandpass.txt' to store and read usernames and passwords.
      You can change the name of the files it uses on lines 12 and 44</li>
</ul><br><br>
<h2>Fail_test_tkinter.py, Fail_root_tkinter.py:</h2><br>
<ul>
  <li>My second attempt using a gui this time and sqlite.</li>
  <li>Uncomment lines 23 and 24 for the first time you run so a table can be madenamed uandp.</li>
  <li>Comment out lines 18 and 19 or change the file location to a picture you'd like to use for the window icon.</li>
</ul>
