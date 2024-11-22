<h1>automate-portfolio-site</h1>
Project to automate portfolio web site.<br><br>

Using automation to test web site with intention to use different frameworks.<br>
Folders are broken up into Frameworks and then separated by different programming lanugages.<br><br>
Framework:<br>
&emsp;- Playwright.<br>
&emsp;&emsp;- Pytest.<br>


<h2>Installation:</h2>
Playwright/Pytest:<br>
1) Run <code>pip install -r requirements.txt</code> in the 'playwright/pytest' project folder or 'run_requirements.bat' from the 'scripts' folder.<br>


<h2>Getting Started:</h2>
Playwright/Pytest:<br>
1) Run <code>python -m pytest -v</code> in the 'playwright/pytest' project folder or 'run_test.bat' file from the 'scripts' folder.<br>
&emsp;- This will run all of the script sections.<br><br>

> [!NOTE]
> Can only run specific sections with the below commands:<br>
> <code>python -m pytest -v -k test_portfolio_home.py</code><br>
> <code>python -m pytest -v -k test_portfolio_projects.py</code><br>
> <code>python -m pytest -v -k test_portfolio_about.py</code><br>
> <code>python -m pytest -v -k test_portfolio_contact.py</code><br>


  
