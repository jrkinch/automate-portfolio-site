'''
    project testing portfolio about page using playwright and pytest.
    
    Run all: python -m pytest -v
    Run only this section: python -m pytest -v -k test_portfolio_about.py

    Notes:
    - different navbar vs sitemap:
        #get_by_role("list").get_by_role("link", name="Home") #navbar item
        #get_by_role("contentinfo").get_by_role("link", name="Home") #footer item


'''
import pytest
from playwright.sync_api import Playwright, Page, expect
import re

#Menu NAVBAR
def test_menu_home_button(page: Page):
    page.goto("https://jrkinch.github.io/pages/about.html#about")
    
    page.get_by_role("list").get_by_role("link", name="Home").click()
    
    expect(page).to_have_title(re.compile("Welcome"))
    expect(page.get_by_role("heading", name="Passion For Quality.")).to_be_visible()
    expect(page).to_have_url("https://jrkinch.github.io/index.html#home")
    
def test_menu_projects_button(page: Page):
    page.goto("https://jrkinch.github.io/pages/about.html#about")
    
    page.get_by_role("list").get_by_role("link", name="Projects").click()
    
    expect(page).to_have_title(re.compile("Projects"))
    expect(page).to_have_url("https://jrkinch.github.io/pages/projects.html#projects")

def test_menu_about_button(page: Page):
    page.goto("https://jrkinch.github.io/pages/about.html#about")
    
    page.get_by_role("list").get_by_role("link", name="About").click()
    
    expect(page).to_have_title(re.compile("About"))
    expect(page.get_by_role("heading", name="More about me:")).to_be_visible()
    expect(page).to_have_url("https://jrkinch.github.io/pages/about.html#about")

def test_menu_contact_button(page: Page):
    page.goto("https://jrkinch.github.io/pages/about.html#about")
    
    page.get_by_role("list").get_by_role("link", name="Contact").click()
    
    expect(page).to_have_title(re.compile("Contact me"))
    expect(page.get_by_role("heading", name="Get in touch")).to_be_visible() 
    expect(page).to_have_url("https://jrkinch.github.io/pages/contact.html#contact")


#FOOTER
def test_footer_sitemap_home(page: Page):
    page.goto("https://jrkinch.github.io/pages/about.html#about")
    
    page.get_by_role("contentinfo").get_by_role("link", name="Home").click()
    
    expect(page).to_have_title(re.compile("Welcome"))
    expect(page.get_by_role("heading", name="Passion For Quality.")).to_be_visible()
    expect(page).to_have_url("https://jrkinch.github.io/index.html#home")
    
def test_footer_sitemap_projects(page: Page):
    page.goto("https://jrkinch.github.io/pages/about.html#about")
    
    page.get_by_role("contentinfo").get_by_role("link", name="Projects").click()
    
    expect(page).to_have_title(re.compile("Projects"))
    expect(page).to_have_url("https://jrkinch.github.io/pages/projects.html#projects")

def test_footer_sitemap_about(page: Page):
    page.goto("https://jrkinch.github.io/pages/about.html#about")
    
    page.get_by_role("contentinfo").get_by_role("link", name="About").click()
    
    expect(page).to_have_title(re.compile("About"))
    expect(page.get_by_role("heading", name="More about me:")).to_be_visible()
    expect(page).to_have_url("https://jrkinch.github.io/pages/about.html#about")

def test_footer_sitemap_contact(page: Page):
    page.goto("https://jrkinch.github.io/pages/about.html#about")
    
    page.get_by_role("contentinfo").get_by_role("link", name="Contact").click()
    
    expect(page).to_have_title(re.compile("Contact me"))
    expect(page.get_by_role("heading", name="Get in touch")).to_be_visible()
    expect(page).to_have_url("https://jrkinch.github.io/pages/contact.html#contact")

def test_footer_gh_image(page: Page):   
    page.goto("https://jrkinch.github.io/pages/about.html#about")
    
    expect(page.get_by_alt_text("GitHub")) 
    
def test_footer_goto_gh_link(page: Page):
    page.goto("https://jrkinch.github.io/pages/about.html#about")
    page.get_by_role("link", name="GitHub").click()
    
    expect(page).to_have_title(re.compile("jrkinch"))
    expect(page).to_have_url("https://github.com/jrkinch")
   
def test_footer_li_image(page: Page):   
    page.goto("https://jrkinch.github.io/pages/about.html#about")
    
    expect(page.get_by_alt_text("LinkedIn"))  
    
def test_footer_goto_li_link(page: Page):
    page.goto("https://jrkinch.github.io/pages/about.html#about")
    page.get_by_role("link", name="LinkedIn").click()
    page.wait_for_timeout(5000)#linkedIn sometimes takes a while to load
    
    expect(page).to_have_title(re.compile(".*Jason Kinch | LinkedIn"))
    expect(page).to_have_url(re.compile(".*jason-kinch"))#needs regex search as url uses random auth redirect


#PAGE Contents
def test_page_more_title(page: Page):   
    page.goto("https://jrkinch.github.io/pages/about.html#about")
    
    expect(page.get_by_role("heading", name="More about me:")).to_be_visible()

def test_page_more_descrip_one(page: Page):   
    page.goto("https://jrkinch.github.io/pages/about.html#about")
    
    expect(page.get_by_text("I am a passionate and talented Software Quality Engineer with many years of experience including a focus on Test Case Development, Manual Testing, and Automation. I have used those skills testing consumer electronics to cover a wide range of components ranging from firmware, mobile apps, developing scripts, and battery simulation to release products to market.")).to_be_visible()

def test_page_more_descrip_two(page: Page):   
    page.goto("https://jrkinch.github.io/pages/about.html#about")
    
    expect(page.get_by_text("I have a Bachelor's Degree in Computer Science with a major in Game Development. When I am not dabbling with different projects, I like learning new technologies and playing video games.")).to_be_visible()

def test_page_tech_title(page: Page):   
    page.goto("https://jrkinch.github.io/pages/about.html#about")
    
    expect(page.get_by_role("heading", name="Technologies:")).to_be_visible()
    
def test_page_tech_python_check(page: Page):   
    page.goto("https://jrkinch.github.io/pages/about.html#about")
    
    expect(page.get_by_alt_text("Python")).to_be_visible()
    expect(page.get_by_text("Python")).to_be_visible() 

def test_page_tech_html_check(page: Page):   
    page.goto("https://jrkinch.github.io/pages/about.html#about")
    
    expect(page.get_by_alt_text("HTML")).to_be_visible()
    expect(page.get_by_text("HTML5")).to_be_visible()

def test_page_tech_css_check(page: Page):   
    page.goto("https://jrkinch.github.io/pages/about.html#about")
    
    expect(page.get_by_alt_text("CSS")).to_be_visible()
    expect(page.get_by_text("CSS3")).to_be_visible()

def test_page_tech_java_check(page: Page):   
    page.goto("https://jrkinch.github.io/pages/about.html#about")
    
    expect(page.get_by_alt_text("Java")).to_be_visible()
    expect(page.get_by_text("Java")).to_be_visible()

def test_page_tech_sql_check(page: Page):   
    page.goto("https://jrkinch.github.io/pages/about.html#about")
    
    expect(page.get_by_alt_text("SQL")).to_be_visible()
    expect(page.get_by_text("SQL")).to_be_visible()

def test_page_tech_powershell_check(page: Page):   
    page.goto("https://jrkinch.github.io/pages/about.html#about")
    
    expect(page.get_by_alt_text("Powershell")).to_be_visible()
    expect(page.get_by_text("Powershell")).to_be_visible() 