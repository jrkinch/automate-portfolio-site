<h1>automate-portfolio-site</h1>
Project to automate portfolio web site.<br><br>

<h2>Description:</h2>
Using automation to test web site with intention to use different frameworks.<br>
Folders are broken up into Frameworks and then separated by different programming lanugages/Frameworks.<br><br>
Framework:<br>
&emsp;- Playwright.<br>
&emsp;&emsp;- Pytest.<br>

<h2>Getting Started:</h2>

<h3>Playwright/Pytest:</h3>
<h4>Installation:</h4>
1. Clone the repo:

```console
git clone https://github.com/jrkinch/automate-portfolio-site.git
```

<br>
2. Install python dependencies from the 'playwright/pytest' project folder:

```console
pip install -r docs/requirements.txt
```
> [!TIP]
> Can also run the 'run_requirements.bat' from the 'scripts' folder.

<br>
3. Install the required browers for Playwright.

```console
playwright install
```

<h4>Testing:</h4>
1) Run tests from the 'playwright/pytest' project folder:<br>

```console
python -m pytest -v
```
> [!TIP]
> Can also run the 'run_test.bat' file from the 'scripts' folder..



> [!NOTE]
> Can run specific sections with the below commands from the 'playwright/pytest' project folder:<br>
```python
python -m pytest -v -k test_portfolio_home.py
```
```python
python -m pytest -v -k test_portfolio_projects.py
```
```python
python -m pytest -v -k test_portfolio_about.py
```
```python
python -m pytest -v -k test_portfolio_contact.py
```
